label weekend_1:
    play sound "/audio/pencil-write.mp3"
    scene city-morning with dissolve:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}Week 1{/size}{/font}{/color}{color=#000000}{font=JustAnotherHand-Regular.ttf}{size=200}\n Weekend!{/size}{/font}{/color}" at truecenter with wiperight
    pause

    scene menmi-apartment-morning with dissolve
    play music "<from 9>/audio/happily-ever-after.mp3" fadein 0.5
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
    play music "/audio/happily-ever-after.mp3"

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
    show tutorial-box-bathtime
    screen bathtime():
        vbox:
            xalign 0.5
            yalign 0.6
            xmaximum 1000
            box_wrap True
            text """
            Bathtime is Men-ME time! By making time to take a bath, Menmi performs self-care, replenishing her mental and physical energy.

            The bath is the perfect place to ponder and process the events of Menmi’s week. You’ll be able to guide the flow of Menmi’s reflections.

            The more insight she gains into her life, the more {b}Self-Awareness{/b} you’ll earn.
            """
    show screen bathtime with dissolve
    pause
    hide screen bathtime
    hide tutorial-box-bathtime
    jump bathtime_1
label bathtime_1:
    m "It's been an eventful week. Out of everything's that's happened though, there's one thing I can't get off my mind."
    menu:
        m "What do I want to reflect on?"

        "Naji":
            jump naji_bathtime_1
        "Myself" if self_awareness > 30:
            jump myself_bathtime_1

label naji_bathtime_1:
    menu we_were_close:
        "I miss how close we used to be...":
            menu:
                "We were neighbors":
                    menu:
                        "Naji and I grew up across the street from each other":
                            menu across_the_street:
                                "Naji's mom dropped him off at our house a lot, so we spent a lot of time together.":
                                    menu dropped_off:
                                        "Naji's dad left when he was a baby, and his mom didn't make time for him. He had to go through a lot on his own.":
                                            menu on_his_own:
                                                "That's probably why he's so reticent. Even if he spoke up, his feelings always came second to hers.":
                                                    menu second_to_hers:
                                                        "I wonder if he keeps in touch with her.":
                                                            $ renpy.notify("+20 Self-Awareness")
                                                            $ self_awareness += 20
                                                            jump naji_bathtime_1_best_result
                                                "Naji's mom was always with a new guy who didn't last. That's probably why he never seemed interested in romance.":
                                                    menu new_guy:
                                                        "I wonder if he keeps in touch with her.":
                                                            $ renpy.notify("+20 Self-Awareness")
                                                            $ self_awareness += 20
                                                            jump naji_bathtime_1_best_result
                                                        "I was protective of him":
                                                            menu protective:
                                                                "Naji would always listen to me vent about my feelings, but he never seemed as open with his own":
                                                                    menu vent:
                                                                        "Bartending suits him":
                                                                            $ renpy.notify("+15 Self-Awareness")
                                                                            $ self_awareness += 15
                                                                            jump naji_bathtime_1_good_result
                                                                        "I hope he can be open with me someday...":
                                                                            $ renpy.notify("+15 Self-Awareness")
                                                                            $ self_awareness += 15
                                                                            jump naji_bathtime_1_good_result
                                                                        "He's not the type to share his feelings":
                                                                            jump share_his_feelings
                                                                        "Naji prioritizes the needs of others before his own":
                                                                            menu prioritize_others:
                                                                                "Bartending suits him":
                                                                                    $ renpy.notify("+15 Self-Awareness")
                                                                                    $ self_awareness += 15
                                                                                    jump naji_bathtime_1_good_result
                                                                                "He's a good guy.":
                                                                                    menu good_guy:
                                                                                        "There were times I wondered if we could be more than friends...":
                                                                                            jump more_than_friends
                                                                                        "I have a lot of good memories with Naji.":
                                                                                            jump good_memories
                                                                                        "I have to keep that in mind, no matter what happens going forward.":
                                                                                            $ renpy.notify("+15 Self-Awareness")
                                                                                            $ self_awareness += 15
                                                                                            jump naji_bathtime_1_good_result
                                                                                "He’s a good listener":
                                                                                    jump good_listener
                                                                                "He used to follow me around and do whatever I wanted":
                                                                                    jump follow_me
                                                                                "Maybe it was his way of coping":
                                                                                    menu coping:
                                                                                        "Naji's dad left when he was a baby, and his mom didn't make time for him. He had to go through a lot on his own.":
                                                                                            jump on_his_own
                                                                "We're the same age, but I kind of saw him as a little brother":
                                                                    jump little_brother
                                                        "By the time we were in high school, I could see how he would be considered attractive...physically":
                                                            menu attractive_in_hs:
                                                                "I always worried that he was out of my league, though":
                                                                    $ renpy.notify("+10 Self-Awareness")
                                                                    $ self_awareness += 10
                                                                    jump naji_bathtime_1_mid_result
                                                "I have to keep that in mind, no matter what happens going forward.":
                                                    $ renpy.notify("+15 Self-Awareness")
                                                    $ self_awareness += 15
                                                    jump naji_bathtime_1_good_result
                                        "We used to mix bath bubbles in the inflatable pool and pretend we were at a spa":
                                            menu bubbles:
                                                "He used to follow me around and do whatever I wanted":
                                                    menu follow_me:
                                                        "I was protective of him":
                                                            jump protective
                                                        "Naji would always listen to me vent about my feelings, but he never seemed as open with his own":
                                                            jump vent
                                                        "He's changed.":
                                                            jump naji_changed
                                                "We're the same age, but I kind of saw him as a little brother":
                                                    jump little_brother
                                                "We're super comfortable with each other":
                                                    jump comfortable
                                                "I have a lot of good memories with Naji.":
                                                    menu good_memories:
                                                        "He's changed.":
                                                            jump naji_changed
                                                        "I have to keep that in mind, no matter what happens going forward.":
                                                            $ renpy.notify("+15 Self-Awareness")
                                                            $ self_awareness += 15
                                                            jump naji_bathtime_1_good_result
                                "We're the same age, but I kind of saw him as a little brother":
                                    menu little_brother:
                                        "He used to follow me around and do whatever I wanted":
                                            jump follow_me
                                        "By the time we were in high school, I could see how he would be considered attractive...physically":
                                            jump attractive_in_hs
                                "We're super comfortable with each other":
                                        menu comfortable:
                                            "We're the same age, but I kind of saw him as a little brother":
                                                jump little_brother
                                            "He’s a good listener":
                                                menu good_listener:
                                                    "Naji's dad left when he was a baby, and his mom didn't make time for him. He had to go through a lot on his own.":
                                                        jump on_his_own
                                                    "Naji would always listen to me vent about my feelings, but he never seemed as open with his own":
                                                        jump vent
                                                    "Bartending suits him":
                                                        $ renpy.notify("+15 Self-Awareness")
                                                        $ self_awareness += 15
                                                        jump naji_bathtime_1_good_result
                                            "It makes me jealous to think that there are others who are closer to him now":
                                                menu closer_to_him:
                                                    "I hope he can be open with me someday...":
                                                        $ renpy.notify("+15 Self-Awareness")
                                                        $ self_awareness += 15
                                                        jump naji_bathtime_1_good_result
                                                    "I don't know...or maybe I'm not ready to face it yet. I need more insight on this.":
                                                        $ renpy.notify("+20 Self-Awareness")
                                                        $ self_awareness += 20
                                                        jump naji_bathtime_1_best_result
                        "We were pretty close through high school, but lost touch after graduation.":
                            menu close_in_hs:
                                "He's changed":
                                    menu naji_changed:
                                        "I thought I knew him better.":
                                            menu knew_him_better:
                                                "It makes me jealous to think that there are others who are closer to him now":
                                                    jump closer_to_him
                                                "It makes me feel insecure that I don't know everything about him":
                                                    $ renpy.notify("+20 Self-Awareness")
                                                    $ self_awareness += 20
                                                    jump naji_bathtime_1_best_result
                                        "It makes me uncomfortable":
                                                jump uncomfortable
                                "Naji's mom dropped him off at our house a lot, so we spent a lot of time together.":
                                        jump dropped_off
                                "There were times I wondered if we could be more than friends...":
                                        menu more_than_friends:
                                            "By the time we were in high school, I could see how he would be considered attractive...physically":
                                                jump attractive_in_hs
                                            "It's romantic to fall for the best friend who's been with you all along. Who knows me better than him?":
                                                menu fall_for_bf:
                                                    "I always worried that he was out of my league, though":
                                                        $ renpy.notify("+10 Self-Awareness")
                                                        $ self_awareness += 10
                                                        jump naji_bathtime_1_mid_result
                                                    "Everyone has to believe in something, and I choose to believe in love!":
                                                        $ renpy.notify("+10 Self-Awareness")
                                                        $ self_awareness += 10
                                                        jump naji_bathtime_1_mid_result
                                                    "I thought I knew him better.":
                                                        jump knew_him_better
                "He was my best friend":
                    menu best_friend:
                        "We used to mix bath bubbles in the inflatable pool and pretend we were at a spa":
                            menu:
                                "I have a lot of good memories with Naji.":
                                    $ renpy.notify("+15 Self-Awareness")
                                    $ self_awareness += 15
                                    jump naji_bathtime_1_good_result
                        "We were pretty close through high school, but lost touch after graduation.":
                            jump close_in_hs
                        "There were times I wondered if we could be more than friends...":
                            jump more_than_friends
                "He's changed.":
                    jump naji_changed
        "He seems to be doing well...":
            menu doing_well:
                "I'm happy for him":
                    menu happy_for_him:
                        "I didn't know he was so popular...":
                            menu popular:
                                "It makes sense.":
                                    menu:
                                        "He's always had a way with people. Got the rizz, as they say.":
                                            jump rizz
                                        "He’s a good listener":
                                            jump good_listener
                                        "By the time we were in high school, I could see how he would be considered attractive...physically":
                                            jump attractive_in_hs
                                        "It makes me uncomfortable":
                                            menu uncomfortable:
                                                "I thought I knew him better.":
                                                    jump knew_him_better
                                                "I can't help but feel a bit jealous":
                                                    jump bit_jealous
                                                "I hope he can be open with me someday...":
                                                    $ renpy.notify("+15 Self-Awareness")
                                                    $ self_awareness += 15
                                                    jump naji_bathtime_1_good_result
                                                "It makes me jealous to think that there are others who are closer to him now":
                                                    jump closer_to_him
                                "I miss how close we used to be…":
                                    jump we_were_close
                                "Compared to him, I must look like a loser.":
                                    jump loser
                                "I can't help but feel a bit jealous":
                                    jump bit_jealous
                                "He's changed":
                                    jump naji_changed
                        "I have to keep that in mind, no matter what happens going forward.":
                            $ renpy.notify("+15 Self-Awareness")
                            $ self_awareness += 15
                            jump naji_bathtime_1_good_result
                        "He's always had a way with people. Got the rizz, as they say.":
                            menu rizz:
                                "Naji prioritizes the needs of others before his own":
                                    jump prioritize_others
                                "Bartending suits him":
                                        $ renpy.notify("+15 Self-Awareness")
                                        $ self_awareness += 15
                                        jump naji_bathtime_1_good_result
                                "Maybe it was his way of coping":
                                    jump coping
                "I can't help but feel a bit jealous":
                    menu bit_jealous:
                        "He was my best friend":
                            jump best_friend
                        "He's always had a way with people. Got the rizz, as they say.":
                            jump rizz
                        "Compared to him, I must look like a loser.":
                            menu loser:
                                "I hope he doesn't think I'm silly for wanting to be in love":
                                    menu love_is_silly:
                                        "Why is Naji's opinion of me such a big deal?":
                                            menu najis_opinion:
                                                "I don't know...or maybe I'm not ready to face it yet. I need more insight on this.":
                                                    $ renpy.notify("+20 Self-Awareness")
                                                    $ self_awareness += 20
                                                    jump naji_bathtime_1_best_result
                                                "He's not the type to share his feelings":
                                                    jump share_his_feelings
                                        "Everyone has to believe in something, and I choose to believe in love!":
                                            $ renpy.notify("+10 Self-Awareness")
                                            $ self_awareness += 10
                                            jump naji_bathtime_1_mid_result
                                        "It's romantic to fall for the best friend who's been with you all along. Who knows me better than him?":
                                            jump fall_for_bf
                                "I always worried that he was out of my league.":
                                    $ renpy.notify("+10 Self-Awareness")
                                    $ self_awareness += 10
                                    jump naji_bathtime_1_mid_result
                                "He's always had a way with people. Got the rizz, as they say.":
                                    jump rizz
                                "Maybe I shouldn't have talked about my love life...":
                                    menu love_life:
                                        "Why not, though?":
                                            menu:
                                                "It was inappropriate":
                                                    menu inappropriate:
                                                        "Maybe I was coming on too strong for our first time seeing each other in so long, but it's not like we're total strangers.":
                                                            menu coming_on_too_strong:
                                                                "Naji would always listen to me vent about my feelings, but he never seemed as open with his own":
                                                                    jump vent
                                                                "Naji and I grew up across the street from each other":
                                                                    jump across_the_street
                                                                "I have a lot of good memories with Naji.":
                                                                    jump good_memories
                                                        "Naji's mom was always with a new guy who didn't last. That's probably why he never seemed interested in romance.":
                                                            jump new_guy
                                                "I don't know...or maybe I'm not ready to face it yet. I need more insight on this.":
                                                    $ renpy.notify("+20 Self-Awareness")
                                                    $ self_awareness += 20
                                                    jump naji_bathtime_1_best_result
                                                "We're super comfortable with each other":
                                                    jump comfortable
                                        "There were times I wondered if we could be more than friends...":
                                            jump more_than_friends
                                        "Naji's not the type to share his feelings":
                                            jump share_his_feelings
                "We were pretty close through high school, but lost touch after graduation.":
                    jump close_in_hs
        "Why did he seem reluctant to talk about love?":
            menu reluctant:
                "I must have said something to make him uncomfortable":
                    menu made_him_uncomfortable:
                        "I hope he doesn't think I'm silly for wanting to be in love":
                            jump love_is_silly
                        "Maybe I shouldn't have talked about my love life...":
                            jump love_life
                        "He's not the type to share his feelings":
                            menu share_his_feelings:
                                "Naji prioritizes the needs of others before his own":
                                    jump prioritize_others
                                "Maybe it was his way of coping":
                                    jump coping
                                "I hope he can be open with me someday...":
                                    $ renpy.notify("+15 Self-Awareness")
                                    $ self_awareness += 15
                                    jump naji_bathtime_1_good_result
                "He's hiding something":
                    menu hiding_something:
                        "His past...":
                            menu:
                                "Naji's mom was always with a new guy who didn't last. That's probably why he never seemed interested in romance.":
                                    jump new_guy
                        "His feelings...":
                            menu najis_feelings:
                                "I hope he doesn't think I'm silly for wanting to be in love":
                                    jump love_is_silly
                                "Naji prioritizes the needs of others before his own":
                                    jump prioritize_others
                                "He's not the type to share his feelings":
                                    jump share_his_feelings
                        "Naji would always listen to me vent about my feelings, but he never seemed as open with his own":
                            jump vent

label naji_bathtime_1_mid_result:
    menu:
        "I probably wouldn't have a chance, but there is something romantic about falling in love with your best friend...":
            call after_bathtime_1 from _call_after_bathtime_1
            scene menmi-apartment-night with dissolve
            m "I'm still working through my thoughts and feelings, but I've gotten some clarity. It's nice to slow down every now and then."
            jump menmi_after_bath
label naji_bathtime_1_good_result:
    menu:
        "Naji's grown with time. I'm curious about what else about him has changed...":
            call after_bathtime_1 from _call_after_bathtime_1_1
            scene menmi-apartment-night with dissolve
            m "Things are starting to feel a little clearer. I'm glad I took the time to reflect."
            jump menmi_after_bath
label naji_bathtime_1_best_result:
    menu:
        "Why do I feel so self-conscious around Naji now that he's different from how I remember? Maybe if I talk to him more, I can sort out my feelings.":
            call after_bathtime_1 from _call_after_bathtime_1_2
            scene menmi-apartment-night with dissolve
            m "What a rejuvenating bath! I feel completely cleansed and ready to take on whatever's ahead."
            jump menmi_after_bath

label myself_bathtime_1:
    pause

label after_bathtime_1:
    scene bathtime-classic with dissolve
    show tutorial box
    screen narrative_tutorial():
        vbox:
            xalign 0.5
            yalign 0.5
            xmaximum 1000
            box_wrap True
            text "{size=+10}{i}Creating A Narrative{/i}":
                xalign 0.5
            text "   We internalize events and experiences by telling ourselves stories. In turn, through these narratives, we make sense of the world."
            text "   Because of this, Menmi may remember her bathtime ruminations as she goes about her daily life. Her narratives may even influence her thoughts and actions."
            text "   Narratives are flexible and naturally evolve over time, so be sure to check the planner and reflect regularly."
    show screen narrative_tutorial with dissolve
    pause
    hide screen narrative_tutorial
    hide tutorial box
    return

label menmi_after_bath:
    m "Now that I'm refreshed, I can start thinking about my plans for the week ahead!"
