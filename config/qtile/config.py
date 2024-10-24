#--------------------------------------------------------------------------------
#                                                                              
#  ,--.   ,--.        ,--.             ,-----.                ,---.,--.        
#  |   `.'   | ,--,--.`--',--,--,     '  .--./ ,---. ,--,--, /  .-'`--' ,---.  
#  |  |'.'|  |' ,-.  |,--.|      \    |  |    | .-. ||      \|  `-,,--.| .-. | 
#  |  |   |  |\ '-'  ||  ||  ||  |    '  '--'\' '-' '|  ||  ||  .-'|  |' '-' ' 
#  `--'   `--' `--`--'`--'`--''--'     `-----' `---' `--''--'`--'  `--'.`-  /  
#                                                                      `---'
#             
#      , _ ,        RESUME:  General configuration for Qtile, like layouts,
#     ( o o )                sizes, some rules, etc.
#    /'` ' `'\
#    |'''''''|      AUTHOR:  Andr3xDev
#    |\\'''//|      URL: (Pendiente)
#       """                                              
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# Imports
#--------------------------------------------------------------------------------

from libqtile import layout
from libqtile.config import Match, Screen

from bars import widget_defaults, mainBar, secondBar
from colors import colors
from keybinds import *
from functions import *


#--------------------------------------------------------------------------------
# Layout settings
#--------------------------------------------------------------------------------

layoutTheme = {
    "border_focus": colors[2], 
    "border_normal": colors[0], 
    "border_width": 2, 
    "margin": 5
}

# Select column layout type
layouts = [
    layout.Columns(**layoutTheme),
]

# Apps that opens in floating mode
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class = "confirmreset"),  # gitk
        Match(wm_class = "makebranch"),  # gitk
        Match(wm_class = "maketag"),  # gitk
        Match(wm_class = "ssh-askpass"),  # ssh-askpass
        Match(title = "branchdialog"),  # gitk
        Match(title = "pinentry"),  # GPG key password entry

        # System control
        Match(wm_class = "pavucontrol"),
        Match(wm_class = "nm-connection-editor"),
        Match(wm_class = "blueman-manager"),
        Match(wm_class = "gnome-disks"),

        # Communication
        Match(wm_class = "whatsdesk"),
        Match(wm_class = "discord"),

        # Others
        Match(wm_class = "qalculate-gtk"),
    ],
    **layoutTheme
)


#--------------------------------------------------------------------------------
# Screens settings
#--------------------------------------------------------------------------------

#Wallpaper select
wallpaperSettings = {
    "wallpaper": "~/.config/wallpapers/wall_CR.jpg",
    "wallpaper_mode": "fill",
}

screens = [
    Screen(
        top = mainBar,
        **wallpaperSettings,
    ),
    # If you have a second monitor, uncomment this line and organize code
    Screen(
        top = secondBar, 
        **wallpaperSettings,
    ),
]


#--------------------------------------------------------------------------------
# Miscelanous settings
#--------------------------------------------------------------------------------

dgroups_key_binder = None
dgroups_app_rules = []  # type: list 
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False

# If something Java related is not working, set this to "LG3D"
wmname = "Qtile"