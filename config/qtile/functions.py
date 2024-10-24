#--------------------------------------------------------------------------------
#                                                                   
#  ,------.                        ,--.  ,--.                       
#  |  .---',--.,--.,--,--,  ,---.,-'  '-.`--' ,---. ,--,--,  ,---.  
#  |  `--, |  ||  ||      \| .--''-.  .-',--.| .-. ||      \(  .-'  
#  |  |`   '  ''  '|  ||  |\ `--.  |  |  |  |' '-' '|  ||  |.-'  `) 
#  `--'     `----' `--''--' `---'  `--'  `--' `---' `--''--'`----'  
#                                                                   
#             
#      , _ ,        RESUME:  Functions for Qtile configuration.
#     ( o o )                It inclues brightness control, power menu, etc.
#    /'` ' `'\
#    |'''''''|      AUTHOR:  Andr3xDev
#    |\\'''//|      URL:  https://github.com/Andr3xDev/Qtile-Dotfiles
#       """
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# Imports
#--------------------------------------------------------------------------------

import os
import subprocess

from libqtile import hook
from libqtile.lazy import lazy
from qtile_extras.popup.toolkit import PopupRelativeLayout, PopupImage, PopupText

from colors import colors


#--------------------------------------------------------------------------------
# Defaults
#--------------------------------------------------------------------------------


imageDefaults = {
    "mask": True,
    "colour": colors[1],
    "highlight_radius": 10,
    "highlight_border": -10,
}


textDefaults = {
    "font": "jetbrains mono nerd font",
    "fontsize": 14,
    "h_align": "center",
    "foreground": colors[1],
}


layoutDefaults = {
    "border_width": 2,
    "border": colors[1],
    "background": colors[0],
    "hide_on_mouse_leave": True,
}



#--------------------------------------------------------------------------------
# Functions
#--------------------------------------------------------------------------------


def powerMenu(qtile):
    controls = [
        PopupImage(
            filename = "~/.config/qtile/images/terminal.svg",
            pos_x = 0.15,
            pos_y = 0.15,
            width = 0.1,
            height = 0.5,
            **imageDefaults,
            highlight = colors[3],
            mouse_callbacks = {
                "Button1": lazy.shutdown()
            },
        ),
        PopupImage(
            filename = "~/.config/qtile/images/reboot.svg",
            pos_x = 0.45,
            pos_y = 0.15,
            width = 0.1,
            height = 0.5,
            **imageDefaults,
            highlight = colors[3],
            mouse_callbacks = {
                "Button1": lazy.spawn("reboot")
            }
        ),
        PopupImage(
            filename = "~/.config/qtile/images/shutdown.svg",
            pos_x = 0.75,
            pos_y = 0.15,
            width = 0.1,
            height = 0.5,
            **imageDefaults,
            highlight = "A00000",
            mouse_callbacks = {
                "Button1": lazy.spawn("shutdown now")
            }
        ),
        PopupText(
            text = "Quit Qtile",
            pos_x = 0.1,
            pos_y = 0.75,
            width = 0.2,
            height = 0.2,
            **textDefaults,
        ),
        PopupText(
            text = "Reboot",
            pos_x = 0.4,
            pos_y = 0.75,
            width = 0.2,
            height = 0.2,
            **textDefaults,
        ),
        PopupText(
            text = "Shutdown",
            pos_x = 0.7,
            pos_y = 0.75,
            width = 0.2,
            height = 0.2,
            **textDefaults,
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width = 1000,
        height = 200,
        controls = controls,
        initial_focus = 1,
        opacity = 0.8,
        **layoutDefaults,
    )

    layout.show(centered=True)


#--------------------------------------------------------------------------------
# Hooks
#--------------------------------------------------------------------------------

@hook.subscribe.client_new
def center_floating_win(window):
    wm_name = window.cmd_inspect()["name"]
    if wm_name == "Calendar" or wm_name == "Available updates":
        window.toggle_floating()
        window.cmd_set_size_floating(1000, 600)


@hook.subscribe.screen_change
def screen_change(event):
    monitorScript = os.path.expanduser("~/.config/qtile/scripts/monitors.sh")
    subprocess.run([monitorScript])


@hook.subscribe.startup_once
def autostart():
    autostartScript = os.path.expanduser("~/.config/qtile/scripts/autostart.sh")
    monitorScript = os.path.expanduser("~/.config/qtile/scripts/monitors.sh")
    subprocess.run([autostartScript])
    subprocess.run([monitorScript])