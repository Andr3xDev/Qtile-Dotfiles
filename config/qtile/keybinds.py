#--------------------------------------------------------------------------------
#                                                                   
#  ,--. ,--.                ,-----.  ,--.,--.           ,--.        
#  |  .'   / ,---. ,--. ,--.|  |) /_ |  |`--',--,--,  ,-|  | ,---.  
#  |  .   ' | .-. : \  '  / |  .-.  \|  |,--.|      \' .-. |(  .-'  
#  |  |\   \\   --.  \   '  |  '--' /|  ||  ||  ||  |\ `-' |.-'  `) 
#  `--' '--' `----'.-'  /   `------' `--'`--'`--''--' `---' `----'  
#                  `---'                                            
#             
#      , _ ,        RESUME:  My personal keybinds for Qtile, you can change
#     ( o o )                the keybinds to your liking, or add more.
#    /'` ' `'\
#    |'''''''|      AUTHOR:  Andr3xDev
#    |\\'''//|      URL: https://github.com/Andr3xDev/Qtile-Dotfiles
#       """                                              
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# Imports
#--------------------------------------------------------------------------------

from libqtile.config import Key, Click, Drag
from libqtile.lazy import lazy

from functions import powerMenu
from groups import groups



#--------------------------------------------------------------------------------
# Default apps and the mod key
# Here you can change the default apps that will be opened with the keybinds.
#--------------------------------------------------------------------------------

mod = "mod4"
alt = "mod1"

defaultApps = {
    "terminal": "kitty",
    "browser": "firefox",
    "fileMan": "thunar",
    "calendar": "kitty --title Calendar calcurse",
    "sound": "pipeware",
    "network": "nm-connection-editor",
    "bluetooth": "blueman-manager",
}


#--------------------------------------------------------------------------------
# Keybinds for window management and opening apps 
#--------------------------------------------------------------------------------
    
keys = [
    ##### Focus Window #####
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "r", lazy.layout.next(), desc="Move window focus to other window"),
    
    ##### Move Window In Workspace #####
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    
    ##### Rezise Focus Window #####
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    ##### General actions #####
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "v", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod], "s", lazy.window.move_down(), desc="Bring the window down"),
    Key([mod], "w", lazy.window.move_up(), desc="Bring the window up"),
    Key([mod], "q", lazy.window.move_to_top(), desc="Bring the window to the top"),
    Key([mod], "a", lazy.window.move_to_bottom(), desc="Bring the window to the bottom"),

    ##### General actions #####
    Key([mod], "Return", lazy.spawn(defaultApps["terminal"]), desc="Launch the terminal"),
    Key([mod], "b", lazy.spawn(defaultApps["browser"]), desc="Launch the browser"),
    Key([mod], "e", lazy.spawn(defaultApps["fileMan"]), desc="Launch the file manager"),
    Key([mod], "Print", lazy.spawn("flameshot gui"), desc="Choose the part of the screen for a screenshot"),
    Key([mod, "shift"], "Print", lazy.spawn("flameshot screen"), desc="Screenshot of the entire screen"),
    Key([mod, "control"], "Print", lazy.spawn("flameshot full"), desc="Screenshot of all of the monitors"),
    Key([mod, "shift"], "p", lazy.spawn("picom"), desc="Enable picom"),
    Key([mod, "control"], "p", lazy.spawn("killall picom"), desc="Disable picom"),

    ##### Change Workspace #####
    Key([mod, alt], "Left", lazy.screen.prev_group(), desc="Change focus to the previous screlazy.next_screen()en"),
    Key([mod, alt], "Right", lazy.screen.next_group(), desc="Change focus to the next screen"),

    ##### Change focus screen #####
    Key([mod, alt], "Down", lazy.prev_screen(), desc="Change focus to the preview screen"),
    Key([mod, alt], "Up", lazy.next_screen(), desc="Change focus to the next screen"),

    ##### Menus #####
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.function(powerMenu), desc="Show Power Menu"),
    Key([mod], "space", lazy.spawn('rofi -show drun -theme ~/.config/rofi/config.rasi'), desc="Launch rofi menu"),

    ##### Sound #####
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
]


#--------------------------------------------------------------------------------
# Keybinds for groups
#--------------------------------------------------------------------------------

for i in groups:  
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc="Switch to & move focused window to group {}".format(i.name)),
        Key([mod, "control"], i.name, lazy.window.togroup(i.name), desc="Move focused window to group {}".format(i.name)),
    ])


#--------------------------------------------------------------------------------
# Drag floating layouts
#--------------------------------------------------------------------------------

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]