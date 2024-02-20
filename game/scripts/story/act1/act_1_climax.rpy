label act_1_climax:
    stop music fadeout 2.0
    play sound "/audio/pencil-write.mp3"
    scene city-morning with fade:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}Week [week]{/size}{/font}{/color}{color=#000000}{color=#000000}{font=JustAnotherHand-Regular.ttf}{size=200}\n Weekend!{/size}{/font}{/color}" at truecenter with wiperight
    pause

    scene menmi-apartment-morning with blinds
    play music "/audio/reaching-the-sky.mp3" fadein 2.0

    m """
    *Yawn* Good mourning, everybody.

    No, that's not a misspelling. I'm grieving the loss of my decision-making faculties.
    """

    #play audio barbling

    m "Ow...why'd I drink so much last night?"
