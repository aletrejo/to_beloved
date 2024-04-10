
# Dynamic characters
default behemoth_name = "???"
define be = Character("[behemoth_name]", color="#A9A9A9")
default joule_name = "???"
define j = Character("[joule_name]", color="#0064C2", image="joule")
default devan_name = "???"
define d = Character("[devan_name]", color='#800DCD', image="dev")
default naji_name = "???"
define n = Character("[naji_name]", color='#E59A34',  image="naji")


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Menmi", color='#F52088')
define c = Character("Conscience", color='#DB694F')
define u = Character("Delivery Guy", color="#6c431a", image="delivery-guy.png")
define al = Character("Allie", color="#66b704", image="allie")
define i = Character("Intrusive Inner Voice", color='#023F59')



# Global variables
default self_awareness = 0
default naji_relationship = 0
default joule_relationship = 0
default dev_relationship = 0
default week = 1
default n1 = False
default n2 = False
default n3 = False
default passed_checks = 0
default planner_cover = 1
# Images used in-game
image tutorial box = "tutorial-box.png"
image ol_text = Text("Self-Awareness Check: Passed", style='outlined_text')
image bubbless = SnowBlossom("bubble-3.png", count=30, yspeed=(-150, -90), start=3)
image bubblesm = SnowBlossom("bubble-1.png", count=28, yspeed=(-130, -100))
image bubblesl = SnowBlossom("bubble-2.png", count=46, yspeed=(-120, -50), start=5)


# Splashscreen
label splashscreen:
    screen splash():
        add "images/city-night.png" at citynightappear
        add "images/main-menu-naji.png" at najiappear
        add "images/main-menu-joule.png" at jouleappear
        add "images/main-menu-dev.png" at devappear
        add "images/main-menu-menmi.png" at menmiappear
        add "images/main-menu-title.png" at titleappear
        add "images/main-menu-navbg.png" at navappear
    show screen splash
    with Pause(10.5)
    hide screen splash
    return

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "<from 5>/audio/cloud.wav"
    scene menmi-apartment-morning
    with vpunch


    # These display lines of dialogue.

    m """
    Oof. That's the last one!

    I didn't expect to be carrying so much stuff from my parents' place up to my new apartment

    So {i}this{/i} is what they mean by 'walk-up.' Ooooooooohhh...

    But, hey! I got a steal on this place with rent! It's more shoebox than studio, but it's Home – here in Applecore City!
    """

    scene applecore-city
    with dissolve

    play sound "/audio/inhale.mp3"

    m """
    Isn't it just the picture of perfection? The staggering skyscrapers, the constant commotion of the crowds,
    the mystery odors of human body gumbo.

    My life starts now. Look out world, Menmi is officially entering her City Biddy Era.

    You can't see it, but I'm twerking right now. Do I know how to twerk? Just trust.
    """

    play sound "/audio/doorbell.wav"

    m "Ah! That's the first time I've heard the door buzzer. It's a shock to the senses." with vpunch

    scene menmi-apartment-morning
    with dissolve

    m """
    I look down at my bare feet and the tissue-thin camisole I'm wearing.

    Whoops! Definitely going to need a fig leaf for that nip.

    I can't let anyone know I have nipples!!!

    I tear open a box labeled “Clothes” and throw on a roomy sweatshirt that only mildly smells like teenage regret.
    """

    play sound "/audio/stomping.wav"

    m "“Be right there!”"

    scene menmi-apartment-door
    with dissolve

    show delivery-guy with dissolve

    m """
    Standing in the doorway is a tall mystery man holding a small cardboard box.

    He's kind of hot. I can't help but notice how big his hands look wrapped around that tiny box.

    I wonder how they'd look around my...

    hand.

    Oooh, Menmi! Don't get “carried away” by the UPS Man!
    """

    u "“I've got a package for Ms. Menmi?”"

    m """
    “Yes, that's me!”

    As he hands me the package, I feel electricity sparking at the brief synapse between our fingers.

    Is this...chemistry?
    """

    scene menmi-apartment-door:
        blur 24

    show delivery-guy at center:
        blur 24

    m """
    What would it be like to date a delivery man? It'd be kinda wild to be with someone so in-demand in this post-pandemic,
    pro-postal world.

    Like, he'd find excuses to come visit me – “Oh I'm just in the neighborhood because of a delivery,”
    but his roguish grin and the takeout for two will say otherwise.

    You're doing some essential work to my heart, baby.

    It sounds so romantic!

    """
    stop music
    play music "<from 13>/audio/cave-streams.mp3"
    play sound "/audio/impact-slam.mp3"
    scene menmi-apartment-door with vpunch:
        blur 24
        matrixcolor InvertMatrix(value=1.0)

    show delivery-guy at center:
        matrixcolor InvertMatrix(value=1.0)

    i "It sounds like a bad idea. What if you get murderobbed??  Or worse, what if he rejects you?"

    m """
    Hush! I wish my brain settle down with these *second thoughts* or whatever. Where do these voices even come from?

    Of course I see the practical perils of pickup, but love is a risk worth taking!
    """
    stop music
    play music "<from 5>/audio/cloud.wav"
    scene menmi-apartment-door:
        blur 24
    show delivery-guy at center:
        blur 0

    m "“Would you like to put that down...inside?”"

    u "“Ma'am, please just sign for the package.”"
    show delivery-guy at center with vpunch:
        blur 0
    play sound "/audio/impact-slam.mp3"

    m "Ignored. What's *that* supposed to mean?"


    menu:
        m "How should I interpret his silence?"

        "He rejected you.":
            $ renpy.notify("+0 Self-Awareness")
            c "So cringe. You don't even have a couch. Were you planning on having him sit on the toilet?"
            $ self_awareness += 0
            jump no_self_awareness_tutorial

        "He's probably in a rush":
            $ renpy.notify("+5 Self-Awareness")
            c "We're in Applecore City, girl. People are busy! You shot your shot and got what ya got. Onward!"
            $ self_awareness += 5
            jump self_awareness_tutorial

