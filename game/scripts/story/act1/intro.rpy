# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character ("Menmi", color='#F52088')
define c = Character ("Menmi's Conscience", color='#750F41')
define n = Character ("Naji", color='#E59A34')
define j = Character ("Joule", color='#0064C2')
define d = Character ("Devan", color='#800DCD')
define u = Character ("Delivery Guy", color="#6c431a")

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

    show ups

    u "I've got a package for Ms. Menmi."

    m """
    Yes, that's me!

    As he hands me the package, I feel electricity sparking at the brief synapse between our fingers.

    Is this...chemistry?
    """

    scene menmi-apartment-door:
        blur 24

    show ups:
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

label tutorial:
    screen conscience():
        text "Tutorial"
    
    call screen conscience with dissolve

return
