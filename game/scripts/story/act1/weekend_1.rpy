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
            c "You gave it your all this week. You're allowed to relax. Not every second of your life has to be dedicated to productivity. Listen to your body. Listen to *me*."
            $ renpy.notify("+10 Self-Awareness")
            $ self_awareness += 10
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
            m "There's nothing like a simple bath to clear your head and refocus on your body."
        "Romantic":
            m "The heady perfumes of lavender and cedar essential oils are so indulgent! Baths always make me feel like I'm being buoyed up into a higher plane of awareness..."
        "Fruity":
            m "The sweet and fresh scents of citrus fill me with playful bliss! I feel like I'm in a fresh jug of lemonade. Aahhh, baths are so refreshing."