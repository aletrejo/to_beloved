# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character ("Menmi", color='#F52088')
define c = Character ("Menmi's Conscience", color='#750F41')
define n = Character ("Naji", color='#E59A34')
define j = Character ("Joule", color='#0064C2')
define d = Character ("Devan", color='#800DCD')
define u = Character ("Delivery Guy", color="#6c431a", image="delivery-guy.png")

# Images used in-game
image tutorial box = "tutorial-box.png"

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

    m "Be right there!"

    scene menmi-apartment-door
    with dissolve

    m """
    Standing in the doorway is a tall mystery man holding a small cardboard box.

    He's kind of hot. I can't help but notice how big his hands look wrapped around that tiny box.

    I wonder how they'd look around my...

    Oooh, Menmi! Don't get “carried away” by the UPS Man!
    """

    show delivery-guy

    u "I've got a package for Ms. Menmi?"

    m """
    Yes, that's me!

    As he hands me the package, I feel electricity sparking at the brief synapse between our fingers.

    Is this...chemistry?
    """

    scene menmi-apartment-door:
        blur 24

    show delivery-guy at truecenter:
        blur 24
    
    m """
    What would it be like to date a delivery man? It'd be kinda wild to be with someone so in-demand in this post-pandemic, 
    pro-postal world.

    Like, he'd find excuses to come visit me – “Oh I'm just in the neighborhood because of a delivery,” 
    but his roguish grin and the takeout for two will say otherwise.

    You're doing some essential work to my heart, baby.

    It sounds so romantic! Should I invite him in?
    """

    c "Come now, scatterbrains – with our apartment in this state? Where's he going to sit, the toilet?" with vpunch

    m "Ugh, it's that naggy inner voice again. Such a party pooper. No pun intended. What is she, my mom?"

label conscience_tutorial:
    window hide
    hide delivery-guy
    show tutorial box
    screen conscience():
        vbox:
            xalign 0.5
            yalign 0.5
            xmaximum 1000
            box_wrap True
            text "{size=+10}{i}Menmi's Conscience{/i}":
                xalign 0.5
            text "Decisions are difficult when we all contain multitudes. Whether she likes it or not, Menmi's Conscience, or \"inner voice\", will sometimes chime in to help her weigh her options."
            text "As in life, the choices you make may affect the tone your Conscience takes. Occasional self-skepticism can build Self-Awareness, but a running dialogue of self-criticism and doubt results in a negative worldview, which makes life sucky!"
        
    show screen conscience with dissolve
    pause
    hide screen conscience
    hide tutorial box
    window show
    menu:
        m "Should I hit on the delivery guy?"

        "I don't know, it might be awkward":
            m "If he sees my place like this, he might not be into me. Besides, this isn't the time or place. {w}{color=#F52088}{b}+5 Self-Awareness{/b}{/color}"
        
        "You miss every shot you don't take!":
            m "I know what I want, and I have to be proactive about it. No one's going to hand love to me on a platter, uh, package."
            m "Would you like to come inside for a drink?{w}{color=#F52088}{b}+5 Self-Awareness{/b}{/color}"
label self_awareness_tutorial:
    window hide
    show tutorial box
    screen self_awareness():
        vbox:
            xalign 0.5
            yalign 0.5
            xmaximum 1000
            box_wrap True
            text "{size=+10}{i}Self-Awareness{/i}":
                xalign 0.5
            text "Nice job -- you just gained some Self-Awareness. When Menmi makes sound decisions and processes events mindfully, she gains insight into her own behaviors and emotions."
            text "Accumulating Self-Awareness helps Menmi get through life with less distortion and more resilience, self-esteem, and stability. Having more Self-Awareness also allows opens up more possibilities for Menmi's Conscience."   
    show screen self_awareness with dissolve
    pause
    hide screen self_awareness
    hide tutorial box

