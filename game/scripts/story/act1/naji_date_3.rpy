label naji_date_3:
    play sound "/audio/pencil-write.mp3"
    scene city-morning with fade:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}Week [week]{/size}{/font}{/color}{color=#000000}{color=#000000}{font=JustAnotherHand-Regular.ttf}{size=200}\n Weekend!{/size}{/font}{/color}" at truecenter with wiperight
    pause

    stop music
    play sound "/audio/impact-slam.mp3"
    scene menmi-apartment-morning with vpunch:
        matrixcolor InvertMatrix(value=1.0)
    i "You're up early for a weekend."

    scene menmi-apartment-morning
    play sound "/audio/subway-door.mp3"
    m "Yeah, I have a train to catch..."

    scene bakery with pushleft
    play sound "/audio/outdoor-crowd.mp3" volume 0.7
    m "...A hype train, that is!"

    play music "<from 9>audio/cloud.wav"

    m """A celebrity chef downtown just dropped the latest pastry craze – a combination of a waffle and a macaroon.

    They call it...The Wackaroon.

    And I consider it my civic duty to stay on the cutting board's edge of pastry innovation.

    So here I am, outside Jujube Bakery, standing on a line that wraps almost entirely around the block.
    """

    scene bakery with dissolve:
        matrixcolor BrightnessMatrix(value=0.7)
    scene bakery with dissolve:
        matrixcolor BrightnessMatrix(value=0.5)
    scene bakery with vpunch

    m """
    Feeling both antsy and sleepy at the same time, I fight to stay on my feet as the front of the line comes into view.

    A worker comes out and hangs a “SOLD OUT” sign over the Wackaroons.
    """

    play sound "/audio/impact-slam.mp3"
    scene bakery with vpunch:
        matrixcolor BrightnessMatrix (value=1.0)
    play sound "/audio/impact-slam.mp3"
    scene bakery with vpunch

    m "NOOOOOOOOO!"

    if self_awareness<=70:
        play sound "/audio/impact-slam.mp3"
        scene bakery with vpunch:
            matrixcolor InvertMatrix(value=1.0)
        # Related Insights: I have to be better about that; It's deserved; how else will I learn?; I'll learn from my mistakes
        i "If you were capable, you'd have gotten here earlier."
        scene bakery with vpunch

    m "As I marinate in regret, looking woefully through the unWackmarkable leftovers, a familiar golden head comes into view."

    show naji-neutral with dissolve
    play music "/audio/najis-theme.mp3"
    n "“Looks like you just Menmissed out.”"

    play sound "/audio/impact-slam.mp3"
    scene bakery with vpunch
    show naji-smile

    m """
    He's sending my overcaffeinated heart into overdrive.

    “Don't sneak up on me like that!”

    "What are you doing here? We weren't supposed to meet until later.”
    """
    hide naji-smile
    show naji-neutral
    n "“I know. I was just picking up a treat.”"
    m"""
    He holds out a white paper bag and-OH MY SQUASH.

    “Is that-?”
    """

    hide naji-neutral
    show naji-laugh

    m "Naji cackles riotously, lording the bag over my head."

    n "“Sorry, Men. You know what they say -- 'the early bird whacks the worm.'”"
    hide naji-laugh
    show naji-surprised

    m "“Nobody says that, you macaroon.”"
    n "“Is that any way to talk to someone who’s wacked his worm?”"
    m "“That sound better in your head?”"
    hide naji-surprised
    show naji-neutral
    n "“Yea.”"

    #Relevant Insights: I have regrets.; I have to be better about that.; I need to be a better person.; Trick question, still me.; What if things don't go as planned?
    m "He *is* right about being punctual, though. As hard as it is to admit, he *did* earn it by being here early."

    if self_awareness>=100:
        #Relevant Insights: Naji prioritizes the needs of others before his own; He used to follow me around and do whatever I wanted; It's nice to know that I'm capable of achieving happiness for myself.; He's a good guy
        m """
        But this is Naji we're talking about.

        "“Please, Naji? Just a tiny bite? A sliver!”"
        """
        hide naji-neutral
        show naji-smile
        m "A quirk passes the edge of his lips."
        $ renpy.notify("Naji feels closer to you!")
        $ naji_relationship += 5
        n "“Ha, ya caught me.”"

    #Relevant Insights: He's always had a way with people. Got the rizz, as they say; He's a good guy.; He was my best friend
    n "“You knew I was planning on sharing them with you all along, right?”"

    #Relevant Insights: It's all coming true like I planned; It's nice to know that I'm capable of achieving happiness for myself.
    m "“No cap. Shall we eat these in the park?”"

    scene park-day with pixellate

    m "“Hello my Menminions! Welcome to Menmi's Wackaroon Reaction! Featuring...Naji!”"

    show naji-frown with dissolve

    n """
    *Sigh*

    “Is this necessary?”
    """

    #Relevant Insight: Meeting new people, experiencing new things, chasing down a whirlwind romance..
    m """
    "It for my Instayam story!"

    I hold the macaroon to the camera, getting a good shot of the brightly colored waffle texture.

    As I take a bite out of the disc, I hand over the other half for Naji.

    """

    if self_awareness >=100:
        m "Why's he just staring at it like that?"
        c "Why'd the Behemoth want to drink from your bottle?"


    play sound "/audio/sparkle.mp3" volume 0.7
    scene park-day with dissolve:
        matrixcolor BrightnessMatrix (value=1.0)
    scene park-day with dissolve

    m """
    The macaroon is delicious!

    The outer shell is a perfect balance between chewy and soft. The smooth, sweet filling creates a magical mouthfeel that contrasts with the bumpy waffle crust.
    """

    show naji-neutral with dissolve
    #Relevant Insights: Why is Naji's opinion of me such a big deal?
    m """
    I take a peek next to me, trying to assess Naji's reaction.

    He's staring straight ahead, throat bobbing slowly as he swallows.
    """

    n "“Good! {w}So yummy. {w}Wow.”"

    $ n3=True
    jump after_naji_date
