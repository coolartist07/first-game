# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")
define d = Character("Doodlebob")
define j = Character("Julius")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg castle

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show doodlebob base

    # These display lines of dialogue.

    d "You've created a new Ren'Py game."

    d "Once you add a story, pictures, and music, you can release it to the world!"

    d "The current version of the game is 1.0, last updated: 10/20/2025"

    d "I recall a time when you were younger, you wouldn't stop throwing a tantrum 
    until I refilled your glass with more orange juice! I was new to the job too, 
    so you really had me worried I'd lose it as soon as I got it!"


    hide doodlebob base
    show julius base

    j "I-I'm sorry about that, Doodlebob."

    hide julius base
    show doodlebob base

    d "It was the only way you knew how to get what you wanted, so I understood."

    hide doodlebob base
    show julius base

    j "There's so many people yelling, though. And they sound mad at us. 
    Why would they be mad at us, Doodlebob? Have we done something to make them angry?"

    hide julius base
    show doodlebob base

    d "Now, dearest, this is not your fault. Your mother and father will take care of the commotion 
    so you can have a good night's rest. I'll be waiting for you in the morning with your favorite breakfast. 
    So, quickly! The sooner you sleep, the sooner you can eat it!"

    # This ends the game.

    return
