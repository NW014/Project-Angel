label testing: #For animation tests

    show marty angy1 at left
    show pietro neutral at right

    m "I had enough of you!"
    p "Huh?"

    show marty angy2 as marty at attack_left

    $ renpy.pause(0.3)

    show hit effect at right
    show pietro hurt1 as pietro at damaged1

    $ renpy.pause(2.0)

    show marty angy1 as marty
    show pietro hurt2

    p "What did I ever do to you?"

    show pietro angy1

    p "Take that!"

    show pietro angy2 at attack_right

    $ renpy.pause(0.3)

    show hit effect at left
    show marty hurt1 at damaged1

    $ renpy.pause(0.5)

    show marty at damaged2

    $ renpy.pause(2.0)
    show marty faint as marty

    m "Ugh..."

    show marty at faint

    $ renpy.pause(2.0)



    