label no_self_awareness_tutorial:
    window hide
    show tutorial-box-awareness
    screen no_self_awareness():
        vbox:
            xalign 0.5
            yalign 0.5
            xmaximum 1000
            box_wrap True
            text """
            {size=-5}Looks like Menmi just missed out on some {b}Self-Awareness{/b}, but no worries — we're all learning.

            {b}Self-Awareness{/b} allows Menmi to distinguish between the voices that help and the ones that hinder. Having a more informed sense of self helps Menmi navigate the world with fewer distortions about herself and those around her.

            As {b}Menmi's Conscience{/b}, you can not only help her make sound decisions, but process events mindfully and kindfully so that she can both gain critical insight into her own behaviors and maintain a healthy sense of self.
            {/size}"""
    show screen no_self_awareness with dissolve
    pause
    hide screen no_self_awareness
    hide tutorial box
    jump after_tutorial

label self_awareness_tutorial:
    window hide
    show tutorial-box-awareness
    screen self_awareness():
        vbox:
            xalign 0.5
            yalign 0.5
            xmaximum 1000
            box_wrap True
            text """
            {size=-5}
            Nice job — Menmi just gained some {b}Self-Awareness{/b}.

            {b}Self-Awareness{/b} allows Menmi to distinguish between the voices that help and the ones that hinder. Having a more informed sense of self helps Menmi navigate the world with fewer distortions about herself and those around her.

            As {b}Menmi's Conscience{/b}, you can not only help her make sound decisions, but process events mindfully and kindfully so that she can both gain critical insight into her own behaviors and maintain a healthy sense of self.
            {/size}
            """
    show screen self_awareness with dissolve
    pause
    hide screen self_awareness
    hide tutorial box
    jump after_tutorial

