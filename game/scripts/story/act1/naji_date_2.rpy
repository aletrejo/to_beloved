label naji_date_2:
    play sound "/audio/pencil-write.mp3"
    scene city-morning with fade:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}Week [week]{/size}{/font}{/color}{color=#000000}{color=#000000}{font=JustAnotherHand-Regular.ttf}{size=200}\n Weekend!{/size}{/font}{/color}" at truecenter with wiperight
    pause

    play music "<from 9>/audio/happily-ever-after.mp3" fadein 0.5
    scene lounge-outside with dissolve
    m """
    Today, Naji and I decided to meet up after his shift to grab *brunch*. Just like on Seed and the City!

    It's been a while since I've seen Naji outside the lounge.

    As much as I like the William Collins, I'm looking forward to hanging out some place where the drinks aren't strong enough to make you forget about how much you paid for them.

    I'm waiting for Naji in front of the lounge when a squeaky "Mee!" pipes in from my periphery.
    """

    scene alleyway with wipeleft
    stop music fadeout 3.0

    m "I look in and go *weak* in the knees. (Note to Self: Ask Joule about strengthening knees)"

    m "I see Naji crouched over, hands cupping the top of a tiny head."

    play music "/audio/najis-theme.mp3"
    show naji-neutral with dissolve
    play sound "/audio/kitty_mew.mp3"

    m """
    The cat is eating kibble out of what I recognize as one of the peanut bowls from the lounge.

    “Who's this little darling?” """

    hide naji-neutral
    show naji-surprised

    $ unlocks_dialogue = ["We're super comfortable with each other", "I have a lot of good memories with Naji."]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    m "Naji looks up, startled, but the tension in his shoulders uncoils once he sees me."

    hide naji-surprised
    show naji-smile

    n "“Menmi, you are in the presence of one of our most esteemed patrons.”"
    m """
    His grin is wide, like a proud father's.

    I gasp. “And here I've been caught without my clutching pearls!”"""

    hide naji-smile
    show naji-laugh

    m """
    Naji's laughter sounds comfortingly intimate cocooned within the alleyway.

    “Does she have a name?”
    """

    hide naji-laugh
    show naji-lookaway

    m "Naji runs a hand through his hair and drops his gaze to the ground, suddenly sheepish."
    n "“Yeah, actually...ee...”"
    m "“Pardon?”"

    $ unlocks_dialogue = ["It makes me feel insecure that I don't know everything about him", "I thought I knew him better", "I hope he can be open with me someday...", "He's hiding something"]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    m """
    Why's he being shy all of a sudden? He practically whispered that last part.

    Naji clears his throat.
    """
    n "“Mimi...it's Mimi.”"

    hide naji-lookaway
    show naji-blush

    n "{cps=*2}“Any resemblances to any people real or fictional are purely coincidental.”{/cps}"
    i "Thanks for the disclaimer...not sus in the slightest."

    $ unlocks_dialogue = ["I always worried that he was out of my league, though", "Why is Naji's opinion of me such a big deal?", "Sometimes I feel insecure.", "I'll learn from my mistakes"]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    m "It's not like Naji named the cat after *me* or anything..."
    play sound "/audio/kitty_mew.mp3"
    "Mimi" "“Mee! Mee!”"
    m "“Haha she just said her name. Like a Pokébowlmon!”"

    stop music
    play sound "/audio/impact-slam.mp3"
    scene alleyway with vpunch:
        matrixcolor InvertMatrix(value=1.0)
    m "So why are my cheeks burning?"


    $ unlocks_dialogue = ["Maybe I shouldn't have talked about my love life...Compared to him, I must look like a loser", "I hope he doesn't think I'm silly for wanting to be in love", "I always worried that he was out of my league, though"]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    i "Naji? Like *you*? Cool dumb thought, Menmi."

    if self_awareness>=60:
        $ renpy.notify("Self-Awareness Check: Passed")
        $ unlocks_dialogue = ["There were times I wondered if we could be more than friends...","I have a lot of good memories with Naji", "It's romantic to fall for the best friend who's been with you all along. Who knows me better than him?", "I choose to believe in myself!"]
        $ dialogue_matches = []
        $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
        if len(dialogue_matches) > 0:
            show screen insight(dialogue_matches)
        m "I mean, he *did* get all defensive about it. I can be cautiously optimistic."
    elif self_awareness<60:
        m """
        Gosh, I must be delulu to believe a miracle like that could be trululu.

        Either way, I need to be present and focus on the moment in front of me."""

    scene alleyway with vpunch
    play music "/audio/najis-theme.mp3"
    show naji-neutral

    $ unlocks_dialogue = ["I'm going to have faith and enjoy the ride", "I have to keep that in mind, no matter what happens going forward."]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    m """

    The cat, having finished her meal, purrs happily as she squeezes her round form around his legs.

    “Oh my gosh, Naji. Is she–”
    """

    n "“Yeah, pregnant. I think she's due soon.”"

    hide naji-neutral
    show naji-frown
    $ unlocks_dialogue = ["Naji prioritizes the needs of others before his own", "He's a good guy."]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    n """
    "It's been tricky to care for her with work being so hectic, but it's not like I can leave her alone..."

    "Poor thing. She's probably looking for a safe space to give birth.”
    """

    m "“But if you're doing this much already, why not just take her in? Or call a shelter?”"

    hide naji-frown
    show naji-lookaway

    $ unlocks_dialogue = ["Naji's mom dropped him off at our house a lot, so we spent a lot of time together."]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    n """
    “I've thought about it, but I'm really not home often enough to care for a cat...cats.”

    “And with the city shelters as packed as they are, who knows what'll happen to a pregnant cat?”
    """

    hide naji-lookaway
    show naji-neutral

    $ unlocks_dialogue = ["Naji's dad left when he was a baby, and his mom didn't make time for him. He had to go through a lot on his own"]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    n "“She's her own cat, you know? She's free. She made it this far on her own without anyone's help.”"

    $ unlocks_dialogue = ["Naji's mom was always with a new guy who didn't last. That's probably why he never seemed interested in romance."]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    n "“Who am I to take away her freedom just so I can feel reassured about her safety?”"

    $ unlocks_dialogue = ["He's not the type to share his feelings", "Naji would always listen to me vent about my feelings, but he never seemed as open with his own", "He's hiding something"]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    m """
    Naji's getting so passionate about this.

    I can't read the subtext from this distance. We might have to get personal.
    """

label choice_14:
    menu:
        "Agree":
            c "He wants to be reassured that he's doing the right thing. As his friend, you should validate his feelings."
            $ unlocks_dialogue = ["That's probably why he's so reticent. Even if he spoke up, his feelings always came second to hers", "He's not the type to share his feelings", "Naji's grown with time. I'm curious about what else about him has changed..."]
            $ dialogue_matches = []
            $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
            if len(dialogue_matches) > 0:
                show screen insight(dialogue_matches)
                m "It must be difficult for him to share how he really feels."

            $ unlocks_dialogue = ["I was protective of him", "I think I just have to learn to accept that I don't know everything, but..."]
            $ dialogue_matches = []
            $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
            if len(dialogue_matches) > 0:
                show screen insight(dialogue_matches)
            m """
            “Yeah, I see where you're coming from.”

            Naji nods silently, long fingers brushing behind Mimi's ear for a scratch.
            """
        "Challenge him":
            $ unlocks_dialogue = ["I hope he can be open with me someday..."]
            $ dialogue_matches = []
            $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
            if len(dialogue_matches) > 0:
                show screen insight(dialogue_matches)
            c """
            It's unlikely that he'll offer more information on his own.

            Offering a different perspective could help him give the issue more thought.
            """
            m "“How can you be sure that she's made it this far on her own? Friendly strays usually have had experiences with humans.”"

            hide naji-neutral
            show naji-lookaway

            n """
            ...

            “Yeah, you've got a point.”
            """
            $ renpy.notify("+5 Self-Awareness")
            $ self_awareness += 5

            $ unlocks_dialogue = ["His past...", "His feelings..., Maybe it was his way of coping", "Naji's dad left when he was a baby, and his mom didn't make time for him.  He had to go through a lot on his own."]
            $ dialogue_matches = []
            $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
            if len(dialogue_matches) > 0:
                show screen insight(dialogue_matches)
            n """
            “I don't know, but...”

            “I guess I might have been seeing myself in her situation.”
            """
        "Ask him to clarify":
            c "Just ask him. You might be able to support him if he feels like sharing."
            m """
            “What do you mean by that?”

            Naji pauses, brows scrunched.

            The sizzle in his eyes have dissipated, and he seems to be considering his next words carefully.

            """

            $ unlocks_dialogue = ["He's not the type to share his feelings", "Naji would always listen to me vent about my feelings, but he never seemed as open with his own", "That's probably why he's so reticent. Even if he spoke up, his feelings always came second to hers."]
            $ dialogue_matches = []
            $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
            if len(dialogue_matches) > 0:
                show screen insight(dialogue_matches)
            n "“I don't want to talk about this anymore. All I'll say is...”"

        "There's something deeper at play..." if self_awareness>=70:
                $ unlocks_dialogue = ["Where did I get that idea from?", "Naji prioritizes the needs of others before his own", "Maybe it was his way of coping, My family", "His past..."]
                $ dialogue_matches = []
                $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
                if len(dialogue_matches) > 0:
                    show screen insight(dialogue_matches)
                c "There's a way to make sense of this."
                scene alleyway with dissolve:
                    blur 50
                show naji-lookaway at truecenter:
                    blur 50
                m """
                I reach into the past, recalling the details of Naji's upbringing.

                Naji's single mother was often absent, and whenever she was around, it seemed like she always had something for Naji to do.

                I'd remember times when we'd play "laundry" while she nursed a hangover in her bedroom.
                """

                scene alleyway
                show naji-lookaway

                $ unlocks_dialogue = ["Naji's mom dropped him off at our house a lot, so we spent a lot of time together", "That's probably why he's so reticent. Even if he spoke up, his feelings always came second to hers", "I wonder if he keeps in touch with her."]
                $ dialogue_matches = []
                $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
                if len(dialogue_matches) > 0:
                    show screen insight(dialogue_matches)
                m """
                “Naji, do you think this might have to do with your mom?"

                He frowns, brow furrowing up as he stares at the space between Mimi's ears.
                """
                if self_awareness <=70:
                    scene alleyway with vpunch:
                        matrixcolor InvertMatrix(value=1.0)
                    stop music
                    play sound "/audio/impact-slam.mp3"
                    $ unlocks_dialogue = ["Where did I get that idea from?", "They may have shaped my past, but the future isn't set in stone.", "I need to move on."]
                    $ dialogue_matches = []
                    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
                    if len(dialogue_matches) > 0:
                        show screen insight(dialogue_matches)
                    m """Did I say something wrong?"

                    I should've just taken him at face value. Feelings aren't meant to be examined!
                    """
                    scene alleyway
                    play music "<from 14>/audio/najis-theme.mp3"

                hide naji-lookaway
                show naji-frown
                n """
                ...

                “...I guess I never really thought of it that way, but you might have a point.”

                *Sigh*
                """
                if naji_relationship >=20:
                    hide naji-frown
                    show naji-blush
                    n "“I'm amazed by how well you know me.”"
                    hide naji-blush
                    show naji-frown

                $ renpy.notify("+5 Self-Awareness")
                $ self_awareness += 5

                $ unlocks_dialogue = ["Naji's dad left when he was a baby, and his mom didn't make time for him. He had to go through a lot on his own", "He had to go through a lot on his own.", "Naji's mom was always with a new guy who didn't last. That's probably why he never seemed interested in romance"]
                $ dialogue_matches = []
                $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
                if len(dialogue_matches) > 0:
                    show screen insight(dialogue_matches)
                n """
                “I really admire Mimi's independence.”

                Mom was always relying on me or worse, whichever guy she was trying to impress that day.”
                """


label after_choice_14:
    $ unlocks_dialogue = ["Naji's dad left when he was a baby, and his mom didn't make time for him. He had to go through a lot on his own", "Maybe it was his way of coping", "Naji's mom was always with a new guy who didn't last. That's probably why he never seemed interested in romance."]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    show naji-smile
    n "“I don't want to interfere with her autonomy. If you love something, let it go, you know?”"

    hide naji-smile
    show naji-frown

    m "“I can see where you're coming from.”"

    $ unlocks_dialogue = ["Everyone has to believe in something, and I choose to believe in love!"]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    m """"But for me, if I love something, I'd want to keep it with me forever.”

    Naji glances at me, a dark look crossing his face.
    """
    stop music
    play sound "/audio/impact-slam.mp3"
    scene alleyway with vpunch:
        matrixcolor InvertMatrix(value=1.0)
    show naji-frown at truecenter:
        matrixcolor InvertMatrix(value=1.0)
    i "Clearly, he disagrees."

    if self_awareness >=60:
        $ renpy.notify("Self-Awareness Check: Passed")
        $ unlocks_dialogue = ["There are times when I admit I can be hard on myself.", "I choose to believe in myself!", "Everyone has to believe in something, and I choose to believe in love!"]
        $ dialogue_matches = []
        $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
        if len(dialogue_matches) > 0:
            show screen insight(dialogue_matches)
        c "It's OK to disagree. You're different people, after all."
        m "Yeah, and I'm not trying to convince him of my views, either. Still..."
    elif self_awareness <60:
        $ unlocks_dialogue = ["I keep second-guessing myself and thinking about other possibilities...I can't go back now, though.", "Why's Naji's opinion of me such a big deal?", "Maybe I shouldn't have talked about my love life..."]
        $ dialogue_matches = []
        $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
        if len(dialogue_matches) > 0:
            show screen insight(dialogue_matches)
        m "I've upset him."
        i "Nice going, scatterbrains!"

    scene alleyway with vpunch
    play music "<from 15>/audio/najis-theme.mp3"
    show naji-frown

    $ unlocks_dialogue = ["I need to be a better person.", "I must have said something to make him uncomfortable", "I hope he doesn't think I'm silly for wanting to be in love", "I was protective of him"]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    m """
    The vibes are off. I need to fix them.

    “It's admirable that you empathize with Mimi so much, Naj. She clearly adores you.”
    """

    hide naji-frown
    show naji-neutral
    n "“Yeah...thanks. I'll do everything I can to help her out without interfering with her life.”"

    $ unlocks_dialogue = ["Naji prioritizes the needs of others before his own", "That's probably why he's so reticent. Even if he spoke up, his feelings always came second to hers.", "I hope he can be open with me someday..."]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    m "Phew! He took the olive branch."

    $ unlocks_dialogue = ["He's not the type to share his feelings", "It's deserved. How else will I learn?", "Trick question, still me.", "They taught me well."]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
        m "That was uncomfy for both of us!"

    m "“I'll have to remember to save my sardines from pizza for Mimi!”"

    hide naji-neutral
    show naji-laugh

    n "“Haha, since when did you eat pizza with sardines?”"
    m """
    “Since I met Mimi!”

    “It's called girl dinner. You wouldn't get it.”
    """

    $ unlocks_dialogue = ["He was my best friend", "We're super comfortable with each other"]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
    m "Naji laughs, tension disappearing like frost in the sun."
    n """
    “Speaking of eating, should we get going?”

    “I'm so hungry I could eat a bush!”
    """
    m "“Ha...I was hoping you'd forgotten that...”"

    hide naji-laugh with dissolve
    m """
    As we head out, I take one last look at Mimi in the alley. Would she be there next time? With kittens? Or a new person? Or maybe...

    Who can say for sure what the future holds?
    """

    $ n2=True

    $ unlocks_dialogue = ["I think I just have to learn to accept that I don't know everything, but...", "I'm going to have faith and enjoy the ride", "They may have shaped my past, but the future isn't set in stone"]
    $ dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)

    $ renpy.notify("Naji feels closer to you!")
    $ naji_relationship += 10
    m "Nothing to do but trust."


    jump after_naji_date
