# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init: 
    # Define characters
    define n = Character("Nathaniel", ctc = "arrow", ctc_position = "fixed")
    define test = Character("???")
    define nar2 = nvl_narrator
    

image arrow:
    "arrow.png" 
    zoom 0.2 
    xpos 0.95, ypos 0.99, xanchor 1.0, yanchor 1.0

image neil_test base = Transform("images/sprites/test/neil_test.png", zoom=0.56, crop=(0, 0, 1.0, 0.70))

image max_b office =  Transform("images/sprites/max/body/max-b-casual.png", zoom=0.56, crop=(0, 0, 1.0, 0.70))
image max_h hair1 =  Transform("images/sprites/max/hair/max-h-hair1.png", zoom=0.56, crop=(0, 0, 1.0, 0.70))
image max_f happy1 =  Transform("images/sprites/max/face/max-f-happy1.png", zoom=0.56, crop=(0, 0, 1.0, 0.70))

define fade_to_black = Fade(1.0, 0.0, 1.0)

# Transforms
transform appear_left:
    xalign -1.0
    linear 0.5 xalign 0.0

transform appear_right:
    xalign 2.0
    linear 0.5 xalign 1.0

transform slide_left:
    ease 0.5 xalign 0.8

transform slide_left2:
    ease 0.5 xalign 0.5

transform slide_left3:
    ease 5.0 xalign 0.2


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    $ renpy.pause(1.0)

    centered "Testing{w=0.1}.{w=0.1}.{w=0.1}."

    nvl clear

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    $ renpy.pause(2.0)

    scene bg room
    with fade_to_black

    #show neil_test base
    show max_b office
    show max_h hair1
    show max_f happy1
    show neil_test base at right

    # Close up shot of falling n
    n "{i}Life was so simple.{w=1} Just follow orders and everything will be just alright.{/i}"
    n "{i}Fulfill your role in society and everyone will be happy.{/i}"
    n "{i}That's{w=0.1}.{w=0.1}.{w=0.1}. {w=1}what the Archangel says.{w=1} So{w=0.1}.{w=0.1}.{w=0.1}.{/i}"
    # Zooms out to full view
    n "{i}How did things turn out like this{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}?{/i}"

    $ renpy.pause(2.0)

    # This ends the game.

    return