label after_tutorial:
    scene applecore-city
    with dissolve
    m """
    I push a sturdy box over to the small desk by the window and sit on it, examining the package label.

    Oh, it's from Mom!

    Ripping open the package reveals a cute planner with some sticker sheets.

    There's a note on it:

    {i}Menmi — I worry for you, my little scatterbrains. Use this to stay organized.{/i}

    {i}Love, Mom{/i}

    Wow! This planner just my style!

    She knows me so well! It's like she's my mom or something.

    I guess I {i}could use{/i} a little break from unpacking.
    """
label pick_planner_pattern:
    screen patterns():
        text "{size=+20}{b}Which cover should I use?{/b}":
                xalign 0.5
                yalign 0.2
        imagebutton:
            xalign 0.2
            yalign 0.5
            auto "planner-pattern-1 %s" action Jump("planner_with_pattern_1")
        imagebutton:
            xalign 0.4
            yalign 0.5
            auto "planner-pattern-2 %s" action Jump("planner_with_pattern_2")
        imagebutton:
            xalign 0.6
            yalign 0.5
            auto "planner-pattern-3 %s" action Jump("planner_with_pattern_3")
        imagebutton:
            xalign 0.8
            yalign 0.5
            auto "planner-pattern-4 %s" action Jump("planner_with_pattern_4")
    show screen patterns with dissolve
    pause
label planner_with_pattern_1:
    $ planner_cover = 1
    hide screen patterns
    image cover_1 = "planner-cover-1.png"
    show cover_1 
    jump planner_tutorial
label planner_with_pattern_2:
    $ planner_cover = 2
    hide screen patterns
    image cover_2 = "planner-cover-2.png"
    show cover_2 
    jump planner_tutorial
label planner_with_pattern_3:
    $ planner_cover = 3
    hide screen patterns
    image cover_3 = "planner-cover-3.png"
    show cover_3 
    jump planner_tutorial
label planner_with_pattern_4:
    $ planner_cover = 4
    hide screen patterns
    image cover_4 = "planner-cover-4.png"
    show cover_4 
    jump planner_tutorial
label planner_tutorial:
    window hide
    show tutorial box
    screen planner():
        vbox:
            xalign 0.5
            yalign 0.5
            xmaximum 1000
            box_wrap True
            text "{size=+10}{i}Menmi's Planner{/i}":
                xalign 0.5
            text "Menmi's planner isn't just her schedule, it's also a journal! (Listen, everyone has side hustles nowadays, even planners). Check back to see her thoughts on each activity throughout the week."
    show screen planner with dissolve
    pause
    hide screen planner
    hide tutorial box
    window show
    m """
    *Gasp*...Oh my god?

    It's *perfect*? Did I really do this? Great job, Menmi. Take that, expectations!

    Whose expectations? I'm not sure!
    """
    scene planner with dissolve
    m """
    OK. Time to fill it out. Blank pages sure are intimidating.

    It's a good thing I know what my weekday schedule already looks like.

    Morning workouts, work during the day, and party after-hours. I just have to drop the stickers into the right place.
    """
    window hide
    call screen planner_drag(_with_none=False) with dissolve
    with dissolve
label planner_tutorial_success:
    scene gym-inside with dissolve
    m "Mornings are at the gym! Gotta start the day strong with my favorite workout — Spotting hot guys."
    scene office-inside with dissolve
    m "Primetime is grind time. I managed to land my dream job at a PR firm. I’m so excited to make a difference in the world!"
    scene lounge-inside with dissolve
    m "At the end of the day, I'll unwind with a drink. One of my friends from home is a bartender! Ooooohh getting wasted on a weeknight? We grow up so fast"
    scene menmi-apartment-afternoon with dissolve
    m "And weekends? Weekends are when the magic happens so I'll have to choose how to utilize them carefully."
    scene planner-weekend1 with dissolve
    m "Pretty sure I'm going to be washed after my first week, so I'm going to take a cleansing bath."

