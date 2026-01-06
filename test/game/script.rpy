# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")
define d = Character(_("Doodlebob"), color = "414288")
define j = Character(_("Julius"), color = "FF8D21")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg castle
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show doodlebob base

    # These display lines of dialogue.

    d "You've created a new Ren'Py game."

    d "Once you add a story, pictures, and music, you can release it to the world!"

    d "The current version of the game is 1.0, last updated: 10/20/2025"

    j "Why is there always a commotion every night at our door, Doodlebob?"

    "Doodlebob's been their housemaid for ages, so he knows how to quell the young master's curiosity."

    d "There are some who can only have their voices heard if they make a ruckus."

    j "But why? Couldn't they just wait 'til morning to talk with Father?"

    d "I recall a time when you were younger, you wouldn't stop throwing a tantrum 
    until I refilled your glass with more orange juice! I was new to the job too, 
    so you really had me worried I'd lose it as soon as I got it!"


    hide doodlebob base
    show julius base

    "Julius looked away, embarrassment coloring his cheeks."

    j "I-I'm sorry about that, Doodlebob."

    hide julius base
    show doodlebob base

    d "It was the only way you knew how to get what you wanted, so I understood."

    hide doodlebob base
    show julius base

    "Julius looks up again, brows knitted together out of confusion."

    j "There's so many people yelling, though. And they sound mad at us. 
    Why would they be mad at us, Doodlebob? Have we done something to make them angry?"

    hide julius base
    show doodlebob base

    "Doodlebob's expression dawns a sad smile now, eyes hiding a deep pain he couldn't pick out easily. 
    After a brief moment, he takes his hand and gives it a squeeze."

    d "Now, dearest, this is not your fault. Your mother and father will take care of the commotion 
    so you can have a good night's rest. I'll be waiting for you in the morning with your favorite breakfast. 
    So, quickly! The sooner you sleep, the sooner you can eat it!"

    hide doodlebob base

    "His fingers touched the cold glass, but something within him decided to linger before closing it." 
   
    "The night air nipped at his nose. Though cold, it was refreshing compared to the stuffy palace air he's been 
    inhaling most of his life. The stars twinkled above him, beckoning him to come outside and search them more. 
    He needed to leave, but he hesitated."

    # Learning the choice mechanic

    label choice1:
        j "(Father and Mother would send out the entire cavalry if they noticed I was missing. I'd never be allowed to leave again. 
        And yet...)"
    menu:
        "Sneak out":
            jump sneakout

        "Close the window":
            jump close_window

    label sneakout:
        j "It'll only be for an hour or two. I'm usually a good kid, so this should be fine!"
        jump end_story

    label close_window:
        j "(It's probably for the best I stay in. Everything will be okay by tomorrow.)"
        "Julius closes the window, heading back to bed."

    label end_story:

    # This ends the game.

    return
