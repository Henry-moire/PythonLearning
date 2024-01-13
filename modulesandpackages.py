#Modules in Python are just Python files with a .py extension.
#Importing module objects to the current namespace
# game.py
# import the draw module
from draw import draw_game

def main():
    result = play_game()
    draw_game(result)

#Importing all objects from a module
# game.py
# import the draw module
from draw import *

def main():
    result = play_game()
    draw_game(result)

#Modules may be loaded under any name you want.
import draw_visual as draw

#Module initialization
# draw.py

def draw_game():
    # when clearing the screen we can use the main screen object initialized in this module
    clear_screen(main_screen)
    ...

def clear_screen(screen):
    ...

class Screen():
    ...

# initialize main_screen as a singleton
main_screen = Screen()

#Extending module load path
PYTHONPATH=/foo python game.py
#This executes game.py, and enables the script to load modules from the foo directory, as well as the local directory.
#You may also use the sys.path.append function. Execute it before running the import command:
sys.path.append("/foo")