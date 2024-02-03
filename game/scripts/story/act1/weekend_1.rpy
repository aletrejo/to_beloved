label weekend_1:
    scene image Solid("#ffc6ebff") with fade
    show text "{font=fredoka}{size=288}Weekend 1{/size}{/font}" at truecenter with dissolve
    pause
    scene menmi-apartment-morning with dissolve
    m """
    Mmmmmm... Ah, did I sleep in? It's so late!

    Aaaah I was so tired that I forgot to set an alarm.

    Part of me feels guilty for losing so much of the day, but then again, I didn't have much planned this weekend.
    """
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

    Let's just say I'm well equipped.
    """
    menu:
        m "Now, what kind of bath am I in the mood for today?"

        "Classic":
            scene bathtime-classic with fade
            m "There's nothing like a simple bath to clear your head and refocus on your body."
        "Romantic":
            scene bathtime-classic with fade
            m "The heady perfumes of lavender and cedar essential oils are so indulgent! Baths always make me feel like I'm being buoyed up into a higher plane of awareness..."
        "Fruity":
            scene bathtime-classic with fade
            m "The sweet and fresh scents of citrus fill me with playful bliss! I feel like I'm in a fresh jug of lemonade. Aahhh, baths are so refreshing."
    window hide
    show tutorial box
    screen bathtime():
        vbox:
            xalign 0.5
            yalign 0.5
            xmaximum 1000
            box_wrap True
            text "{size=+10}{i}Bathtime{/i}":
                xalign 0.5
            text "   The bath is the perfect place to ponder and process the events of Menmi's week. By making time to take a bath, Menmi performs self-care, replenishing her mental and physical energy. "
            text "   Guide the flow of Menmi's reflections and earn Self-Awareness!"
    show screen bathtime with dissolve
    pause
    hide screen bathtime
    hide tutorial box
    jump bathtime_1
label bathtime_1:
    m "It's been an eventful week. Out of everything's that's happened though, there's one thing I can't get off my mind."
    menu:
        m "What do I want to reflect on?"

        "Naji":
            jump naji_bathtime_1
        "Myself" if self_awareness > 120:
            jump myself_bathtime_1

label naji_bathtime_1:
    menu:
        "I miss how close we used to be...":
            menu:
                "We were neighbors":
                    menu:
                        "Naji and I grew up across the street from each other":
                            menu:
                                "Our parents weren't very close, but we'd play together all the time":
                                    menu:
                                        "Naji's dad left when he was a baby, and his mom was always seeing some new guy.":
                                            menu dad_left:
                                                "I wonder if he keeps in touch with her.":
                                                            $ renpy.notify("+15 Self-Awareness")
                                                            $ self_awareness += 15
                                                            jump naji_bathtime_1_good_result

                                "We're the same age, but I kind of saw him as a little brother":
                                    menu:
                                        "He used to follow me around and do whatever I wanted":
                                            menu:
                                                "He's changed.":
                                                    menu:
                                                        "It makes me uncomfortable":
                                                            menu:
                                                                "I thought I knew him better.":
                                                                    menu:
                                                                        "It makes me feel insecure that I don't know everything about him":
                                                                            $ renpy.notify("+15 Self-Awareness")
                                                                            $ self_awareness += 15
                                                                            jump naji_bathtime_1_good_result
                                                                        "It makes me jealous to think that there are others who are closer to him now":
                                                                            $ renpy.notify("+20 Self-Awareness")
                                                                            $ self_awareness += 20
                                                                            jump naji_bathtime_1_best_result
                                                "Naji would always listen to me vent about my feelings, but he never seemed as open with his own":
                                                    menu bartending_menu:
                                                        "Bartending suits him":
                                                            $ renpy.notify("+15 Self-Awareness")
                                                            $ self_awareness += 15
                                                            jump naji_bathtime_1_good_result
                                                        "Why is Naji's opinion of me such a big deal?":
                                                            $ renpy.notify("+20 Self-Awareness")
                                                            $ self_awareness += 20
                                                            jump naji_bathtime_1_best_result
                                "We're super comfortable with each other":
                                    menu:
                                        "Naji's always made people laugh like it was his job":
                                            menu naji_has_the_rizz_menu:
                                                "He's always had a way with people. Got the rizz, as they say.":
                                                    menu naji_bartending_menu:
                                                        "Bartending suits him":
                                                                $ renpy.notify("+15 Self-Awareness")
                                                                $ self_awareness += 15
                                                                jump naji_bathtime_1_good_result
                                                        "It makes me uncomfortable":
                                                            jump naji_knew_him_better_menu
                "He was my best friend":
                    menu:
                        "We used to mix bath bubbles in the inflatable pool and pretend we were at a spa":
                            menu:
                                "I have a lot of good memories with Naji.":
                                    $ renpy.notify("+15 Self-Awareness")
                                    $ self_awareness += 15
                                    jump naji_bathtime_1_good_result
                                "He's changed.":
                                    menu naji_uncomfortable_menu:
                                        "It makes me uncomfortable":
                                            menu naji_knew_him_better_menu:
                                                "I thought I knew him better.":
                                                    menu:
                                                        "It makes me feel insecure that I don't know everything about him":
                                                            $ renpy.notify("+15 Self-Awareness")
                                                            $ self_awareness += 15
                                                            jump naji_bathtime_1_good_result
                                                        "It makes me jealous to think that there are others who are closer to him now":
                                                            $ renpy.notify("+20 Self-Awareness")
                                                            $ self_awareness += 20
                                                            jump naji_bathtime_1_best_result
        "He seems to be doing well...":
            menu:
                "I'm happy for him":
                    menu:
                        "I didn't know he was so popular...":
                            menu:
                                "He's changed.":
                                    jump naji_uncomfortable_menu
                                "It makes sense.":
                                    menu:
                                        "It makes me uncomfortable":
                                            jump naji_knew_him_better_menu
                                        "By the time we were teens, I could see how he would be considered attractive...physically":
                                            menu:
                                                "I always worried that he was out of my league, though":
                                                    $ renpy.notify("+10 Self-Awareness")
                                                    $ self_awareness += 10
                                                    jump naji_bathtime_1_mid_result
                        "He's always had a way with people. Got the rizz, as they say.":
                            jump naji_bartending_menu
                "I can't help but feel a bit jealous":
                    menu:
                        "Compared to him, I must look like a loser.":
                            menu:
                                "I hope he doesn't think I'm silly for wanting to be in love":
                                    menu naji_opinion:
                                        "Why is Naji's opinion of me such a big deal?":
                                            $ renpy.notify("+20 Self-Awareness")
                                            $ self_awareness += 20
                                            jump naji_bathtime_1_best_result
                        "He's always had a way with people. Got the rizz, as they say.":
                            jump naji_bartending_menu
        "I can't believe he said that about my princess movies!":
            menu:
                "It was upsetting":
                    menu:
                        "But why?":
                            menu:
                                "It threatened my worldview":
                                    menu different_opinions:
                                        "It's OK to have different opinions. Doesn't make either or us less right or wrong.":
                                            jump believe_in_love
                                        "Why is Naji's opinion of me such a big deal?":
                                            jump naji_opinion
                                        "Everyone has to believe in something, and I choose to believe in love!":
                                            jump naji_bathtime_1_mid_result
                                        "He disagreed with me":
                                            jump different_opinions
                                "I hope he doesn't think I'm silly for wanting to be in love":
                                    menu believe_in_love:
                                        "Everyone has to believe in something, and I choose to believe in love!":
                                            $ renpy.notify("+10 Self-Awareness")
                                            $ self_awareness += 10
                                            jump naji_bathtime_1_mid_result
                "Why'd he bring it up?":
                    menu:
                        "To hurt me":
                            menu:
                                "I hope he doesn't think I'm silly for wanting to be in love":
                                    jump believe_in_love
                                "That doesn't make sense":
                                    jump tease_me
                        "To tease me":
                            menu tease_me:
                                "We're super comfortable with each other":
                                    jump naji_laugh_job
                                "Naji's always made people laugh like it was his job":
                                    menu naji_laugh_job:
                                        "It makes me jealous to think that there are others who are closer to him now.":
                                            menu:
                                                "Why is Naji's opinion of me such a big deal?":
                                                    jump naji_opinion

                                        "He’s a good listener":
                                            menu good_listener:
                                                "Bartending suits him":
                                                    $ renpy.notify("+15 Self-Awareness")
                                                    $ self_awareness += 15
                                                    jump naji_bathtime_1_good_result
                                                "Naji would always listen to me vent about my feelings, but he never seemed as open with his own":
                                                    menu naji_oppenness:
                                                        "Maybe it was his way of coping":
                                                            menu:
                                                                "Naji's dad left when he was a baby, and his mom was always seeing some new guy.":
                                                                    jump dad_left
                                                        "Why is Naji's opinion of me such a big deal?":
                                                            jump naji_opinion
                                                        "Bartending suits him":
                                                            jump bartending_menu



            $ self_awareness += 10
            jump naji_bathtime_1_mid_result
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
