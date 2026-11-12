label intro: #The prologue of the game.

    #show neil_test base
    show max_b office
    show max_h hair1
    show max_f happy1
    show neil_test base at right

    #nvl narration flashback

    $ renpy.pause(1.0)
    scene black
    #play music somberbattle1 fadein 1.0
    "Year 1459, Caris Calendar."
    "The Tower of the Celestial Tree."
    nar2 "On top of a sacred tower, an angel faces his superior. The flowers below are stained in crimson, corrupted by artificial starfire, losing their once white pure glow." 
    nar2 "For the Archangel, this is a new beginning. Angelkind will soon enter a glorious new dawn, where they will no longer be shackled by the past, and rise past the oppression of the god Acarion."
    nar2 "For the angel, this is an ending. To the end of a false dream, prophesied by a man who grew corrupt with power, and lost his soul along the way. Ending him here would be a mercy."
    nar2 "Beside the angel are allies from his long journey, unified by a single purpose."
    nar2 "The priest who found his true faith. The adventurer who found the end of that yellow brick road. And the demon who learned to love."
    #play sound rainfall fadein 1.0
    nar2 "The rain falls unceasingly, the pattering of drops in sync with the beat of their racing hearts. With bonds forged in fire, unable to be dampened by the seemingly hopeless situation in front of them, they stand together as one."
    nar2 "The Archangel looks at the young men with a bored gaze. For him, this was nothing. Just another group of insurgents trying to rebel against the status quo. Useless. They could not even compare to the power he wielded."
    nar2 "He looks to the angel holding his sword in defiance. Once upon a time, they were comrades. But now, he is nothing but an enemy - and enemies must be eliminated. Swiftly, efficiently, and mercilessly."
    "The angel looks back to the Archangel, holding his breath. He..."
    menu:
        "...tried to reason with the Archangel, one last time.":
            jump reason
        "...attacked immediately.":
            jump attack

    # Close up shot of falling n
    n "{i}Life was so simple.{w=1} Just follow orders and everything will be just alright.{/i}"
    n "{i}Fulfill your role in society and everyone will be happy.{/i}"
    n "{i}That's{w=0.1}.{w=0.1}.{w=0.1}. {w=1}what the Archangel says.{w=1} So{w=0.1}.{w=0.1}.{w=0.1}.{/i}"
    # Zooms out to full view
    n "{i}How did things turn out like this{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}?{/i}"

    $ renpy.pause(2.0)

    # This ends the game.

    return