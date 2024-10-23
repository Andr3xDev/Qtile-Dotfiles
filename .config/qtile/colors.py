#--------------------------------------------------------------------------------
#                                           
#   ,-----.       ,--.                      
#  '  .--./ ,---. |  | ,---. ,--.--. ,---.  
#  |  |    | .-. ||  || .-. ||  .--'(  .-'  
#  '  '--'\' '-' '|  |' '-' '|  |   .-'  `) 
#   `-----' `---' `--' `---' `--'   `----'  
#                                           
#             
#      , _ ,        RESUME:  Declare colors for the rice, just to keep it clean
#     ( o o )                and organized, it will be applied automatically
#    /'` ' `'\
#    |'''''''|      AUTHOR:  Andr3xDev
#    |\\'''//|      URL:  https://github.com/Andr3xDev/Qtile-Dotfiles
#       """                                              
#--------------------------------------------------------------------------------


#----------------------------------------------------------------------------
# Themes and basic transparent color
# Here u can switch and declarate colors of the rice.
#----------------------------------------------------------------------------

transparent = "#00000000"


freiren_blue = [            
    "#00181D", #background
    "#D0BBE4", #foreground            
    "#855FA9", #borders and groups
    "#815FBD", #groupbox and highlights
]

freiren2 = [            
    "#0B2123", #background
    "#f8f8f2", #foreground            
    "#bd93f9", #borders and groups
    "#815FBD", #groupbox and highlights
]

cyberpunk_lucy = [            
    "#181a1a", #background
    "#ffffff", #foreground            
    "#cfcfcf", #borders and groups
    "#697565", #groupbox and highlights
]


#----------------------------------------------------------------------------
# Colors variable used in other files
#----------------------------------------------------------------------------

colors = cyberpunk_lucy         #Change the colors used in the rice here
colors.append(transparent)