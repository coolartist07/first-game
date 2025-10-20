# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")
define d = Character("Doodlebob")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg washington

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show doodlebob base

    # These display lines of dialogue.

    d "You've created a new Ren'Py game."

    d "Once you add a story, pictures, and music, you can release it to the world!"

    d "The current version of the game is 1.0, last updated: 10/20/2025"

    # This ends the game.

    return