label after_tutorial:
    show delivery-guy
    u "Ma'am, please just sign for the package."
    m "He seems to be in a rush. I know when to cut my losses."
    c "There's always next time."
    m "Thanks! Take care."
    m "I grab the package and shut the door behind me. Oh well, plenty where that came from! I hope all the guys in Mangottan are this cute."
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
            text "Player chooses cover for planner and decorates it with stickers"   
    show screen planner with dissolve
    pause
    hide screen planner
    hide tutorial box
    window show
    m """
    {i}Gasp{/i}...Oh my god?

    It's perfect? Did I really do this? Great job, Menmi. Take that, expectations!
    """
    scene planner with dissolve
    m """
    OK. Time to fill it out. Blank pages sure are intimidating.

    It's a good thing I know what my weekday schedule already looks like.
    """
    scene gym-inside with dissolve
    m "Mornings are at the gym! Gotta start the day strong with my favorite workout — Spotting hot guys."
    scene office-inside with dissolve
    m "Then, it's time to head to my dream job. I'm so excited to make a difference in the world!"
    scene lounge-inside with dissolve
    m "At the end of the day, I'll unwind with a drink. One of my friends from home is a bartender! Ooooohh getting wasted on a weeknight? We grow up so fast"

label choosing_prince:
    scene applecore-city with dissolve
    m """
    There! My perfect first week in the perfect city at the start of my perfect life — perfectly planned!

    I'm supporting myself with my own money in my own apartment in the BIG CITY! Complete independence!

    And then all I'll need to be complete is the perfect partner. Love is the greatest goal of all, and I've been preparing to fall in love *only* my whole life

    A girls' gotta be ready. That's why I know *exactly* what I'm looking for.
    """
    menu:
        m "My prince charming is..."

        "Friendly, loyal, and compassionate":
            m "Someone who's kind, spends lots of time with me, and puts our love first. Obviously, I want him to be as crazy about me as I definitely will be about him."
        "Strong and protective":
            m "Someone who's always got my back and makes me feel safe from the dangerous world! What's dangerous about it? I don't know. Maybe that's part of the problem."
        "Effortlessly cool and competent":
            m "A mature person who strides through life with unwavering confidence, admired by all. He's always in control...until {i}I{/i} make him lose it."
    m "It's not like I'm expecting it to be all fun and games, of course! Give me more credit than that. I'm a realist at heart."
    c "Are you, though?"
    menu:
        m "Yes! I know all the red flags:"

        "Flawed first impressions that transform into a lasting love":
            m "A string of misunderstandings! A tense, yet thrilling rivalry. Witty banter! Stubborn prides! The belated realization that your petty enmity is rooted in an unshakeable sense of trust! Ah, the initial bitterness makes the happy ending all the sweeter."
        "Traditional family members who don't want to see us together":
            m "His dad, a CEO mafia boss undercover buddy cop sultan, forbids him from consorting with commoners, lest he be lured away from his responsibility to the family “business”. Us against the world! Overthrowing the patriarchy! Singing out the moon roof of a limousine!"
        "Vengeful exes hellbent on sabotaging our happiness":
            m "Naturally, he'll be a man in demand. You know, a skater boy? To whom she said  ‘see ya later boi’? I'll never forget how desirable he is because his ex(es) will constantly be coming after me like they don't have anything better to do!"
        "A tragic accident that leaves us forever changed":
            m "What would I lose? A hand? An eye? Consciousness? Gosh I hope I don't go into a coma – that would be so boring. For the readers. And worse yet? For me. *Gasp* Maybe my beautiful singing voice? I don't have a beautiful singing voice, but maybe I can look into podcasting?"
        "Supernatural secrets threatening to doom our fragile love":
            m "Aaaahh what if he's an 800-year-old vampire nurse who's honest and lonely, but also resentful and idealistic? And I die before him? Oh my gosh I hope he's not mad at me for that."
    scene menmi-apartment-afternoon with dissolve
    m """
    I'm not naive. I know the world isn't all sunshine and six-packs.

    But it's OK, because at the end of the day, as long as I have him, we will overcome the odds and make each other more perfect and whole people.

    Love is the greatest thing that can happen to anyone. To feel, finally, in this cold, lonely world, the safe haven of love...it's the height of the human experience.

    Love is the answer. If you don't believe in that, what's life even for?
    """
    menu:
        m "So there's only one way my story can end:"
        "They lived happily ever after":
            m "It'll happen. I know it will. Everything is coming to pass, just as I planned it."
    scene applecore-city with dissolve
    m "Now that my story's been written, all that's left to do is live it!"
        
pause
return
