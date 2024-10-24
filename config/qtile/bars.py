#--------------------------------------------------------------------------------
#                                                                                                   
#  ,-----.                         
#  |  |) /_  ,--,--.,--.--. ,---.  
#  |  .-.  \' ,-.  ||  .--'(  .-'  
#  |  '--' /\ '-'  ||  |   .-'  `) 
#  `------'  `--`--'`--'   `----'  
#                      
#             
#      , _ ,        RESUME: Config the bars of Qtile, one for each screen. It
#     ( o o )              includes the widgets and their settings and workspaces.
#    /'` ' `'\
#    |'''''''|      AUTHOR:  Andr3xDev
#    |\\'''//|      URL: https://github.com/Andr3xDev/Qtile-Dotfiles
#       """                                              
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# Imports
#--------------------------------------------------------------------------------

from libqtile import bar
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

from colors import colors
from keybinds import defaultApps
from functions import powerMenu


#--------------------------------------------------------------------------------
# Defaults and recurring variable settings
#--------------------------------------------------------------------------------

widget_defaults = {
    "font": "Roboto",
    "fontsize": 12,
    "padding": 10,
    "background": colors[-1],
    "foreground": colors[0],
}

widgetDecorations = {
    "background": colors[0],
    "foreground": colors[1],
    "decorations": [
        RectDecoration(use_widget_background = True, radius = 12, filled = True, group = True),
    ],
}

barConfig = {
    "size":         24,
    "margin":       [4, 6, 2, 6],
    "border_width": [0, 0, 0, 0],
    "border_color": [colors[-1], colors[-1], colors[-1], colors[-1]],
    "background": colors[-1]
}


#--------------------------------------------------------------------------------
# Bar templates
#--------------------------------------------------------------------------------

leftWidgets = [
    #CPU image
    widget.TextBox(
        font = "Font Awesome 6 Free Regular",
        fmt = "",
        **widgetDecorations,
    ),
    widget.Spacer(
        length = -8,
        padding = 0,
        **widgetDecorations
    ),
    #CPU
    widget.CPU(
        format = '{load_percent}%',
        update_interval = 5.0,
        **widgetDecorations,
    ),
    widget.Spacer(
        length = 10,
    ),
    #RAM image
    widget.TextBox(
        font = "Font Awesome 6 Free Regular",
        fmt = "",
        **widgetDecorations,
    ),
    widget.Spacer(
        length = -8,
        padding = 0,
        **widgetDecorations
    ),
    #RAM text
    widget.Memory(
        format = '{MemPercent}%',
        update_interval = 5.0,
        **widgetDecorations
    ),
    widget.Spacer(
        length = 10,
    ),
    widget.BatteryIcon(
        theme_path = "~/.config/qtile/images/",
        scale = 1.6,
        **widgetDecorations,
    ),
    widget.Spacer(
        length = -15,
        padding = 0,
        **widgetDecorations
    ),
    widget.Battery(
        format = "{percent: 2.0%}",
        **widgetDecorations,
    ),
    widget.Spacer(
        length = 10,
    ),
    #Volume icon
    widget.Volume(
        font = "Font Awesome 6 Free Regular",
        emoji = True,
        emoji_list = ['', '', '', ''],
        volume_app = defaultApps["sound"],
        **widgetDecorations,
    ),
    widget.Spacer(
        length = -6,
        padding = 0,
        mouse_callbacks = {"Button1": lazy.spawn(defaultApps["sound"])},
        **widgetDecorations
    ),
    #Volume text
    widget.Volume(
        mute_foreground = colors[1] + "90",
        mute_format = "Muted",
        volume_app = defaultApps["sound"],
        **widgetDecorations,
    ),
    widget.Spacer(
        length = 10,
    ),
]


mainSpecificWidgets = [
    #Update checker
    widget.CheckUpdates(
        font = 'Font Awesome 6 Free Regular',
        distro = 'Arch_checkupdates',
        display_format = ' ! ',
        no_update_string = '',
        update_interval = 30,
        mouse_callbacks = {"Button1": lazy.spawn(defaultApps["terminal"] + ' --hold --title "Available updates" checkupdates')},
        **widgetDecorations,
    ),
    widget.Spacer(
        length = 10,
    ),
    widget.Spacer(
        length = bar.STRETCH,
    ),
    # Workspaces
    widget.GroupBox(
        spacing = 6,
        padding_x = 5,
        padding_y = 0,
        margin_x = 10,
        fontsize = 14,
        borderwidth = 0,
        inactive = colors[1],
        active = colors[1],
        block_highlight_text_color = colors[0],
        this_current_screen_border = colors[2],
        this_screen_border = colors[2],
        other_current_screen_border = colors[3],
        other_screen_border = colors[3],
        highlight_method = 'block',
        rounded = True,
        visible_groups = ["1", "2", "3", "4", "5", "6"],
        **widgetDecorations,
    ),
    widget.Spacer(
        length = bar.STRETCH,
    ),
    widget.Spacer(
        length = 10,
    ),
]

