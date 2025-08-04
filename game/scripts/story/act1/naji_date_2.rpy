label naji_date_2:
    play sound "/audio/pencil-write.mp3"
    hide screen open_planner
    hide screen open_insights
    scene city-morning with fade:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}Week [week]{/size}{/font}{/color}{color=#000000}{color=#000000}{font=JustAnotherHand-Regular.ttf}{size=200}\n Weekend!{/size}{/font}{/color}" at truecenter with wiperight
    pause

    play music "<from 9>/audio/happily-ever-after.mp3" fadein 0.5
    scene lounge-outside with dissolve
    show screen open_planner
    show screen open_insights
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
    show cat at truecenter with easeinbottom

    m """
    The cat is eating kibble out of what I recognize as one of the peanut bowls from the lounge.

    “Who's this little darling?” """

    hide naji-neutral
    show naji-surprised at hop
    hide cat

    m "Naji looks up, startled, but the tension in his shoulders uncoils once he sees me."

    hide naji-surprised
    show naji-smile

    n "“Menmi, you are in the presence of one of our most esteemed patrons.”"
    m """
    (His grin is wide, like a proud father's.)

    I gasp. “And here I've been caught without my clutching pearls!”"""

    hide naji-smile
    show naji-laugh at laughter

    m """
    (Naji's laughter sounds comfortingly intimate within the alleyway.)

    “Does she have a name?”
    """

    hide naji-laugh
    show naji-lookaway

    m "Naji runs a hand through his hair and drops his gaze to the ground, suddenly sheepish."
    n "“Yeah, actually...ee...”"
    m "“Pardon?”"

    m """
    (Why's he being shy all of a sudden? He practically whispered that last part.)

    Naji clears his throat.
    """
    n "“Mimi...it's Mimi.”"

    hide naji-lookaway
    show naji-blush at squirm

    n "{cps=*2}“Any resemblances to any people real or fictional are purely coincidental.”{/cps}"
    show cat at truecenter with easeinbottom
    play sound "/audio/kitty_mew.mp3"
    "Mimi" "“Mee! Mee!”"
    m "“Haha she just said her name. Like a Pokébowlmon!”"
    m "(Although his disclaimer was definitely odd.)"

    stop music
    play sound "/audio/impact-slam.mp3"
    scene alleyway with vpunch:
        matrixcolor InvertMatrix(value=1.0)
    show naji-blush at truecenter:
        matrixcolor InvertMatrix(value=1.0)

    m "(But It's not like Naji named the cat after *me* or anything...)"
    m "(So why are my cheeks burning?)"

    i "Naji? Like *you*? Cool dumb thought, Menmi."

    if self_awareness>=60:
        play sound "/audio/awareness-ding.mp3"
        show text "{image=ol_text}" with easeinbottom
        pause
        hide text with dissolve

        m "(I mean, he *did* get all defensive about it. I can be cautiously optimistic.)"
        $ chosen_sticker = "mimi"
        image sticker_won = "stickers/sticker-mimi.png"
        show sticker_won at rotation:
            xpos 0.5
            ypos 0.5
        show text "{image=stickertext}" with dissolve:
            xpos 0.5
            ypos 0.5
        pause
        hide sticker_won
        hide text
        show screen place_sticker(chosen_sticker)
        pause
        hide screen place_sticker
        $ passed_checks +=1
        scene alleyway with vpunch

    elif self_awareness<60:
        m """
        (Gosh, I must be delulu to believe a miracle like that could be trululu.)

        (Either way, I need to be present and focus on the moment in front of me.)"""

    scene alleyway with vpunch
    play music "/audio/najis-theme.mp3"
    show naji-neutral
    show cat at truecenter with easeinbottom

    m """

    The cat, having finished her meal, purrs happily as she squeezes her round form around his legs.

    “Oh my gosh, Naji. Is she–”
    """

    n "“Yeah, pregnant. I think she's due soon.”"

    hide naji-neutral
    hide cat
    show naji-frown

    n """
    "It's been tricky to care for her with work being so hectic, but it's not like I can leave her alone..."

    "Poor thing. She's probably looking for a safe space to give birth.”
    """

    m "“But if you're doing this much already, why not just take her in? Or call a shelter?”"

    hide naji-frown
    show naji-lookaway

    n """
    “I've thought about it, but I'm really not home often enough to care for a cat...cats.”

    “And with the city shelters as packed as they are, who knows what'll happen to a pregnant cat?”
    """

    hide naji-lookaway
    show naji-neutral


    n "“She's her own cat, you know? She's free. She made it this far on her own without anyone's help.”"


    n "“Who am I to take away her freedom just so I can feel reassured about her safety?”"


    m """
    (Naji's getting so passionate about this.)

    (I can't read the subtext from this distance. We might have to get personal.)
    """

label choice_14:
    menu:
        "Agree":
            c "He wants to be reassured that he's doing the right thing. As his friend, you should validate his feelings."
            m "(It must be difficult for him to share how he really feels.)"
            m """
            “Yeah, I see where you're coming from.”

            Naji nods silently, long fingers brushing behind Mimi's ear for a scratch.
            """
        "Challenge him":
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
            show screen selfawareup 
            window hide
            play sound "/audio/awareness-ding.mp3"
            pause
            hide screen selfawareup 
            $ self_awareness += 5

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

            n "“I don't want to talk about this anymore. All I'll say is...”"

        "There's something deeper at play..." if self_awareness>=70:
                c "There's a way to make sense of this."
                scene alleyway with dissolve:
                    blur 50
                show naji-lookaway at truecenter:
                    blur 50
                m """
                (I reach into the past, recalling the details of Naji's upbringing.)

                (Naji's single mother was often absent, and whenever she was around, it seemed like she always had something for Naji to do.)

                (I'd remember times when we'd play "laundry" while she nursed a hangover in her bedroom.)
                """

                scene alleyway
                show naji-lookaway

                m """
                “Naji, do you think this might have to do with your mom?"

                He frowns, brow furrowing up as he stares at the space between Mimi's ears.
                """
                if self_awareness <=70:
                    scene alleyway with vpunch:
                        matrixcolor InvertMatrix(value=1.0)
                    stop music
                    play sound "/audio/impact-slam.mp3"

                    m """Did I say something wrong?"

                    (I should've just taken him at face value. Feelings aren't meant to be examined!)
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

                show screen selfawareup 
                window hide
                play sound "/audio/awareness-ding.mp3"
                pause
                hide screen selfawareup 
                $ self_awareness += 5

                n """
                “I really admire Mimi's independence.”

                Mom was always relying on me or worse, whichever guy she was trying to impress that day.”
                """


label after_choice_14:
    show naji-smile
    n "“I don't want to interfere with her autonomy. If you love something, let it go, you know?”"

    hide naji-smile
    show naji-frown

    m "“That makes sense.”"

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
        play sound "/audio/awareness-ding.mp3"
        show text "{image=ol_text}" with easeinbottom
        pause
        hide text with dissolve
        c "It's OK to disagree. You're different people, after all."
        m "(Yeah, and I'm not trying to convince him of my views, either. Still...)"
        $ chosen_sticker = renpy.random.choice(available_stickers)
        image sticker_won = "stickers/sticker-[chosen_sticker].png"
        show sticker_won at rotation:
            xpos 0.5
            ypos 0.5
        show text "{image=stickertext}" with dissolve:
            xpos 0.5
            ypos 0.5
        pause
        hide sticker_won
        hide text
        show screen place_sticker(chosen_sticker)
        $ available_stickers.remove(chosen_sticker)
        pause
        hide screen place_sticker
        $ passed_checks +=1

    elif self_awareness <60:
        m "(I've upset him.)"
        i "Nice going, scatterbrains!"

    scene alleyway with vpunch
    play music "<from 15>/audio/najis-theme.mp3"
    show naji-frown

    m """
    (The vibes are off. I need to fix them.)

    “It's admirable that you empathize with Mimi so much, Naj. She clearly adores you.”
    """

    hide naji-frown
    show naji-neutral
    n "“Yeah...thanks. I'll do everything I can to help her out without interfering with her life.”"

    m "(Phew! He took the olive branch.)"

    m "(That was uncomfy for both of us!)"

    m "“I'll have to remember to save my sardines from pizza for Mimi!”"

    hide naji-neutral
    show naji-laugh at laughter

    n "“Haha, since when did you eat pizza with sardines?”"
    m """
    “Since I met Mimi!”

    “It's called girl dinner. You wouldn't get it.”
    """

    m "Naji laughs, tension disappearing like a cat in the night."
    n """
    “Speaking of eating, should we get going?”

    “I'm so hungry I could eat a bush!”
    """
    m "“Ha...I was hoping you'd forgotten that...”"

    hide naji-laugh with dissolve
    m """
    (As we head out, I take one last look at Mimi in the alley. Would she be there next time? With kittens? Or a new person? Or maybe...)

    (Who can say for sure what the future holds?)
    """

    $ n2=True


    $ renpy.notify("Naji feels closer to you!")
    $ naji_relationship += 10
    m "Nothing to do but trust."


    jump after_naji_date
