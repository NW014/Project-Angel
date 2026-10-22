# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init: 
    # Define characters
    define n = Character("Nathaniel", ctc = "arrow", ctc_position = "fixed")
    define test = Character("???")
    define nar2 = nvl_narrator
    define m = Character("Marty")
    define p = Character("Pietro")
    

image arrow:
    "arrow.png" 
    zoom 0.2 
    xpos 0.95, ypos 0.99, xanchor 1.0, yanchor 1.0

image neil_test base = Transform("images/sprites/test/neil_test.png", zoom=0.56, crop=(0, 0, 1.0, 0.70))

image max_b office =  Transform("images/sprites/max/body/max-b-casual.png", zoom=0.56, crop=(0, 0, 1.0, 0.70))
image max_h hair1 =  Transform("images/sprites/max/hair/max-h-hair1.png", zoom=0.56, crop=(0, 0, 1.0, 0.70))
image max_f happy1 =  Transform("images/sprites/max/face/max-f-happy1.png", zoom=0.56, crop=(0, 0, 1.0, 0.70))

image marty angy1 = Image("images/sprites/test/marty_mad_closed.png")
image marty angy2 = Image("images/sprites/test/marty_mad_open.png")
image marty hurt1 = Image("images/sprites/test/marty_hurt1.png")
image marty hurt2 = Image("images/sprites/test/marty_hurt2.png")
image marty faint = Image("images/sprites/test/marty_faint.png")
image pietro neutral = Image("images/sprites/test/pietro_neutral.png")
image pietro hurt1 = Image("images/sprites/test/pietro_hurt1.png")
image pietro hurt2 = Image("images/sprites/test/pietro_hurt2.png")
image pietro angy1 = Image("images/sprites/test/pietro_mad_closed.png")
image pietro angy2 = Image("images/sprites/test/pietro_mad_open.png")

image testhit = Image("images/anim/hit_effect/hit008.png")

image hit effect:
    "images/anim/hit_effect/hit002.png"
    pause 0.05
    "images/anim/hit_effect/hit003.png"
    pause 0.05
    "images/anim/hit_effect/hit004.png"
    pause 0.05
    "images/anim/hit_effect/hit005.png"
    pause 0.05
    "images/anim/hit_effect/hit006.png"
    pause 0.05
    "images/anim/hit_effect/hit007.png"
    pause 0.05
    "images/anim/hit_effect/hit008.png"
    pause 0.05
    "images/anim/hit_effect/hit009.png"
    pause 0.05
    "images/anim/hit_effect/hit010.png"
    pause 0.05
    "images/anim/hit_effect/hit011.png"
    pause 0.05
    "images/anim/hit_effect/hit012.png"
    pause 0.05
    "images/anim/hit_effect/hit013.png"
    pause 0.05
    "images/anim/hit_effect/hit014.png"
    pause 0.05
    "images/anim/hit_effect/hit015.png"
    pause 0.05
    "images/anim/hit_effect/hit000.png"
    pause 0.05


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

transform attack_left:
    ease 0.1 zoom 1.5 offset (-256, 256)
    ease 0.2 zoom 1.0 offset (0, 0)

transform attack_right:
    ease 0.1 zoom 1.5 offset (256, 256)
    ease 0.2 zoom 1.0 offset (0, 0)

transform damaged1:
    ease 0.1 offset (10, 0)
    ease 0.1 offset (-10, 0)
    ease 0.1 offset (0, 0)

transform damaged2:
    ease 0.2 offset (20, 20)
    pause 0.1
    ease 0.2 offset (-20, 30)
    pause 0.1
    ease 0.2 offset (0, 40)

transform faint:
    alpha 1.0
    linear 0.3 yoffset 100 alpha 0.0


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene black

    #$ renpy.pause(1.0)

    #centered "Testing{w=0.1}.{w=0.1}.{w=0.1}."

    #nvl clear

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    #$ renpy.pause(2.0)

    scene bg room
    with fade_to_black

    jump testing