label choosing_prince:
    scene applecore-city with dissolve
    stop music fadeout 1.0
    play music "<from 20>/audio/reaching-the-sky.mp3" fadein 0.5

    m """
    There! My perfect first week in the perfect city at the start of my perfect life — perfectly planned!

    I'm supporting myself with my own money in my own apartment in the BIG CITY! Complete independence!

    And then all I'll need to be complete is the perfect partner. Love is the greatest goal of all, and I've been preparing to fall in love *only* my whole life

    A girls' gotta be ready. That's why I know *exactly* what I'm looking for.
    """
    menu:
        m "My prince charming is..."

        "Friendly, loyal, and compassionate":
            $ naji_relationship += 5
            m "Someone who's kind, spends lots of time with me, and puts our love first. Obviously, I want him to be as crazy about me as I definitely will be about him."
        "Strong and protective":
            $ joule_relationship += 5
            m "Someone who's always got my back and makes me feel safe from the dangerous world! What's dangerous about it? I don't know. Maybe that's part of the problem."
        "Effortlessly cool and competent":
            $ dev_relationship += 5
            m "A mature person who strides through life with unwavering confidence, admired by all. He's always in control...until {i}I{/i} make him lose it."
    m """
    Whew! Manifesting my dream man into existence is hard work.

    Just kidding! I could literally do this all day. {w}And I will!

    I’m not naive, though. I know the world isn’t all sunshine and six-packs.
    """

    menu:
        m "I know *all* the red flags:"

        "Flawed first impressions that transform into a lasting love":
            m """ A string of misunderstandings! A tense, yet thrilling rivalry.

            Witty banter! Stubborn prides! The belated realization that your petty enmity is rooted in an unshakeable sense of trust!

            Ah, the initial bitterness makes the happy ending all the sweeter.
            """
        "Traditional family members who don't want to see us together":
            m """
            His dad, a CEO mafia boss undercover buddy cop sultan, forbids him from consorting with commoners,

            lest he be lured away from his responsibility to the family “business”.

            Us against the world! Overthrowing the patriarchy! Singing out the moon roof of a limousine!

            """
        "Vengeful exes hellbent on sabotaging our happiness":
            m """
            Naturally, he'll be a man in demand.

            I'll never forget how desirable he is because his ex(es) will constantly be coming after me like they don't have anything better to do!

            Nobody wants to work anymore! And why would they when you can ride the highs of hopeless infatuation?

            """

        "A tragic accident that leaves us forever changed":
            m """
            What would I lose? A hand? An eye? Consciousness? Gosh I hope I don't go into a coma – that would be so boring. For *me*.

            *Gasp* Maybe my beautiful singing voice? I don't have a beautiful singing voice, but maybe I can look into podcasting?

            """

        "Supernatural secrets threatening to doom our fragile love":
            m """
            Aaaahh what if he's an 800-year-old vampire nurse who's honest and lonely, but also resentful and idealistic?

            And I die before him? Oh my gosh I hope he isn't mad at me for that!
            """
    scene menmi-apartment-afternoon with dissolve
    m """
    We might struggle, but it’s OK, because at the end of the day, hardship happens to test our love!

    Love is the answer - to everything.

    We'll overcome the odds and make each other more perfect and whole.

    To feel, finally, in this cold, lonely world, the safe haven of love...it’s the height of the human experience.

    If you don’t believe in that, what’s life even for?
    """
    menu:
        m "So there's only one way my story can end:"
        "They lived happily ever after":
            m "It'll happen. I know it will. Everything is coming to pass, just as I planned it."
    scene applecore-city with dissolve
    m "Now that my story's been written, all that's left to do is live it!"
    window hide


    show image "title-screen.png" with dissolve
    show text "{font=PatuaOne-Regular.ttf}{size=150}{color=#d33c59}To BeLoved{/size}{/font}" at truecenter
    with dissolve
    pause

    play sound "/audio/impact-slam.mp3"
    show image "title-screen.png":
        matrixcolor InvertMatrix(value=1.0)
    show text "{font=PatuaOne-Regular.ttf}{size=150}{color=#FFFFFF}To BeLoved{/size}{/font}" at truecenter
    with hpunch
    pause
    show image "title-screen.png" with dissolve:
        matrixcolor InvertMatrix(value=0.0)
    hide text with dissolve
    jump week_1_morning
