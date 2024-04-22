label weekend_1:
    play sound "/audio/pencil-write.mp3"
    hide screen open_planner
    scene city-morning with dissolve:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}Week 1{/size}{/font}{/color}{color=#000000}{font=JustAnotherHand-Regular.ttf}{size=200}\n Weekend!{/size}{/font}{/color}" at truecenter with wiperight
    pause

    scene menmi-apartment-morning with dissolve
    show screen open_planner
    m """
    Mmmmmm... Ah, did I sleep in? It's so late!

    Aaaah I was so tired that I forgot to set an alarm.
    """
    stop music
    play music "<from 13>/audio/cave-streams.mp3"
    play sound "/audio/impact-slam.mp3"
    scene menmi-apartment-morning with vpunch:
        matrixcolor InvertMatrix(value=1.0)
    i "You're going to build bad habits if you let yourself lay about."

    scene menmi-apartment-morning
    stop music
    play music "<from 13>/audio/happily-ever-after.mp3"

    m "I shouldn't be sleeping in when I have so much I need to do! But then again, I didn't have much planned for the weekend."

label choice_11:
    menu:
        m "How do I feel about this?"

        "Let the guilt sink in":
            c "Don't let this happen again. You're young and worse yet -- *single*. You just lost half the day to sleep. Who knows how many men you could have been macking on with that time?"
            m """
            Ugh, there goes that weekend cafe meet-cute.

            I can't believe I let myself laze about today.  Lesson learned for the future!
            """
        "Take it easy":
            $ renpy.notify("+10 Self-Awareness")
            $ self_awareness += 10
            c "You gave it your all this week. You're allowed to relax. Not every second of your life has to be dedicated to productivity. Listen to your body. Listen to *me*."
            m "It isn't good for me to constantly put pressure on myself to do things. There has to be balance. I have to remind myself of that."

label bathtime_tutorial:
    scene planner-weekend1 with dissolve
    m "What a wild week. I'm glad I decided to take some time off today to take a bath and have some *me* time."
    scene menmi-apartment-morning with dissolve
    m "After all, I deliberately chose an apartment with a tub. It'd be a waste if I didn't at least try it out."
    m """
    Hehe. I'm somewhat of a bath buff. I've got all the fixings (well, maybe I shouldn't say “fixings”; it makes it sound like I'm cooking up a pot of Menmi soup)

    Let's just say I'm {i}well equipped{/i}.
    """
    stop music fadeout 2.0

    menu:
        m "Now, what kind of bath am I in the mood for today?"

        "Classic":
            scene bathtime-classic with fade
            m "There's nothing like a simple bath to clear your head and refocus on your body."
        "Romantic":
            scene bathtime-romantic with fade
            m "The heady perfumes of lavender and cedar essential oils are so indulgent! Baths always make me feel like I'm being buoyed up into a higher plane of awareness..."
        "Fruity":
            scene bathtime-fruity with fade
            m "The sweet and fresh scents of citrus fill me with playful bliss! I feel like I'm in a fresh jug of lemonade. Aahhh, baths are so refreshing."
    window hide

    play music "/audio/bathtime-theme.mp3"

    show tutorial-box-bathtime
    screen bathtime():
        vbox:
            xalign 0.5
            yalign 0.6
            xmaximum 1000
            box_wrap True
            text """
            Bathtime is Men-ME time! By making time to take a bath, Menmi performs self-care, replenishing her mental and physical energy.

            The bath is the perfect place to ponder and process the events of Menmi's week. You'll be able to guide the flow of Menmi's reflections.

            The more insight she gains into her life, the more {b}Self-Awareness{/b} you'll earn.
            """
    show screen bathtime with dissolve
    pause
    hide screen bathtime
    hide tutorial-box-bathtime
    jump bathtime_1

label week_2_4_bathtime:
    play sound "/audio/pencil-write.mp3"
    scene city-morning with dissolve:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}Week [week]{/size}{/font}{/color}{color=#000000}{color=#000000}{font=JustAnotherHand-Regular.ttf}{size=200}\n Weekend!{/size}{/font}{/color}" at truecenter with wiperight
    pause

    scene menmi-apartment-morning
    show screen open_insights
    show screen open_planner
    play music "<from 13>/audio/happily-ever-after.mp3" fadein 1.0
    m """
    Ah, the weekend's here! Which means it's time for me to soak in life one memory at a time.

    I still have a lot to reflect on. Alright, time to marinate in my brothy thoughts and get some *winsight* into the situation.

    """
    stop music fadeout 1.0
    play music "/audio/bathtime-theme.mp3"
    menu:
        m "Now, what kind of bath am I in the mood for today?"

        "Classic":
            scene bathtime-classic with fade
            m "There's nothing like a simple bath to clear your head and refocus on your body."
        "Romantic":
            scene bathtime-romantic with fade
            m "The heady perfumes of lavender and cedar essential oils are so indulgent! Baths always make me feel like I'm being buoyed up into a higher plane of awareness..."
        "Fruity":
            scene bathtime-fruity with fade
            m "The sweet and fresh scents of citrus fill me with playful bliss! I feel like I'm in a fresh jug of lemonade. Aahhh, baths are so refreshing."
    jump bathtime_1

label bathtime_1:
    show bubblesm with dissolve
    show bubblesl with dissolve
    show bubbless with dissolve
    default bathtime_1_choices = []
    # Work around to clear list
    #while bathtime_1_choices:
        #$ bathtime_1_choices.pop()
    m "It's been an eventful week. Out of everything's that's happened though, there's one thing I can't get off my mind."
    menu:
        m "What do I want to reflect on?"

        "Naji":
            $ bathtime_1_choices.append("Naji")
            jump naji_bathtime_1
        "Myself" if self_awareness > 30:
            $ bathtime_1_choices.append("Myself")
            jump myself_bathtime_1

label naji_bathtime_1:
    menu we_were_close:
        with Dissolve(2.0)
        "I miss how close we used to be...":
            $ bathtime_1_choices.append("I miss how close we used to be...")
            menu:
                with Dissolve(2.0)
                "We were neighbors":
                    $ bathtime_1_choices.append("We were neighbors")
                    menu:
                        with Dissolve(2.0)
                        "Naji and I grew up across the street from each other":
                            $ bathtime_1_choices.append("Naji and I grew up across the street from each other")
                            menu across_the_street:
                                with Dissolve(2.0)
                                "Naji's mom dropped him off at our house a lot, so we spent a lot of time together.":
                                    $ bathtime_1_choices.append("Naji's mom dropped him off at our house a lot, so we spent a lot of time together.")
                                    menu dropped_off:
                                        with Dissolve(2.0)
                                        "Naji's dad left when he was a baby, and his mom didn't make time for him. He had to go through a lot on his own.":
                                            $ bathtime_1_choices.append("Naji's dad left when he was a baby, and his mom didn't make time for him. He had to go through a lot on his own.")
                                            menu on_his_own:
                                                with Dissolve(2.0)
                                                "That's probably why he's so reticent. Even if he spoke up, his feelings always came second to hers.":
                                                    $ bathtime_1_choices.append("That's probably why he's so reticent. Even if he spoke up, his feelings always came second to hers.")
                                                    menu second_to_hers:
                                                        with Dissolve(2.0)
                                                        "I wonder if he keeps in touch with her.":
                                                            $ bathtime_1_choices.append("I wonder if he keeps in touch with her.")
                                                            $ renpy.notify("+20 Self-Awareness")
                                                            $ self_awareness += 20
                                                            jump naji_bathtime_1_best_result
                                                "Naji's mom was always with a new guy who didn't last. That's probably why he never seemed interested in romance.":
                                                    $ bathtime_1_choices.append("Naji's mom was always with a new guy who didn't last. That's probably why he never seemed interested in romance.")
                                                    menu new_guy:
                                                        with Dissolve(2.0)
                                                        "I wonder if he keeps in touch with her.":
                                                            $ bathtime_1_choices.append("I wonder if he keeps in touch with her.")
                                                            $ renpy.notify("+20 Self-Awareness")
                                                            $ self_awareness += 20
                                                            jump naji_bathtime_1_best_result
                                                        "I was protective of him":
                                                            $ bathtime_1_choices.append("I was protective of him")
                                                            menu protective:
                                                                with Dissolve(2.0)
                                                                "Naji would always listen to me vent about my feelings, but he never seemed as open with his own":
                                                                    $ bathtime_1_choices.append("Naji would always listen to me vent about my feelings, but he never seemed as open with his own")
                                                                    menu vent:
                                                                        with Dissolve(2.0)
                                                                        "Bartending suits him":
                                                                            $ bathtime_1_choices.append("Bartending suits him")
                                                                            $ renpy.notify("+15 Self-Awareness")
                                                                            $ self_awareness += 15
                                                                            jump naji_bathtime_1_good_result
                                                                        "I hope he can be open with me someday...":
                                                                            $ bathtime_1_choices.append("I hope he can be open with me someday...")
                                                                            $ renpy.notify("+15 Self-Awareness")
                                                                            $ self_awareness += 15
                                                                            jump naji_bathtime_1_good_result
                                                                        "He's not the type to share his feelings":
                                                                            $ bathtime_1_choices.append("He's not the type to share his feelings")
                                                                            jump share_his_feelings
                                                                        "Naji prioritizes the needs of others before his own":
                                                                            $ bathtime_1_choices.append("Naji prioritizes the needs of others before his own")
                                                                            menu prioritize_others:
                                                                                with Dissolve(2.0)
                                                                                "Bartending suits him":
                                                                                    $ bathtime_1_choices.append("Bartending suits him")
                                                                                    $ renpy.notify("+15 Self-Awareness")
                                                                                    $ self_awareness += 15
                                                                                    jump naji_bathtime_1_good_result
                                                                                "He's a good guy.":
                                                                                    $ bathtime_1_choices.append("He's a good guy.")
                                                                                    menu good_guy:
                                                                                        with Dissolve(2.0)
                                                                                        "There were times I wondered if we could be more than friends...":
                                                                                            $ bathtime_1_choices.append("There were times I wondered if we could be more than friends...")
                                                                                            jump more_than_friends
                                                                                        "I have a lot of good memories with Naji.":
                                                                                            $ bathtime_1_choices.append("I have a lot of good memories with Naji.")
                                                                                            jump good_memories
                                                                                        "I have to keep that in mind, no matter what happens going forward.":
                                                                                            $ bathtime_1_choices.append("I have to keep that in mind, no matter what happens going forward.")
                                                                                            $ renpy.notify("+15 Self-Awareness")
                                                                                            $ self_awareness += 15
                                                                                            jump naji_bathtime_1_good_result
                                                                                "He's a good listener":
                                                                                    $ bathtime_1_choices.append("He's a good listener")
                                                                                    jump good_listener
                                                                                "He used to follow me around and do whatever I wanted":
                                                                                    $ bathtime_1_choices.append("He used to follow me around and do whatever I wanted")
                                                                                    jump follow_me
                                                                                "Maybe it was his way of coping":
                                                                                    $ bathtime_1_choices.append("Maybe it was his way of coping")
                                                                                    menu coping:
                                                                                        with Dissolve(2.0)
                                                                                        "Naji's dad left when he was a baby, and his mom didn't make time for him. He had to go through a lot on his own.":
                                                                                            $ bathtime_1_choices.append("Naji's dad left when he was a baby, and his mom didn't make time for him. He had to go through a lot on his own.")
                                                                                            jump on_his_own
                                                                "We're the same age, but I kind of saw him as a little brother":
                                                                    $ bathtime_1_choices.append("We're the same age, but I kind of saw him as a little brother")
                                                                    jump little_brother
                                                        "By the time we were in high school, I could see how he would be considered attractive...physically":
                                                            $ bathtime_1_choices.append("By the time we were in high school, I could see how he would be considered attractive...physically")
                                                            menu attractive_in_hs:
                                                                with Dissolve(2.0)
                                                                "I always worried that he was out of my league, though":
                                                                    $ bathtime_1_choices.append("I always worried that he was out of my league, though")
                                                                    $ renpy.notify("+10 Self-Awareness")
                                                                    $ self_awareness += 10
                                                                    jump naji_bathtime_1_mid_result
                                                "I have to keep that in mind, no matter what happens going forward.":
                                                    $ bathtime_1_choices.append("I have to keep that in mind, no matter what happens going forward.")
                                                    $ renpy.notify("+15 Self-Awareness")
                                                    $ self_awareness += 15
                                                    jump naji_bathtime_1_good_result
                                        "We used to mix bath bubbles in the inflatable pool and pretend we were at a spa":
                                            $ bathtime_1_choices.append("We used to mix bath bubbles in the inflatable pool and pretend we were at a spa")
                                            menu bubbles:
                                                with Dissolve(2.0)
                                                "He used to follow me around and do whatever I wanted":
                                                    $ bathtime_1_choices.append("He used to follow me around and do whatever I wanted")
                                                    menu follow_me:
                                                        with Dissolve(2.0)
                                                        "I was protective of him":
                                                            $ bathtime_1_choices.append("I was protective of him")
                                                            jump protective
                                                        "Naji would always listen to me vent about my feelings, but he never seemed as open with his own":
                                                            $ bathtime_1_choices.append("Naji would always listen to me vent about my feelings, but he never seemed as open with his own")
                                                            jump vent
                                                        "He's changed.":
                                                            $ bathtime_1_choices.append("He's changed")
                                                            jump naji_changed
                                                "We're the same age, but I kind of saw him as a little brother":
                                                    $ bathtime_1_choices.append("We're the same age, but I kind of saw him as a little brother")
                                                    jump little_brother
                                                "We're super comfortable with each other":
                                                    $ bathtime_1_choices.append("We're super comfortable with each other")
                                                    jump comfortable
                                                "I have a lot of good memories with Naji.":
                                                    $ bathtime_1_choices.append("I have a lot of good memories with Naji.")
                                                    menu good_memories:
                                                        with Dissolve(2.0)
                                                        "He's changed.":
                                                            $ bathtime_1_choices.append("He's changed.")
                                                            jump naji_changed
                                                        "I have to keep that in mind, no matter what happens going forward.":
                                                            $ bathtime_1_choices.append("I have to keep that in mind, no matter what happens going forward.")
                                                            $ renpy.notify("+15 Self-Awareness")
                                                            $ self_awareness += 15
                                                            jump naji_bathtime_1_good_result
                                "We're the same age, but I kind of saw him as a little brother":
                                    $ bathtime_1_choices.append("We're the same age, but I kind of saw him as a little brother")
                                    menu little_brother:
                                        with Dissolve(2.0)
                                        "He used to follow me around and do whatever I wanted":
                                            $ bathtime_1_choices.append("He used to follow me around and do whatever I wanted")
                                            jump follow_me
                                        "By the time we were in high school, I could see how he would be considered attractive...physically":
                                            $ bathtime_1_choices.append("By the time we were in high school, I could see how he would be considered attractive...physically")
                                            jump attractive_in_hs
                                "We're super comfortable with each other":
                                        $ bathtime_1_choices.append("We're super comfortable with each other")
                                        menu comfortable:
                                            with Dissolve(2.0)
                                            "We're the same age, but I kind of saw him as a little brother":
                                                $ bathtime_1_choices.append("We're the same age, but I kind of saw him as a little brother")
                                                jump little_brother
                                            "He's a good listener":
                                                $ bathtime_1_choices.append("He's a good listener")
                                                menu good_listener:
                                                    with Dissolve(2.0)
                                                    "Naji's dad left when he was a baby, and his mom didn't make time for him. He had to go through a lot on his own.":
                                                        $ bathtime_1_choices.append("Naji's dad left when he was a baby, and his mom didn't make time for him. He had to go through a lot on his own.")
                                                        jump on_his_own
                                                    "Naji would always listen to me vent about my feelings, but he never seemed as open with his own":
                                                        $ bathtime_1_choices.append("Naji would always listen to me vent about my feelings, but he never seemed as open with his own")
                                                        jump vent
                                                    "Bartending suits him":
                                                        $ bathtime_1_choices.append("Bartending suits him")
                                                        $ renpy.notify("+15 Self-Awareness")
                                                        $ self_awareness += 15
                                                        jump naji_bathtime_1_good_result
                                            "It makes me jealous to think that there are others who are closer to him now":
                                                $ bathtime_1_choices.append("It makes me jealous to think that there are others who are closer to him now")
                                                menu closer_to_him:
                                                    with Dissolve(2.0)
                                                    "I hope he can be open with me someday...":
                                                        $ bathtime_1_choices.append("I hope he can be open with me someday...")
                                                        $ renpy.notify("+15 Self-Awareness")
                                                        $ self_awareness += 15
                                                        jump naji_bathtime_1_good_result
                                                    "I don't know...or maybe I'm not ready to face it yet. I need more insight on this.":
                                                        $ bathtime_1_choices.append("I don't know...or maybe I'm not ready to face it yet. I need more insight on this.")
                                                        $ renpy.notify("+20 Self-Awareness")
                                                        $ self_awareness += 20
                                                        jump naji_bathtime_1_best_result
                        "We were pretty close through high school, but lost touch after graduation.":
                            $ bathtime_1_choices.append("We were pretty close through high school, but lost touch after graduation.")
                            menu close_in_hs:
                                with Dissolve(2.0)
                                "He's changed":
                                    $ bathtime_1_choices.append("He's changed")
                                    menu naji_changed:
                                        with Dissolve(2.0)
                                        "I thought I knew him better.":
                                            $ bathtime_1_choices.append("I thought I knew him better.")
                                            menu knew_him_better:
                                                with Dissolve(2.0)
                                                "It makes me jealous to think that there are others who are closer to him now":
                                                    $ bathtime_1_choices.append("It makes me jealous to think that there are others who are closer to him now")
                                                    jump closer_to_him
                                                "It makes me feel insecure that I don't know everything about him":
                                                    $ bathtime_1_choices.append("It makes me feel insecure that I don't know everything about him")
                                                    $ renpy.notify("+20 Self-Awareness")
                                                    $ self_awareness += 20
                                                    jump naji_bathtime_1_best_result
                                        "It makes me uncomfortable":
                                            $ bathtime_1_choices.append("It makes me uncomfortable")
                                            jump uncomfortable
                                "Naji's mom dropped him off at our house a lot, so we spent a lot of time together.":
                                    $ bathtime_1_choices.append("Naji's mom dropped him off at our house a lot, so we spent a lot of time together.")
                                    jump dropped_off
                                "There were times I wondered if we could be more than friends...":
                                        $ bathtime_1_choices.append("There were times I wondered if we could be more than friends...")
                                        menu more_than_friends:
                                            with Dissolve(2.0)
                                            "By the time we were in high school, I could see how he would be considered attractive...physically":
                                                $ bathtime_1_choices.append("By the time we were in high school, I could see how he would be considered attractive...physically")
                                                jump attractive_in_hs
                                            "It's romantic to fall for the best friend who's been with you all along. Who knows me better than him?":
                                                $ bathtime_1_choices.append("It's romantic to fall for the best friend who's been with you all along. Who knows me better than him?")
                                                menu fall_for_bf:
                                                    with Dissolve(2.0)
                                                    "I always worried that he was out of my league, though":
                                                        $ bathtime_1_choices.append("I always worried that he was out of my league, though")
                                                        $ renpy.notify("+10 Self-Awareness")
                                                        $ self_awareness += 10
                                                        jump naji_bathtime_1_mid_result
                                                    "Everyone has to believe in something, and I choose to believe in love!":
                                                        $ bathtime_1_choices.append("Everyone has to believe in something, and I choose to believe in love!")
                                                        $ renpy.notify("+10 Self-Awareness")
                                                        $ self_awareness += 10
                                                        jump naji_bathtime_1_mid_result
                                                    "I thought I knew him better.":
                                                        $ bathtime_1_choices.append("I thought I knew him better.")
                                                        jump knew_him_better
                "He was my best friend":
                    $ bathtime_1_choices.append("He was my best friend")
                    menu best_friend:
                        with Dissolve(2.0)
                        "We used to mix bath bubbles in the inflatable pool and pretend we were at a spa":
                            $ bathtime_1_choices.append("We used to mix bath bubbles in the inflatable pool and pretend we were at a spa")
                            menu:
                                "I have a lot of good memories with Naji.":
                                    $ bathtime_1_choices.append("I have a lot of good memories with Naji.")
                                    $ renpy.notify("+15 Self-Awareness")
                                    $ self_awareness += 15
                                    jump naji_bathtime_1_good_result
                        "We were pretty close through high school, but lost touch after graduation.":
                            $ bathtime_1_choices.append("We were pretty close through high school, but lost touch after graduation.")
                            jump close_in_hs
                        "There were times I wondered if we could be more than friends...":
                            $ bathtime_1_choices.append("There were times I wondered if we could be more than friends...")
                            jump more_than_friends
                "He's changed.":
                    $ bathtime_1_choices.append("He's changed.")
                    jump naji_changed
        "He seems to be doing well...":
            $ bathtime_1_choices.append("He seems to be doing well...")
            menu doing_well:
                with Dissolve(2.0)
                "I'm happy for him":
                    $ bathtime_1_choices.append("I'm happy for him")
                    menu happy_for_him:
                        with Dissolve(2.0)
                        "I didn't know he was so popular...":
                            $ bathtime_1_choices.append("I didn't know he was so popular...")
                            menu popular:
                                with Dissolve(2.0)
                                "It makes sense.":
                                    $ bathtime_1_choices.append("It makes sense.")
                                    menu:
                                        with Dissolve(2.0)
                                        "He's always had a way with people. Got the rizz, as they say.":
                                            $ bathtime_1_choices.append("He's always had a way with people. Got the rizz, as they say.")
                                            jump rizz
                                        "He's a good listener":
                                            $ bathtime_1_choices.append("He's a good listener")
                                            jump good_listener
                                        "By the time we were in high school, I could see how he would be considered attractive...physically":
                                            $ bathtime_1_choices.append("By the time we were in high school, I could see how he would be considered attractive...physically")
                                            jump attractive_in_hs
                                        "It makes me uncomfortable":
                                            $ bathtime_1_choices.append("It makes me uncomfortable")
                                            menu uncomfortable:
                                                with Dissolve(2.0)
                                                "I thought I knew him better.":
                                                    $ bathtime_1_choices.append("I thought I knew him better.")
                                                    jump knew_him_better
                                                "I can't help but feel a bit jealous":
                                                    $ bathtime_1_choices.append("I can't help but feel a bit jealous")
                                                    jump bit_jealous
                                                "I hope he can be open with me someday...":
                                                    $ bathtime_1_choices.append("I hope he can be open with me someday...")
                                                    $ renpy.notify("+15 Self-Awareness")
                                                    $ self_awareness += 15
                                                    jump naji_bathtime_1_good_result
                                                "It makes me jealous to think that there are others who are closer to him now":
                                                    $ bathtime_1_choices.append("It makes me jealous to think that there are others who are closer to him now")
                                                    jump closer_to_him
                                "I miss how close we used to be…":
                                    $ bathtime_1_choices.append("I miss how close we used to be…")
                                    jump we_were_close
                                "Compared to him, I must look like a loser.":
                                    $ bathtime_1_choices.append("Compared to him, I must look like a loser.")
                                    jump loser
                                "I can't help but feel a bit jealous":
                                    $ bathtime_1_choices.append("I can't help but feel a bit jealous")
                                    jump bit_jealous
                                "He's changed":
                                    $ bathtime_1_choices.append("He's changed")
                                    jump naji_changed
                        "I have to keep that in mind, no matter what happens going forward.":
                            $ bathtime_1_choices.append("I have to keep that in mind, no matter what happens going forward.")
                            $ renpy.notify("+15 Self-Awareness")
                            $ self_awareness += 15
                            jump naji_bathtime_1_good_result
                        "He's always had a way with people. Got the rizz, as they say.":
                            $ bathtime_1_choices.append("He's always had a way with people. Got the rizz, as they say.")
                            menu rizz:
                                with Dissolve(2.0)
                                "Naji prioritizes the needs of others before his own":
                                    $ bathtime_1_choices.append("Naji prioritizes the needs of others before his own")
                                    jump prioritize_others
                                "Bartending suits him":
                                    $ bathtime_1_choices.append("Bartending suits him")
                                    $ renpy.notify("+15 Self-Awareness")
                                    $ self_awareness += 15
                                    jump naji_bathtime_1_good_result
                                "Maybe it was his way of coping":
                                    $ bathtime_1_choices.append("Maybe it was his way of coping")
                                    jump coping
                "I can't help but feel a bit jealous":
                    $ bathtime_1_choices.append("I can't help but feel a bit jealous")
                    menu bit_jealous:
                        with Dissolve(2.0)
                        "He was my best friend":
                            $ bathtime_1_choices.append("He was my best friend")
                            jump best_friend
                        "He's always had a way with people. Got the rizz, as they say.":
                            $ bathtime_1_choices.append("He's always had a way with people. Got the rizz, as they say.")
                            jump rizz
                        "Compared to him, I must look like a loser.":
                            $ bathtime_1_choices.append("Compared to him, I must look like a loser.")
                            menu loser:
                                with Dissolve(2.0)
                                "I hope he doesn't think I'm silly for wanting to be in love":
                                    $ bathtime_1_choices.append("I hope he doesn't think I'm silly for wanting to be in love")
                                    menu love_is_silly:
                                        with Dissolve(2.0)
                                        "Why is Naji's opinion of me such a big deal?":
                                            $ bathtime_1_choices.append("Why is Naji's opinion of me such a big deal?")
                                            menu najis_opinion:
                                                with Dissolve(2.0)
                                                "I don't know...or maybe I'm not ready to face it yet. I need more insight on this.":
                                                    $ bathtime_1_choices.append("I don't know...or maybe I'm not ready to face it yet. I need more insight on this.")
                                                    $ renpy.notify("+20 Self-Awareness")
                                                    $ self_awareness += 20
                                                    jump naji_bathtime_1_best_result
                                                "He's not the type to share his feelings":
                                                    $ bathtime_1_choices.append("He's not the type to share his feelings")
                                                    jump share_his_feelings
                                        "Everyone has to believe in something, and I choose to believe in love!":
                                            $ bathtime_1_choices.append("Everyone has to believe in something, and I choose to believe in love!")
                                            $ renpy.notify("+10 Self-Awareness")
                                            $ self_awareness += 10
                                            jump naji_bathtime_1_mid_result
                                        "It's romantic to fall for the best friend who's been with you all along. Who knows me better than him?":
                                            $ bathtime_1_choices.append("It's romantic to fall for the best friend who's been with you all along. Who knows me better than him?")
                                            jump fall_for_bf
                                "I always worried that he was out of my league.":
                                    $ bathtime_1_choices.append("I always worried that he was out of my league.")
                                    $ renpy.notify("+10 Self-Awareness")
                                    $ self_awareness += 10
                                    jump naji_bathtime_1_mid_result
                                "He's always had a way with people. Got the rizz, as they say.":
                                    $ bathtime_1_choices.append("He's always had a way with people. Got the rizz, as they say.")
                                    jump rizz
                                "Maybe I shouldn't have talked about my love life...":
                                    $ bathtime_1_choices.append("Maybe I shouldn't have talked about my love life...")
                                    menu love_life:
                                        with Dissolve(2.0)
                                        "Why not, though?":
                                            $ bathtime_1_choices.append("Why not, though?")
                                            menu:
                                                with Dissolve(2.0)
                                                "It was inappropriate":
                                                    $ bathtime_1_choices.append("It was inappropriate")
                                                    menu inappropriate:
                                                        with Dissolve(2.0)
                                                        "Maybe I was coming on too strong for our first time seeing each other in so long, but it's not like we're total strangers.":
                                                            $ bathtime_1_choices.append("Maybe I was coming on too strong for our first time seeing each other in so long, but it's not like we're total strangers.")
                                                            menu coming_on_too_strong:
                                                                with Dissolve(2.0)
                                                                "Naji would always listen to me vent about my feelings, but he never seemed as open with his own":
                                                                    $ bathtime_1_choices.append("Naji would always listen to me vent about my feelings, but he never seemed as open with his own")
                                                                    jump vent
                                                                "Naji and I grew up across the street from each other":
                                                                    $ bathtime_1_choices.append("Naji and I grew up across the street from each other")
                                                                    jump across_the_street
                                                                "I have a lot of good memories with Naji.":
                                                                    $ bathtime_1_choices.append("I have a lot of good memories with Naji.")
                                                                    jump good_memories
                                                        "Naji's mom was always with a new guy who didn't last. That's probably why he never seemed interested in romance.":
                                                            $ bathtime_1_choices.append("Naji's mom was always with a new guy who didn't last. That's probably why he never seemed interested in romance.")
                                                            jump new_guy
                                                "I don't know...or maybe I'm not ready to face it yet. I need more insight on this.":
                                                    $ bathtime_1_choices.append("I don't know...or maybe I'm not ready to face it yet. I need more insight on this.")
                                                    $ renpy.notify("+20 Self-Awareness")
                                                    $ self_awareness += 20
                                                    jump naji_bathtime_1_best_result
                                                "We're super comfortable with each other":
                                                    $ bathtime_1_choices.append("We're super comfortable with each other")
                                                    jump comfortable
                                        "There were times I wondered if we could be more than friends...":
                                            $ bathtime_1_choices.append("There were times I wondered if we could be more than friends...")
                                            jump more_than_friends
                                        "Naji's not the type to share his feelings":
                                            $ bathtime_1_choices.append("Naji's not the type to share his feelings")
                                            jump share_his_feelings
                "We were pretty close through high school, but lost touch after graduation.":
                    $ bathtime_1_choices.append("We were pretty close through high school, but lost touch after graduation.")
                    jump close_in_hs
        "Why did he seem reluctant to talk about love?":
            $ bathtime_1_choices.append("Why did he seem reluctant to talk about love?")
            menu reluctant:
                with Dissolve(2.0)
                "I must have said something to make him uncomfortable":
                    $ bathtime_1_choices.append("I must have said something to make him uncomfortable")
                    menu made_him_uncomfortable:
                        with Dissolve(2.0)
                        "I hope he doesn't think I'm silly for wanting to be in love":
                            $ bathtime_1_choices.append("I hope he doesn't think I'm silly for wanting to be in love")
                            jump love_is_silly
                        "Maybe I shouldn't have talked about my love life...":
                            $ bathtime_1_choices.append("Maybe I shouldn't have talked about my love life...")
                            jump love_life
                        "He's not the type to share his feelings":
                            $ bathtime_1_choices.append("He's not the type to share his feelings")
                            menu share_his_feelings:
                                with Dissolve(2.0)
                                "Naji prioritizes the needs of others before his own":
                                    $ bathtime_1_choices.append("Naji prioritizes the needs of others before his own")
                                    jump prioritize_others
                                "Maybe it was his way of coping":
                                    $ bathtime_1_choices.append("Maybe it was his way of coping")
                                    jump coping
                                "I hope he can be open with me someday...":
                                    $ bathtime_1_choices.append("I hope he can be open with me someday...")
                                    $ renpy.notify("+15 Self-Awareness")
                                    $ self_awareness += 15
                                    jump naji_bathtime_1_good_result
                "He's hiding something":
                    $ bathtime_1_choices.append("He's hiding something")
                    menu hiding_something:
                        with Dissolve(2.0)
                        "His past...":
                            $ bathtime_1_choices.append("His past...")
                            menu:
                                "Naji's mom was always with a new guy who didn't last. That's probably why he never seemed interested in romance.":
                                    $ bathtime_1_choices.append("Naji's mom was always with a new guy who didn't last. That's probably why he never seemed interested in romance.")
                                    jump new_guy
                        "His feelings...":
                            $ bathtime_1_choices.append("His feelings...")
                            menu najis_feelings:
                                with Dissolve(2.0)
                                "I hope he doesn't think I'm silly for wanting to be in love":
                                    $ bathtime_1_choices.append("I hope he doesn't think I'm silly for wanting to be in love")
                                    jump love_is_silly
                                "Naji prioritizes the needs of others before his own":
                                    $ bathtime_1_choices.append("Naji prioritizes the needs of others before his own")
                                    jump prioritize_others
                                "He's not the type to share his feelings":
                                    $ bathtime_1_choices.append("He's not the type to share his feelings")
                                    jump share_his_feelings
                        "Naji would always listen to me vent about my feelings, but he never seemed as open with his own":
                            $ bathtime_1_choices.append("Naji would always listen to me vent about my feelings, but he never seemed as open with his own")
                            jump vent

label naji_bathtime_1_mid_result:
    menu:
        with Dissolve(2.0)
        "I probably wouldn't have a chance, but there is something romantic about falling in love with your best friend...":
            call after_bathtime_1 from _call_after_bathtime_1
            scene menmi-apartment-afternoon with dissolve
            m "I'm still working through my thoughts and feelings, but I've gotten some clarity. It's nice to slow down every now and then."
            jump menmi_after_bath
label naji_bathtime_1_good_result:
    menu:
        with Dissolve(2.0)
        "Naji's grown with time. I'm curious about what else about him has changed...":
            call after_bathtime_1 from _call_after_bathtime_1_1
            scene menmi-apartment-afternoon with dissolve
            m "Things are starting to feel a little clearer. I'm glad I took the time to reflect."
            jump menmi_after_bath
label naji_bathtime_1_best_result:
    menu:
        with Dissolve(2.0)
        "Why do I feel so self-conscious around Naji now that he's different from how I remember? Maybe if I talk to him more, I can sort out my feelings.":
            call after_bathtime_1 from _call_after_bathtime_1_2
            scene menmi-apartment-afternoon with dissolve
            m "What a rejuvenating bath! I feel completely cleansed and ready to take on whatever's ahead."
            jump menmi_after_bath

label myself_bathtime_1:
    menu how_i_feel:
        with Dissolve(2.0)
        "How I feel...":
            $ bathtime_1_choices.append("How I feel...")
            menu:
                with Dissolve(2.0)
                "I'm excited...":
                    $ bathtime_1_choices.append("I'm excited...")
                    menu excited:
                        with Dissolve(2.0)
                        "Meeting new people, experiencing new things, chasing down a whirlwind romance...":
                            $ bathtime_1_choices.append("Meeting new people, experiencing new things, chasing down a whirlwind romance...")
                            menu whirlwind_romance:
                                with Dissolve(2.0)
                                "It's all coming true like I planned":
                                    $ bathtime_1_choices.append("It's all coming true like I planned")
                                    menu like_I_planned:
                                        with Dissolve(2.0)
                                        "It's nice to know that I'm capable of achieving happiness for myself.":
                                            $ bathtime_1_choices.append("It's nice to know that I'm capable of achieving happiness for myself.")
                                            menu achieve_happiness:
                                                with Dissolve(2.0)
                                                "I choose to believe in myself!":
                                                    $ bathtime_1_choices.append("I choose to believe in myself!")
                                                    $ renpy.notify("+20 Self-Awareness")
                                                    $ self_awareness += 20
                                                    jump me_bathtime_1_positive_result
                                                "I'll learn from my mistakes":
                                                    $ bathtime_1_choices.append("I'll learn from my mistakes")
                                                    jump my_mistakes
                                        "What if things don't go as planned?":
                                            $ bathtime_1_choices.append("What if things don't go as planned?")
                                            jump not_as_planned
                                "It's nice to know that I'm capable of achieving happiness for myself.":
                                    $ bathtime_1_choices.append("It's nice to know that I'm capable of achieving happiness for myself.")
                                    jump achieve_happiness
                                "Things might not work out, but that's a natural part of life.":
                                    $ bathtime_1_choices.append("Things might not work out, but that's a natural part of life.")
                                    jump part_of_life
                                "There are times when I admit I can be hard on myself.":
                                    $ bathtime_1_choices.append("There are times when I admit I can be hard on myself.")
                                    jump hard_on_myself
                        "It's nice to know that I'm capable of achieving happiness for myself.":
                            $ bathtime_1_choices.append("It's nice to know that I'm capable of achieving happiness for myself.")
                            jump achieve_happiness
                "I'm uncertain...":
                    $ bathtime_1_choices.append("I'm uncertain...")
                    menu:
                        with Dissolve(2.0)
                        "I keep second-guessing myself and thinking about other possibilities...":
                            $ bathtime_1_choices.append("I keep second-guessing myself and thinking about other possibilities...")
                            menu second_guessing:
                                with Dissolve(2.0)
                                "Do I feel like it's justified?":
                                    $ bathtime_1_choices.append("Do I feel like it's justified?")
                                    jump justified
                                "I wish I could redo some decisions":
                                    $ bathtime_1_choices.append("I wish I could redo some decisions")
                                    menu redo:
                                        with Dissolve(2.0)
                                        "I'll get more chances. Nothing's unfixable.":
                                            $ bathtime_1_choices.append("I'll get more chances. Nothing's unfixable.")
                                            $ renpy.notify("+20 Self-Awareness")
                                            $ self_awareness += 20
                                            jump me_bathtime_1_change_result
                                        "I don't think I'm being dramatic when I say Disaster will befall me.":
                                            $ bathtime_1_choices.append("I don't think I'm being dramatic when I say Disaster will befall me.")
                                            jump disaster_befalls
                                        "I think I just have to learn to accept that I don't know everything, but...":
                                            $ bathtime_1_choices.append("I think I just have to learn to accept that I don't know everything, but...")
                                            jump dont_know_everything
                                "I can't go back now, though.":
                                    $ bathtime_1_choices.append("I can't go back now, though.")
                                    menu cant_go_back:
                                        with Dissolve(2.0)
                                        "I need to move on.":
                                            $ bathtime_1_choices.append("I need to move on.")
                                            $ renpy.notify("+20 Self-Awareness")
                                            $ self_awareness += 20
                                            jump me_bathtime_1_practical_result
                                        "I'll get more chances. Nothing's unfixable.":
                                            $ bathtime_1_choices.append("I'll get more chances. Nothing's unfixable.")
                                            $ renpy.notify("+20 Self-Awareness")
                                            $ self_awareness += 20
                                            jump me_bathtime_1_change_result
                                        "I think I just have to learn to accept that I don't know everything, but...":
                                            $ bathtime_1_choices.append("I think I just have to learn to accept that I don't know everything, but...")
                                            jump dont_know_everything
                                        "I'll learn from my mistakes":
                                            $ bathtime_1_choices.append("I'll learn from my mistakes")
                                            jump my_mistakes
                                "I don't think I'm being dramatic when I say Disaster will befall me.":
                                    $ bathtime_1_choices.append("I don't think I'm being dramatic when I say Disaster will befall me.")
                                    jump disaster_befalls
                        "What if things don't go as planned?":
                            $ bathtime_1_choices.append("What if things don't go as planned?")
                            menu not_as_planned:
                                with Dissolve(2.0)
                                "Things might not work out, but that's a natural part of life.":
                                    $ bathtime_1_choices.append("Things might not work out, but that's a natural part of life.")
                                    menu part_of_life:
                                        with Dissolve(2.0)
                                        "I think I just have to learn to accept that I don't know everything, but...":
                                            $ bathtime_1_choices.append("I think I just have to learn to accept that I don't know everything, but...")
                                            jump dont_know_everything
                                "I don't think I'm being dramatic when I say Disaster will befall me.":
                                    $ bathtime_1_choices.append("I don't think I'm being dramatic when I say Disaster will befall me.")
                                    menu disaster_befalls:
                                        with Dissolve(2.0)
                                        "Something about this feels familiar...":
                                            $ bathtime_1_choices.append("Something about this feels familiar...")
                                            menu feels_familiar:
                                                with Dissolve(2.0)
                                                "Where did I get that idea from?":
                                                    $ bathtime_1_choices.append("Where did I get that idea from?")
                                                    menu that_idea:
                                                        with Dissolve(2.0)
                                                        "My family":
                                                            $ bathtime_1_choices.append("My family")
                                                            menu family_tree:
                                                                with Dissolve(2.0)
                                                                "They taught me well.":
                                                                    $ bathtime_1_choices.append("They taught me well.")
                                                                    $ renpy.notify("+20 Self-Awareness")
                                                                    $ self_awareness += 20
                                                                    jump me_bathtime_1_practical_result
                                                                "I need to move on.":
                                                                    $ bathtime_1_choices.append("I need to move on.")
                                                                    $ renpy.notify("+20 Self-Awareness")
                                                                    $ self_awareness += 20
                                                                    jump me_bathtime_1_positive_result
                                                                "They may have shaped my past, but the future isn't set in stone.":
                                                                    $ bathtime_1_choices.append("They may have shaped my past, but the future isn't set in stone.")
                                                                    $ renpy.notify("+20 Self-Awareness")
                                                                    $ self_awareness += 20
                                                                    jump me_bathtime_1_change_result
                                                        "My exes":
                                                            $ bathtime_1_choices.append("My exes")
                                                            jump family_tree
                                                        "Trick question, still me.":
                                                            $ bathtime_1_choices.append("Trick question, still me.")
                                                            menu still_me:
                                                                with Dissolve(2.0)
                                                                "I need to be a better person.":
                                                                    $ bathtime_1_choices.append("I need to be a better person.")
                                                                    jump better_person
                                                                "Sometimes I feel insecure.":
                                                                    $ bathtime_1_choices.append("Sometimes I feel insecure.")
                                                                    menu insecure:
                                                                        with Dissolve(2.0)
                                                                        "I keep second-guessing myself and thinking about other possibilities...":
                                                                            $ bathtime_1_choices.append("I keep second-guessing myself and thinking about other possibilities...")
                                                                            jump second_guessing
                                                                        "I have to be better about that.":
                                                                            $ bathtime_1_choices.append("I have to be better about that.")
                                                                            menu better_about_that:
                                                                                with Dissolve(2.0)
                                                                                "I'll learn from my mistakes":
                                                                                    $ bathtime_1_choices.append("I'll learn from my mistakes")
                                                                                    menu my_mistakes:
                                                                                        with Dissolve(2.0)
                                                                                        "They may have shaped my past, but the future isn't set in stone.":
                                                                                            $ bathtime_1_choices.append("They may have shaped my past, but the future isn't set in stone.")
                                                                                            $ renpy.notify("+20 Self-Awareness")
                                                                                            $ self_awareness += 20
                                                                                            jump me_bathtime_1_change_result
                                                                                        "They taught me well.":
                                                                                            $ bathtime_1_choices.append("They taught me well.")
                                                                                            $ renpy.notify("+20 Self-Awareness")
                                                                                            $ self_awareness += 20
                                                                                            jump me_bathtime_1_practical_result
                                                                                        "I'll get more chances. Nothing's unfixable.":
                                                                                            $ bathtime_1_choices.append("I'll get more chances. Nothing's unfixable.")
                                                                                            $ renpy.notify("+20 Self-Awareness")
                                                                                            $ self_awareness += 20
                                                                                            jump me_bathtime_1_change_result
                                                                                        "I need to move on.":
                                                                                            $ bathtime_1_choices.append("I need to move on.")
                                                                                            $ renpy.notify("+20 Self-Awareness")
                                                                                            $ self_awareness += 20
                                                                                            jump me_bathtime_1_positive_result
                                                                                "On second thought, no...":
                                                                                    $ bathtime_1_choices.append("On second thought, no...")
                                                                                    jump second_thought
                                                                        "Do I feel like it's justified?":
                                                                            $ bathtime_1_choices.append("Do I feel like it's justified?")
                                                                            menu justified:
                                                                                with Dissolve(2.0)
                                                                                "There are times when I admit I can be hard on myself.":
                                                                                    $ bathtime_1_choices.append("There are times when I admit I can be hard on myself.")
                                                                                    menu hard_on_myself:
                                                                                        with Dissolve(2.0)
                                                                                        "I think I just have to learn to accept that I don't know everything, but...":
                                                                                            $ bathtime_1_choices.append("I think I just have to learn to accept that I don't know everything, but...")
                                                                                            jump dont_know_everything
                                                                                        "It's deserved. How else will I learn?":
                                                                                            $ bathtime_1_choices.append("It's deserved. How else will I learn?")
                                                                                            menu deserved:
                                                                                                with Dissolve(2.0)
                                                                                                "I need to be a better person.":
                                                                                                    $ bathtime_1_choices.append("I need to be a better person.")
                                                                                                    menu better_person:
                                                                                                        with Dissolve(2.0)
                                                                                                        "I think I just have to learn to accept that I don't know everything, but...":
                                                                                                            $ bathtime_1_choices.append("I think I just have to learn to accept that I don't know everything, but...")
                                                                                                            jump dont_know_everything
                                                                                                        "Something about this feels familiar...":
                                                                                                            $ bathtime_1_choices.append("Something about this feels familiar...")
                                                                                                            jump feels_famliar
                                                                                                        "I'll learn from my mistakes":
                                                                                                            $ bathtime_1_choices.append("I'll learn from my mistakes")
                                                                                                            jump my_mistakes
                                                                                                "I don't think I'm being dramatic when I say Disaster will befall me.":
                                                                                                    $ bathtime_1_choices.append("I don't think I'm being dramatic when I say Disaster will befall me.")
                                                                                                    jump disaster_befalls
                                                                                                "But I believe in myself.":
                                                                                                    $ bathtime_1_choices.append("But I believe in myself.")
                                                                                                    $ renpy.notify("+20 Self-Awareness")
                                                                                                    $ self_awareness += 20
                                                                                                    jump me_bathtime_1_positive_result
                                                                                                "I'll learn from my mistakes":
                                                                                                    $ bathtime_1_choices.append("I'll learn from my mistakes")
                                                                                                    jump my_mistakes
                                                                                        "Something about this feels familiar...":
                                                                                            $ bathtime_1_choices.append("Something about this feels familiar...")
                                                                                            jump feels_familiar
                                                                                        "I'll learn from my mistakes":
                                                                                            $ bathtime_1_choices.append("I'll learn from my mistakes")
                                                                                            jump my_mistakes
                                                                                "Where did I get that idea from?":
                                                                                    $ bathtime_1_choices.append("Where did I get that idea from?")
                                                                                    jump that_idea
                                                                        "Where did I get that idea from?":
                                                                            $ bathtime_1_choices.append("Where did I get that idea from?")
                                                                            jump that_idea
                                                                "I think I just have to learn to accept that I don't know everything, but...":
                                                                    $ bathtime_1_choices.append("I think I just have to learn to accept that I don't know everything, but...")
                                                                    menu dont_know_everything:
                                                                        with Dissolve(2.0)
                                                                        "I choose to believe in myself":
                                                                            $ bathtime_1_choices.append("I choose to believe in myself")
                                                                            $ renpy.notify("+20 Self-Awareness")
                                                                            $ self_awareness += 20
                                                                            jump me_bathtime_1_positive_result
                                                                        "I need to move on.":
                                                                            $ bathtime_1_choices.append("I need to move on.")
                                                                            $ renpy.notify("+20 Self-Awareness")
                                                                            $ self_awareness += 20
                                                                            jump me_bathtime_1_practical_result
                                                                        "I'm going to have faith and enjoy the ride":
                                                                            $ bathtime_1_choices.append("I'm going to have faith and enjoy the ride")
                                                                            $ renpy.notify("+20 Self-Awareness")
                                                                            $ self_awareness += 20
                                                                            jump me_bathtime_1_change_result
                                        "I'm going to have faith and enjoy the ride":
                                            $ bathtime_1_choices.append("I'm going to have faith and enjoy the ride")
                                            $ renpy.notify("+20 Self-Awareness")
                                            $ self_awareness += 20
                                            jump me_bathtime_1_change_result
                                        "On second thought, no...":
                                            $ bathtime_1_choices.append("On second thought, no...")
                                            menu second_thought:
                                                with Dissolve(2.0)
                                                "How I feel...":
                                                    $ bathtime_1_choices.append("How I feel...")
                                                    jump how_i_feel
                                                "There are times when I admit I can be hard on myself.":
                                                    $ bathtime_1_choices.append("There are times when I admit I can be hard on myself.")
                                                    jump hard_on_myself
                                                "I need to move on.":
                                                    $ bathtime_1_choices.append("I need to move on.")
                                                    $ renpy.notify("+20 Self-Awareness")
                                                    $ self_awareness += 20
                                                    jump me_bathtime_1_practical_result
                                                "Where did I get that idea from?":
                                                    $ bathtime_1_choices.append("Where did I get that idea from?")
                                                    jump that_idea
                                                "I choose to believe in myself!":
                                                    $ bathtime_1_choices.append("I choose to believe in myself!")
                                                    $ renpy.notify("+20 Self-Awareness")
                                                    $ self_awareness += 20
                                                    jump me_bathtime_1_positive_result
                                                "I'm going to have faith and enjoy the ride":
                                                    $ bathtime_1_choices.append("I'm going to have faith and enjoy the ride")
                                                    $ renpy.notify("+20 Self-Awareness")
                                                    $ self_awareness += 20
                                                    jump me_bathtime_1_change_result
                                        "It's deserved. How else will I learn?":
                                            $ bathtime_1_choices.append("It's deserved. How else will I learn?")
                                            jump deserved
                                "What if they do?":
                                    $ bathtime_1_choices.append("What if they do?")
                                    menu things_work_out:
                                        with Dissolve(2.0)
                                        "I'm going to have faith and enjoy the ride":
                                            $ bathtime_1_choices.append("I'm going to have faith and enjoy the ride")
                                            $ renpy.notify("+20 Self-Awareness")
                                            $ self_awareness += 20
                                            jump me_bathtime_1_change_result
                                        "I choose to believe in myself":
                                            $ bathtime_1_choices.append("I choose to believe in myself")
                                            $ renpy.notify("+20 Self-Awareness")
                                            $ self_awareness += 20
                                            jump me_bathtime_1_positive_result
                                        "I need to move on.":
                                            $ bathtime_1_choices.append("I need to move on.")
                                            $ renpy.notify("+20 Self-Awareness")
                                            $ self_awareness += 20
                                            jump me_bathtime_1_practical_result
                        "Sometimes I feel insecure.":
                            $ bathtime_1_choices.append("Sometimes I feel insecure.")
                            jump insecure
                        "I think I just have to learn to accept that I don't know everything, but...":
                            $ bathtime_1_choices.append("I think I just have to learn to accept that I don't know everything, but...")
                            jump dont_know_everything
                "I'm doubtful...":
                    $ bathtime_1_choices.append("I'm doubtful...")
                    menu doubtful:
                        with Dissolve(2.0)
                        "I keep second-guessing myself and thinking about other possibilities...":
                            $ bathtime_1_choices.append("I keep second-guessing myself and thinking about other possibilities...")
                            jump second_guessing
                        "What if things don't go as planned?":
                            $ bathtime_1_choices.append("What if things don't go as planned?")
                            jump not_as_planned
                        "There are times when I admit I can be hard on myself.":
                            $ bathtime_1_choices.append("There are times when I admit I can be hard on myself.")
                            jump hard_on_myself
        "My thoughts...":
            $ bathtime_1_choices.append("My thoughts...")
            menu:
                "Have been rude!":
                    $ bathtime_1_choices.append("Have been rude!")
                    menu rude:
                        with Dissolve(2.0)
                        "Do I feel like it's justified?":
                            $ bathtime_1_choices.append("Do I feel like it's justified?")
                            jump justified
                        "There are times when I admit I can be hard on myself.":
                            $ bathtime_1_choices.append("There are times when I admit I can be hard on myself.")
                            jump hard_on_myself
                        "It's deserved. How else will I learn?":
                            $ bathtime_1_choices.append("It's deserved. How else will I learn?")
                            jump deserved
                "Have been mostly positive":
                    $ bathtime_1_choices.append("Have been mostly positive")
                    menu mostly_positive:
                        with Dissolve(2.0)
                        "Meeting new people, experiencing new things, chasing down a whirlwind romance...":
                            $ bathtime_1_choices.append("Meeting new people, experiencing new things, chasing down a whirlwind romance...")
                            jump whirlwind_romance
                        "It's nice to know that I'm capable of achieving happiness for myself.":
                            $ bathtime_1_choices.append("It's nice to know that I'm capable of achieving happiness for myself.")
                            jump achieve_happiness
                "Have been a bit negative":
                    $ bathtime_1_choices.append("Have been a bit negative")
                    menu bit_negative:
                        with Dissolve(2.0)
                        "Sometimes I feel insecure.":
                            $ bathtime_1_choices.append("Sometimes I feel insecure.")
                            jump insecure
                        "There are times when I admit I can be hard on myself.":
                            $ bathtime_1_choices.append("There are times when I admit I can be hard on myself.")
                            jump hard_on_myself
                        "I need to be a better person.":
                            $ bathtime_1_choices.append("I need to be a better person.")
                            jump better_person
        "My choices...":
            $ bathtime_1_choices.append("My choices...")
            menu:
                with Dissolve(2.0)
                "I'm satisfied with them.":
                    $ bathtime_1_choices.append("I'm satisfied with them.")
                    menu:
                        with Dissolve(2.0)
                        "It's nice to know that I'm capable of achieving happiness for myself.":
                            $ bathtime_1_choices.append("It's nice to know that I'm capable of achieving happiness for myself.")
                            jump achieve_happiness
                        "Things might not work out, but that's a natural part of life.":
                            $ bathtime_1_choices.append("Things might not work out, but that's a natural part of life.")
                            jump part_of_life
                        "I'm excited...":
                            $ bathtime_1_choices.append("I'm excited...")
                            jump excited
                "I have regrets.":
                    $ bathtime_1_choices.append("I have regrets.")
                    menu:
                        with Dissolve(2.0)
                        "I keep second-guessing myself and thinking about other possibilities...":
                            $ bathtime_1_choices.append("I keep second-guessing myself and thinking about other possibilities...")
                            jump second_guessing
                        "It's deserved. How else will I learn?":
                            $ bathtime_1_choices.append("It's deserved. How else will I learn?")
                            jump deserved
                        "What if things don't go as planned?":
                            $ bathtime_1_choices.append("What if things don't go as planned?")
                            jump not_as_planned

label me_bathtime_1_positive_result:
    menu:
        with Dissolve(2.0)
        "It can be tough, but the only productive choice I have is to stay positive, believe in myself, and trust that everything will work out!":
            call after_bathtime_1 from _call_after_bathtime_1_3
            scene menmi-apartment-afternoon with dissolve
            m "What a rejuvenating bath! I feel completely cleansed and ready to take on whatever's ahead."
            jump menmi_after_bath

label me_bathtime_1_practical_result:
    menu:
        with Dissolve(2.0)
        "I might have some stuff to work out, but I can proceed with caution. What other choice do I have?":
            call after_bathtime_1 from _call_after_bathtime_1_4
            scene menmi-apartment-afternoon with dissolve
            m "I'm still working through my thoughts and feelings, but I've gotten some clarity. It's nice to slow down every now and then."
            jump menmi_after_bath

label me_bathtime_1_change_result:
    menu:
        with Dissolve(2.0)
        "I need to give myself time to see how things play out, and check in with myself regularly. Change is the only constant, and I have to be ready for it.":
            call after_bathtime_1 from _call_after_bathtime_1_5
            scene menmi-apartment-afternoon with dissolve
            m "Things are starting to feel a little clearer. I'm glad I took the time to reflect."
            jump menmi_after_bath
    pause

label after_bathtime_1:
    show tutorial-box-insights
    screen narrative_tutorial():
        vbox:
            xalign 0.5
            yalign 0.5
            xmaximum 1000
            box_wrap True
            text """
            We make sense of our experiences by reflecting and internalizing them into {b}insights{/b}. In turn, these {b}insights{/b} help us make sense of the world and take appropriate action.

            Menmi's bathtime {b}insights{/b} may come back to her in daily life. Check the planner to see which {b}insights{/b} are currently top-of-mind.
            """
    show screen narrative_tutorial with dissolve
    pause
    hide screen narrative_tutorial
    hide tutorial-box-insights
    show screen choice_history(bathtime_1_choices) with dissolve
    pause
    hide screen choice_history
    return

label menmi_after_bath:
    stop music fadeout 1.0
    play music "<from 5>/audio/cloud.wav" fadein 1.0
    scene menmi-apartment-afternoon with dissolve

    if week == 4:
        m "Ah...I'm glad I took the time to unwind and cleanse. I wonder what next week will bring..."
        jump reading_time

    elif week<4:
        m "Now that I'm refreshed, I can start thinking about my plans for the week ahead!"
        hide screen open_planner
        hide screen open_insights
        scene planner-week-unfilled with dissolve
        m """I'm settling into my weekday routine, but I should plan what I want to do on the weekends.

        It seems like I'll be able to decide what I want to do for the next three weekends! I have to plan ahead if I want to get to all the activities I want to do."""
        m "Girl's gotta have goals."

        m "I'll just drop the activity sticker I want in the 'Weekend' box!"
        call screen planner_weekend(_with_none=False) with dissolve


label reading_time:
    stop music fadeout 1.0
    scene menmi-apartment-night with dissolve
    play music "/audio/reaching-the-sky.mp3" fadein 1.0
    show screen open_planner
    show screen open_insights
    m """
    Now that my schedule's settled, I'm going to snuggle in with a hot mug of tea and an even steamier romance novel.

    Where did I leave off? Oh right."""

    default random_reading = ["reading_1", "reading_2", "reading_3", "reading_4", "reading_5"]
    $ reading_chosen = renpy.random.choice(random_reading)
    jump expression reading_chosen


label reading_1:
    m """
    Alaynna was just about to start a false courtship with Krystof as a ploy to placate her status-obsessed mother.

    Little does she know that Krystoff is actually her great grandson from the future
    who killed the *real* Krystoff in a hit-and-run caused by his self-driving Teslatte.

    Will Alaynna travel back in time to kill Krystoff before he can commit the murder?

    OR will she fall haplessly in love with him? *And* his friend?

    The future is anybody's guess. """

    jump after_reading

label reading_2:
    m """
    Celine had just been kidnapped by the pirates and held for a ransom her disgraced noble family cannot hope to pay.

    What she doesn't know is that the pirate captain is actually a dashing young rapscallion in need of an etiquette coach for his formal banquet with Ahab's Whale (he's kind of a big deal).

    Celine is now confronted with a choice: to make a prince out of a pirate...

    Or to betray his hard-won trust and take the Whale for herself...
    """
    jump after_reading

label reading_3:
    m """
    Tatiana has just infiltrated the enemy dictator's polar base with her partner Agent Desmond.

    He's as comely as he is combative.

    They've just settled down for the night when Desmond realizes he packed only *one* sleeping bag.

    Will Tatiana consent to sharing the sleeping bag or will she kill Desmond and sleep inside his corpse?

    The heat's turning up...
    """
    jump after_reading

label reading_4:
    m """
    Vivienne has been tasked with picking up her older and obviously plainer sister's wedding dress.

    When she finds out there's been a mix-up at the tailor's, she has to put aside her differences with the apathetic apprentice Gustavo
    to track down her sister's gown.

    Little does she know...Gustavo has a secret...

    It's {i}*vampires*{/i}.

    Bonds will be tested. Blood will spill. Bodices *will* be ripped.
    """
    jump after_reading

label reading_5:
    m """
    Beleagured by her hectic job as a high-powered attorney for fashion tragedies, Slayleigh returns to her small, but picturesque hometown in search of some R&R.

    Instead, she finds Liam, the new baker's apprentice whose hard outer crust as a knife dealer hides a soft and fluffy disposition.

    But when a murder shakes her small town, Slayleigh finds herself amidst a decades-long feud between the bakers and those who oppose all baked goods, known only as "The Glutenless".

    Will Slayleigh rise to the occassion? Or will her theories end up half-baked?

    """
    jump after_reading

label after_reading:
    m """
    The drama! Who needs enemies when you've got *literature*?

    So long, reality. I hardly knew thee. """

    $ random_reading.remove(reading_chosen)

    $ week += 1
    jump week_2_4