# Second monitor bar
secondSpecificWidgets = [
    widget.CheckUpdates(
        font = 'Font Awesome 6 Free Regular',
        distro = 'Arch_checkupdates',
        display_format = ' ! ',
        no_update_string = '',
        update_interval = 30,
        mouse_callbacks = {"Button3": lazy.spawn(defaultApps["terminal"] + ' --hold --title "Available updates" checkupdates')},
        **widgetDecorations,
    ),
    widget.Spacer(
        length = 10,
    ),
    widget.WindowName(
        format = "{name}",
    ),
    widget.Spacer(
        length = bar.STRETCH,
    ),
    widget.GroupBox(
        spacing = 6,
        padding_x = 5,
        padding_y = 0,
        margin_x = 10,
        fontsize = 14,
        borderwidth = 0,
        inactive = colors[1],
        active = colors[1],
        block_highlight_text_color = colors[0],
        this_current_screen_border = colors[2],
        this_screen_border = colors[2],
        other_current_screen_border = colors[3],
        other_screen_border = colors[3],
        highlight_method = 'block',
        rounded = True,
        visible_groups = ["6", "7", "8", "9", "0"],
        **widgetDecorations,
    ),
    widget.Spacer(
        length = bar.STRETCH,
    ),
]


rightWidgets = [
    # Bluetooth image
    widget.Bluetooth(
        font = "Font Awesome 6 Free Regular",
	    mouse_callbacks = {"Button1": lazy.spawn(defaultApps["bluetooth"])},
        default_text = "",
        default_show_battery = True,
        opacity = 0.85,
        hide_after = 0.1,
        highlight_colour = colors[2],
        highlight_radius = 10,
        menu_background = colors[0],
        menu_border = colors[1],
        menu_border_width = 2,
        menu_foreground = colors[1],
        menu_foreground_highlighted = colors[0],
        menu_font = "Roboto",
        menu_offset_x = -20,
        menu_offset_y = 15,
        **widgetDecorations  
    ),
    widget.Spacer(
        length = -8,
        padding = 0,
        mouse_callbacks = {"Button1": lazy.spawn(defaultApps["bluetooth"])},
        **widgetDecorations
    ),
    # Bluetooth text
    widget.Bluetooth(
        mouse_callbacks = {"Button1": lazy.spawn(defaultApps["bluetooth"])},
        adapter_format = "{name}",
        default_text = "{num_connected_devices}",
        default_show_battery = True,
        opacity = 0.85,
        hide_after = 0.1,
        highlight_colour = colors[2],
        highlight_radius = 10,
        menu_background = colors[0],
        menu_border = colors[1],
        menu_border_width = 2,
        menu_foreground = colors[1],
        menu_foreground_highlighted = colors[0],
        menu_font = "Roboto",
        menu_offset_x = -20,
        menu_offset_y = 15,
        **widgetDecorations  
    ),
    widget.Spacer(
        length = 10,
    ),
    widget.WiFiIcon(
        mouse_callbacks = {"Button1": lambda: None, "Button1": lazy.spawn(defaultApps["network"])},
        active_colour = colors[1],
        padding_y = 7,
        **widgetDecorations,
    ),
    widget.Spacer(
        length = -8,
        padding = 0,
        mouse_callbacks = {"Button3": lazy.spawn(defaultApps["network"])},
        **widgetDecorations
    ),
    widget.Wlan(
        mouse_callbacks = {"Button3": lazy.spawn(defaultApps["network"])},
        format = "{essid}",
        disconnected_message = "Disconnected",
        ethernet_message = "Wired",
        use_ethernet = True,
        **widgetDecorations,
    ),
    widget.Spacer(
        length = 10,
    ),
    widget.TextBox(
        font = "Font Awesome 6 Free Regular",
        fmt = "",
        **widgetDecorations,
    ),
    widget.Spacer(
        length = -8,
        padding = 0,
        **widgetDecorations
    ),
    widget.Clock(
        format = "%I:%M",
        timezone = "America/Bogota",
        **widgetDecorations,
    ),
    widget.Spacer(
        length = 10,
    ),
    #Calendar icon
    widget.TextBox(
        font = "Font Awesome 6 Free Regular",
        fmt = "",
	    mouse_callbacks = {"Button1": lazy.spawn(defaultApps["calendar"])},
        **widgetDecorations,
    ),
    widget.Spacer(
        length = -8,
        padding = 0,
        **widgetDecorations
    ),
    #Calendar text
    widget.Clock(
        format = "%d.%m.%Y",
	    mouse_callbacks = {"Button1": lazy.spawn(defaultApps["calendar"])},
        **widgetDecorations,
    ),
    widget.Spacer(
        length = 10,
    ),
    #PowerMenu
    widget.TextBox(
        font = "Font Awesome 6 Free Regular",
        fmt = "",
	    mouse_callbacks = {"Button1": lazy.function(powerMenu)},
        **widgetDecorations,
    )
]


#--------------------------------------------------------------------------------
# Declaration of the bars

# System tray widget can be used only once
# It has to be deleted from the second bar
# uncomment the secondBar variable and the secondBar declaration to use it

mainBar = bar.Bar(leftWidgets + mainSpecificWidgets + rightWidgets, **barConfig)
secondBar = bar.Bar(leftWidgets + secondSpecificWidgets + rightWidgets, **barConfig)