# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character ("Menmi", color='#F52088')
define c = Character ("Menmi's Conscience", color='#750F41')
define n = Character ("Naji", color='#E59A34')
define j = Character ("Joule", color='#0064C2')
define d = Character ("Devan", color='#800DCD')

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show menmi-apartment-sunset
    with vpunch


    # These display lines of dialogue.

    m "Oof. That’s the last one!"

    m "I didn’t expect to be carrying so much stuff from my parents' place up to my new apartment"

    m "So {i}this{/i} is what they mean by 'walk-up.' Ooooooooohhh..."

    m "But, hey! I got a steal on this place with rent! It’s more shoebox than studio, but it’s Home – here in Applecore City!"

    show applecore-city
    with dissolve

    m "Isn’t it just the picture of perfection? The staggering skyscrapers, the constant commotion of the crowds, the mystery odors of human body gumbo."

    m "My life starts now. Look out world, Menmi is officially entering her City Biddy Era."

    n "This is a test"


    return
