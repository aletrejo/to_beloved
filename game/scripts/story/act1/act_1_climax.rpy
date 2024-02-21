label act_1_climax:
    stop music fadeout 2.0
    play sound "/audio/pencil-write.mp3"
    scene city-morning with fade:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}Week [week]{/size}{/font}{/color}{color=#000000}{color=#000000}{font=JustAnotherHand-Regular.ttf}{size=200}\n Weekend!{/size}{/font}{/color}" at truecenter with wiperight
    pause

    scene menmi-apartment-morning with blinds

    m """
    *Yawn* Good mourning, everybody.

    No, that's not a misspelling. The "U" is silent, but still an active participant{w} ;)

    I'm grieving the loss of my decision-making faculties.
    """

    play sound "/audio/swallow.mp3"
    scene menmi-apartment-morning with flash
    scene menmi-apartment-morning with hpunch

    m "Ow...why'd I drink so much last night?"
    i "Take a guess."

    if self_awareness>=60:
        $ unlocks_dialogue = ["I hope he doesn't think I'm silly for wanting to be in love"]
        $ dialogue_matches = []
        $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
        if len(dialogue_matches) > 0:
            show screen insight(dialogue_matches)
        m "I was...feeling lonely."

    if self_awareness<60:
        $ unlocks_dialogue = ["I don't know...or maybe I'm not ready to face it yet. I need more insight on this."]
        $ dialogue_matches = []
        $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
        if len(dialogue_matches) > 0:
            show screen insight(dialogue_matches)
        m "Because I'm cool?"
        i "That's so funny I forgot what I was even thinking about."

    play music "<from 5>/audio/siberian-express.mp3" fadein 5.0

    $ unlocks_dialogue = ["Everyone has to believe in something, and I choose to believe in love!"]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    m """
    *Sigh* I've been in the city for more than a month now, so why haven't I found love?

    It defies explanation.
    """

    i "I've got one: {w}Nobody wants you."

    scene menmi-apartment-morning with dissolve:
        matrixcolor BrightnessMatrix (value=-0.4)
    scene menmi-apartment-morning with flash:
        matrixcolor BrightnessMatrix (value=-0.4)
        matrixcolor SaturationMatrix (value=0.2)

    i """It's obvious. {w}You're defective, {w}and everyone can see it.

    Like a pit stain on that knock-off Louis Mutton blouse you paid way too much for at that thrift store in Cooklyn.
    """

    m "At least it was sustainable!"

    $ unlocks_dialogue = ["It's deserved. How else will I learn?"]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
        m "I know I need to be better, but still..."

    scene menmi-apartment-morning with dissolve:
        matrixcolor BrightnessMatrix (value=-0.7)
    m """
    ...

    I just want to be good enough.
    """

    $ unlocks_dialogue = ["What if things don't go as planned?", "I can't go back now, though."]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    m "Why can't reality just *be* the way I want it to be?"
    m "*Sigh* Is it always going to be this way?"

label choice_16:
    menu:
        m "How do I cope?"

        "Ride the feels":
            $ unlocks_dialogue = ["I keep second-guessing myself and thinking about other possibilities...", "Sometimes I feel insecure", "I can't go back now, though", "I wish I could redo some decisions", "Trick question, still me.", "I don't think I'm being dramatic when I say Disaster will befall me."]
            $ dialogue_matches = []
            $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
            if len(dialogue_matches) > 0:
                show screen insight(dialogue_matches)
            c "There's no use running away from your feelings."
            m """
            Nobody would ever fall in love with someone as worthless as me.

            It's a little sick but...{w}a part of me revels in blaming it all on myself. {w}At least that would mean I'm in control.

            How could it be an accident, after all? A stroke of bad luck? Senselessness like that is way too cruel.
            """
        "Distract yourself":
            stop music fadeout 3.0
            c "This train of thought is making you miserable. Let's do something else."
            m "Maybe listening to some music will help."
            scene menmi-apartment-morning with dissolve:
                matrixcolor BrightnessMatrix (value=-0.4)
            play music "<from 43>/audio/lonely-souls.mp3"
            m """
            Ah, the members of Double Black Velvet Jeans are so pretty.

            *Sigh* Why couldn’t I have been born poreless too?
            """
            $ unlocks_dialogue = ["It's nice to know that I'm capable of achieving happiness for myself.", "I need to move on.", "I think I just have to learn to accept that I don't know everything, but..."]
            $ dialogue_matches = []
            $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
            if len(dialogue_matches) > 0:
                show screen insight(dialogue_matches)
            m """
            I'm still in a funk, but I do feel a little lighter.

            My mouth tastes like mud. I should hydrate. Where'd I put that Stanlychee bottle...?
            """
            $ renpy.notify("+5 Self-Awareness")
            $ self_awareness += 5

        "Practice Positivity" if self_awareness>=70:
            $ unlocks_dialogue = ["I'm going to have faith and enjoy the ride", "What if they do?", "They may have shaped my past, but the future isn't set in stone."]
            $ dialogue_matches = []
            $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
            if len(dialogue_matches) > 0:
                show screen insight(dialogue_matches)
            c "Give it time. You've only just begun."

            $ unlocks_dialogue = ["There are times when I admit I can be hard on myself", "It can be tough, but the only productive choice I have is to stay positive, believe in myself, and trust that everything will work out!", "I choose to believe in myself!"]
            $ dialogue_matches = []
            $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
            if len(dialogue_matches) > 0:
                show screen insight(dialogue_matches)
            m """
            I'm feeling really low right now, but need to choose to think positively. What other productive choice is there?

            It's hard to think of myself as a great catch. {w} I can't do a full 180 on my feelings, but maybe I can accept that an opportunity for love just hasn't happened yet.

            I need to stay positive. It doesn't do me any good to wallow in self-defeat.
            """
            $ renpy.notify("+10 Self-Awareness")
            $ self_awareness += 10

label after_choice_16:
    m "I just wish something would *happen* for once."

    scene menmi-apartment-afternoon with vpunch
    play sound "/audio/cell-vibrate.mp3"
    stop music fadeout 3.0
    m """
    Huh?{w} Is someone calling me?

    I glance at the screen to see who’s crashing my pity party."""

    play music "/audio/najis-theme.mp3" volume 0.7 fadein 5.0

    m "!!!{w} Naji?"

    $ unlocks_dialogue = [" I miss how close we used to be", "He seems to be doing well...", "There were times I wondered if we could be more than friends...", "Why is Naji's opinion of me such a big deal?"]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    m "He *has* been on my mind lately..."
    stop sound
    m "“Hello?”"
    n "“Hey, Men. {w}You busy?”"

    scene menmi-apartment-door with dissolve
    m "In the corner of the room, I watch an ant crawl over a crumb...{w}only to realize that it's dust. {w}The ant is also dust."
    m "“Yes.”"
    n "“...{w}That sounded like a lie”"

    $ unlocks_dialogue = ["He was my best friend", "I have a lot of good memories with Naji", "We're super comfortable with each other", "He’s a good listener"]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    m "Tch. He knows me too well."
    n "“Have you been to Onion Circle?”"
    m "“The park by my place? Yeah, I take the train from there every day.”"
    n "“Right, of course. Sorry, I'm mansplaning...”"
    m "He sounds nervous."

    $ unlocks_dialogue = ["He's always had a way with people. Got the rizz, as they say", "He's changed."]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
        m "That's not like him."

    m """
    “No. Sorry, Naji. I didn’t mean it that way.”

    “I'm hungover.”
    """

    if naji_relationship<=20:
        m "And feeling like crap about myself, {w}but I don’t burden him with that."

    elif naji_relationship>20:
        $ unlocks_dialogue = ["He was my best friend", "He’s a good listener", "We're super comfortable with each other"]
        $ dialogue_matches = []
        $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
        if len(dialogue_matches) > 0:
            show screen insight(dialogue_matches)
        m "“It's been kind of rough lately.”"
        n "“I'm sorry to hear that, Men. I wish I could cheer you up!”"

    n "“If you’re feeling up to it by then, how about hitting up the Onion Circle Greenmarket tomorrow?”"

    $ unlocks_dialogue = ["He used to follow me around and do whatever I wanted", "We're the same age, but I kind of saw him as a little brother"]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    m "Am I hearing this right? Naji...asking *me* to hang out? Usually, *I'm* the one who makes the plans."

    $ unlocks_dialogue = ["There were times I wondered if we could be more than friends..."]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
        m """Maybe I'm just sensitive right now, but this kind of sounds like

        No...{w}it can't be.
        """
    $ unlocks_dialogue = ["I'm going to have faith and enjoy the ride", "Why not, though?"]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    m """
    Then again, is it so strange? We *are* friends after all.

    “Sure! It sounds like fun.”
    """

    n "“...!!! Awesome. I’ll see you tomorrow, then.”"
    m "“Bet.”"

    if naji_relationship>=40:
        n """
        “Hey, Men?”

        “I'm really looking forward to seeing you.”
        """

        m "“You see me all the time, weirdo,”"

        play sound "/audio/heartbeat-fast.mp3"

        m """
        ...is what comes out of my mouth, but my heart is throttling up through my throat.

        Naji just laughs before hanging up.
        """

    stop music fadeout 2.0
    play sound "/audio/heartbeat-fast.mp3" volume 2.0

    scene menmi-apartment-morning with dissolve
    m "When the urge to scream into the couch cushions overcomes me, I do not fight it."

    scene menmi-apartment-morning with hpunch
    m "{cps=*0.5}EEEEEEEEEEEEE{/cps}{w}!!!!! {w}????"
    scene menmi-apartment-morning with hpunch
    scene menmi-apartment-morning with hpunch

    $ unlocks_dialogue = ["He was my best friend", "We're the same age, but I kind of saw him as a little brother"]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    m """
    Why is my heart beating so fast?

    It's *just* Naji...
    """

    $ unlocks_dialogue = ["Do I feel like it's justified?", " Where did I get that idea from?", "Something about this feels familiar..."]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    c "Unzip that subconscious 'cause we're going to unpack these feels."

    play music "/audio/siberian-express.mp3" volume 0.5
    scene menmi-apartment-morning with dissolve:
        matrixcolor BrightnessMatrix (value=-0.4)
        matrixcolor SepiaMatrix (tint='#ffeec2', desat=(0.2126, 0.7152, 0.0722))

    $ unlocks_dialogue = ["Naji and I grew up across the street from each other", "We're super comfortable with each other", "He was my best friend", "I have a lot of good memories with Naji."]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    m """
    We go way back. Naji and I grew up together.

    His mom used to drop him off at our place all the time. {w}She was always pawning him off somewhere so she could spend time with some new guy.
    """

    $ unlocks_dialogue = ["That's probably why he's so reticent. Even if he spoke up, his feelings always came second to hers", "I was protective of him", " I have to keep that in mind, no matter what happens going forward."]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    m "I'm grateful I got to spend so much time with him, but I always felt sorry for how quickly he had to learn to survive on his own."

    $ unlocks_dialogue = ["He's always had a way with people. Got the rizz, as they say", "Naji prioritizes the needs of others before his own"]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    m """
    Not that his presence was ever a burden, though.

    My parents *loved* him.

    Naji made sure of that.
    """

    if self_awareness>=80:
        $ unlocks_dialogue = ["My family..."]
        $ dialogue_matches = []
        $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
        if len(dialogue_matches) > 0:
            show screen insight(dialogue_matches)
        m "For whatever reason, my parents' approval of him endeared him to me too."

    scene lounge-inside with dissolve
    m "Meeting him again at the William Collins..."

    scene lounge-inside with dissolve:
        matrixcolor SepiaMatrix (tint='#ffeec2', desat=(0.2126, 0.7152, 0.0722))
    show naji-bar-neutral at truecenter with flash:
        matrixcolor SepiaMatrix (tint='#ffeec2', desat=(0.2126, 0.7152, 0.0722))

    "Customer" "“The new guy’s charming, isn’t he? Easy on the eyes, too.”"
    "Waitress" "“We all love him here!”"


    hide naji-bar-neutral with dissolve
    show naji-bar-neutral with dissolve


    $ unlocks_dialogue = ["He's changed", "It makes me jealous to think that there are others who are closer to him now", "It makes me feel insecure that I don't know everything about him", "By the time we were in high school, I could see how he would be considered attractive...physically", " I thought I knew him better"]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    m "I'm starting to see him differently."

    scene menmi-apartment-afternoon with fade:
        matrixcolor SepiaMatrix (tint='#ffeec2', desat=(0.2126, 0.7152, 0.0722))

    $ unlocks_dialogue = ["I think I just have to learn to accept that I don't know everything, but..."," I'm going to have faith and enjoy the ride; I believe in myself", "What if they do?", "Things might not work out, but that's a natural part of life."]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    if self_awareness>=50:
        m """
        Our relationship is changing, and it's kind of scary...

        Things might get worse between us.

        But what if they don't?
        """

        $ unlocks_dialogue = ["I hope he doesn't think I'm silly for wanting to be in love", "Why is Naji's opinion of me such a big deal?"]
        $ dialogue_matches = []
        $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
        if len(dialogue_matches) > 0:
            show screen insight(dialogue_matches)
            m "Forgive me for this, Naji..."


        $ unlocks_dialogue = ["There were times I wondered if we could be more than friends..."]
        $ dialogue_matches = []
        $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
        if len(dialogue_matches) > 0:
            show screen insight(dialogue_matches)
        m "Could I be cautiously optimistic? {w} Tentatively, yes."

    elif self_awareness<50:
        $ unlocks_dialogue = ["There were times I wondered if we could be more than friends...", "I always worried that he was out of my league, though"]
        $ dialogue_matches = []
        $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
        if len(dialogue_matches) > 0:
            show screen insight(dialogue_matches)
        m "I’ve been toying with the possibility in the back of mind, but I’ve been too afraid to seriously entertain it until now."

        $ unlocks_dialogue = ["It's romantic to fall for the best friend who's been with you all along. Who knows me better than him?"]
        $ dialogue_matches = []
        $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
        if len(dialogue_matches) > 0:
            show screen insight(dialogue_matches)
        m "There’s an irreplicable intimacy shared between childhood friends."

        $ unlocks_dialogue = ["It's romantic to fall for the best friend who's been with you all along. Who knows me better than him?"]
        $ dialogue_matches = []
        $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
        if len(dialogue_matches) > 0:
            show screen insight(dialogue_matches)
        m "As the years go by and maturity teaches our eyes to see by the light of desire, {w}the innocent bud of camaraderie we planted in childhood blooms into something more...{w}sophisticated."

        $ unlocks_dialogue = ["I always worried that he was out of my league, though"]
        $ dialogue_matches = []
        $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
        if len(dialogue_matches) > 0:
            show screen insight(dialogue_matches)
        m """
        But I can't let myself get carried away.

        I mean, an *objectively* hot guy...interested in *me*?

        Impossible.

        And yet... here we are.
        """

    stop music
    play music "<from 48>/audio/reaching-the-sky.mp3"
    scene menmi-apartment-afternoon with flash
    m """
    Pain bursts through my head as the 2pm sun hits my eyes.

    I’ve got to do something about this hangover...

    Despite the pain in my head, my limbs lightly lift me off the couch.
    """


    scene city-morning with fade:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}End of Act 1{/size}{/font}{/color}{color=#000000}{color=#000000}{font=JustAnotherHand-Regular.ttf}{size=150}\n Self-Awareness Score: [self_awareness]{/size}{/font}{/color}" at truecenter with wiperight
    pause
