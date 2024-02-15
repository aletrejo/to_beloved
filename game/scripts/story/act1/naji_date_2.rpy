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

    It’s been a while since I’ve seen Naji outside the lounge.

    As much as I like the William Collins, I’m looking forward to hanging out some place where the drinks aren’t strong enough to make you forget about how much you paid for them.

    I’m waiting for Naji in front of the lounge when a squeaky "Mee!" pipes in from my periphery.
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

    “Who’s this little darling?” """

    hide naji-neutral
    show naji-surprised

    #Relevant Insights: We're super comfortable with each other; I have a lot of good memories with Naji.
    m "Naji looks up, startled, but the tension in his shoulders uncoils once he sees me."

    hide naji-surprised
    show naji-smile

    n "“Menmi, you are in the presence of one of our most esteemed patrons.”"
    m """
    His grin is wide, like a proud father’s.

    I gasp. “And here I've been caught without my clutching pearls!”"""

    hide naji-smile
    show naji-laugh

    m """
    Naji’s laughter sounds comfortingly intimate cocooned within the alleyway.

    “Does she have a name?”
    """

    hide naji-laugh
    show naji-lookaway

    m "Naji runs a hand through his hair and drops his gaze to the ground, suddenly sheepish."
    n "“Yeah, actually...ee...”"
    m "“Pardon?”"

    #Relevant Insights:  It makes me feel insecure that I don't know everything about him; I thought I knew him better; I hope he can be open with me someday...; He's hiding something
    m """
    Why's he being shy all of a sudden? He practically whispered that last part.

    Naji clears his throat.
    """
    n "“Mimi...it’s Mimi.”"

    hide naji-lookaway
    show naji-blush

    n "{cps=*2}“Any resemblances to any people real or fictional are purely coincidental.”{/cps}"
    i "Thanks for the disclaimer...not sus in the slightest."

    #Relevant Insights: I always worried that he was out of my league, though; Why is Naji's opinion of me such a big deal?; Sometimes I feel insecure.; I'll learn from my mistakes
    m "It's not like Naji named the cat after *me* or anything..."
    play sound "/audio/kitty_mew.mp3"
    "Mimi" "“Mee! Mee!”"
    m "“Haha she just said her name. Like a Pokébowlmon!”"

    stop music
    play sound "/audio/impact-slam.mp3"
    scene alleyway with vpunch:
        matrixcolor InvertMatrix(value=1.0)
        m "So why are my cheeks burning?"

        if self_awareness<60:
            #Relevant Insights: Maybe I shouldn't have talked about my love life...Compared to him, I must look like a loser; I hope he doesn't think I'm silly for wanting to be in love; I always worried that he was out of my league, though
            i "Naji? Like *you*? Cool dumb thought, Menmi."
        elif self_awareness>=60:
            #Relevant Insights: There were times I wondered if we could be more than friends...;I have a lot of good memories with Naji; It's romantic to fall for the best friend who's been with you all along. Who knows me better than him?; I choose to believe in myself!
            c "I mean, he *did* get all defensive about it. You can be cautiously optimistic."

    scene alleyway with vpunch
    play music "/audio/najis-theme.mp3"
    show naji-neutral

    #Relevant Insights:  I'm going to have faith and enjoy the ride; I have to keep that in mind, no matter what happens going forward.
    m """
    I need to be present and focus on the moment in front of me.

    The cat, having finished her meal, purrs happily as she squeezes her rounded form around his legs.

    “Oh my gosh, Naji. Is she–”
    """

    n "“Yeah, pregnant. I think she’s due soon.”"

    hide naji-neutral
    show naji-frown
    #Relevant Insights: Naji prioritizes the needs of others before his own; He's a good guy.
    n """
    "It's been tricky to care for her with work being so hectic, but it's not like I can leave her alone..."

    "Poor thing. She's probably looking for a safe space to give birth.”
    """

    m "“But if you’re doing this much already, why not just take her in? Or call a shelter?”"

    hide naji-frown
    show naji-lookaway

    #Relevant Insights: Naji's mom dropped him off at our house a lot, so we spent a lot of time together.]
    n """
    “I’ve thought about it, but I’m really not home often enough to care for a cat...cats.”

    “And with the city shelters as packed as they are, who knows what’ll happen to a pregnant cat?”
    """

    hide naji-lookaway
    show naji-neutral

    #Relevant Insights:  Naji's dad left when he was a baby, and his mom didn't make time for him. He had to go through a lot on his own
    n "“She’s her own cat, you know? She’s free. She made it this far on her own without anyone’s help.”"

    #Relevant Insights: Naji's mom was always with a new guy who didn't last. That's probably why he never seemed interested in romance.
    n "“Who am I to take away her freedom just so I can feel reassured about her safety?”"

    #Relevant Insights: He's not the type to share his feelings; Naji would always listen to me vent about my feelings, but he never seemed as open with his own; He's hiding something
    m """
    Naji's getting so passionate about this.

    I can't read the subtext from this distance. We might have to get personal.
    """

label choice_12:
    menu:
        "Agree":
            c "He wants to be reassured that he's doing the right thing. As his friend, you should validate his feelings."
            #If any of these Insights were chosen: That's probably why he's so reticent. Even if he spoke up, his feelings always came second to hers; He's not the type to share his feelings; Naji's grown with time. I'm curious about what else about him has changed...
            #m "It must be difficult for him to share how he really feels."

            #Relevant Insight: I was protective of him; I think I just have to learn to accept that I don't know everything, but...
            m """
            “Yeah, I see where you’re coming from.”

            Naji nods silently, long fingers brushing behind Mimi’s ear for a scratch.
            """
        "Challenge him":
            #Relevant Insights: I hope he can be open with me someday...
            c """
            It's unlikely that he'll offer more information on his own.

            Offering a different perspective could help him give the issue more thought.
            """
            m "“How can you be sure that she's made it this far on her own? Friendly strays usually have had experiences with humans.”"

            hide naji-neutral
            show naji-lookaway

            n """
            ...

            “Yeah, you’ve got a point.”
            """
            $ renpy.notify("+5 Self-Awareness")
            $ self_awareness += 5

            #Relevant Insights: His past...; His feelings...; Maybe it was his way of coping; Naji's dad left when he was a baby, and his mom didn't make time for him.  He had to go through a lot on his own.
            n """
            “I don’t know, but...”

            “I guess I might have been seeing myself in her situation.”
            """
        "Ask him to clarify":
            c "Just ask him. You might be able to support him if he feels like sharing."
            m """
            “What do you mean by that?”

            Naji pauses, brows scrunched.

            The sizzle in his eyes have dissipated, and he seems to be considering his next words carefully.

            """

            #Relevant Insights: He's not the type to share his feelings; Naji would always listen to me vent about my feelings, but he never seemed as open with his own; That's probably why he's so reticent. Even if he spoke up, his feelings always came second to hers.
            n "“I don't want to talk about this anymore. All I'll say is...”"
            
        "There’s something deeper at play..." if self_awareness>=70:
            #Relevant Insights: Where did I get that idea from?; Naji prioritizes the needs of others before his own; Maybe it was his way of coping; My family; His past...
                c "There's a way to make sense of this."
                scene alleyway:
                    blur 30
                show naji-lookaway:
                    blur 50
                m """
                I reach into the past, recalling the details of Naji’s upbringing.

                Naji’s single mother was often absent, and whenever she was around, it seemed like she always had something for Naji to do.

                I’d remember times when we'd play "laundry" while she nursed a hangover in her bedroom.
                """
