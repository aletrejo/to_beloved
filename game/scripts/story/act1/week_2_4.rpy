label week_2_4:
    play sound "/audio/pencil-write.mp3"
    scene city-morning with fade:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}Week 2{/size}{/font}{/color}{color=#000000}" at truecenter with wiperight
    #have Week # change depending on number of previous loops
    pause

    play music "<from 9>/audio/happily-ever-after.mp3" fadein 0.5
    scene menmi-apartment-morning with dissolve

    m "Good morning MenME! I'm feeling refreshed and ready for the week ahead!"

    #insert Insight-exclusive dialogue

label gym_auto:
    scene gym-inside with fade
    default gym_options = ['gym_1', 'gym_2', 'gym_3','gym_4','gym_5','gym_6','gym_7','gym_8','gym_9']
    $ gym_chosen = renpy.random.choice(gym_options)
    if gym_chosen == 'gym_1':
        m " workouts are working out just fine."
    if gym_chosen == 'gym_2':
        m "My morning gym routine is kicking me in the tighty whities (that’s my butt)!"
    if gym_chosen == 'gym_3':
        m "With every push-up at the gym, I get closer to my final {b}form{/b}."
    if gym_chosen == 'gym_4':
        m "These workouts are literal exercises in endurance. I just gotta keep my body on my mind and my mind on the man bodies."
    if gym_chosen == 'gym_5':
        m "Making gains or making eyes? I'm a multitasker."
    if gym_chosen == 'gym_6':
        m "It’s always a pleasure to witness the fitness of the morning gym crowd."
    if gym_chosen == 'gym_7':
        m "Joule’s head pats always reinvigorate me to work hard!"
    if gym_chosen == 'gym_8':
        m "My AM gym routine gets my heart rate {i}going!{/i}"
    if gym_chosen == 'gym_9':
        m "I'm more familiar with ripped bodices than ripped bodies, but I'm giving it my best at the gym!"

label work_auto:
    scene office-inside with fade
    default work_options = ['work_1', 'work_2','work_3','work_4','work_5','work_6','work_7','work_8','work_9']
    $ work_chosen = renpy.random.choice(work_options)
    if work_chosen == 'work_1':
        m "Work is hectic, but I make it work."
    if work_chosen == 'work_2':
        m """
        Listened to my coworkers complain to me today.

        It's nice to feel like I can help by lending an ear.

        Who said work couldn't be community service? """
    if work_chosen == 'work_3':
        m "I’ve got a ton going on at work, but I need money to get the honey. Do your best, MenME!"
    if work_chosen == 'work_4':
        m "Everyone at the office is so busy, but I appreciate that Devan always makes time to check in with me."
    if work_chosen == 'work_5':
        m """I bought a plant to decorate my desk.
        It's not real, but it's good practice for the future (probably)."""
    if work_chosen == 'work_6':
        m "Work is about as fun as you'd expect. Let's get that dread, baby."
    if work_chosen == 'work_7':
        m "I hardly see Devan at the office, but his brief appearances always makes my heart hammer like the constant construction going on outside.

        Oh my gosh what are they even working on?"
    if work_chosen == 'work_8':
        m """I'm really starting to feel at home at work!
        Because I'm there 10 hours a day!"""
    if work_chosen == 'work_9':
        m """
        Sometimes I entertain myself during work by thinking about the personalities of Office Apps.

        Would Dev be more of a Powerpoint or a Word?

        Asking some seriously important questions here."""


label lounge_auto:
    scene lounge-inside with fade
    default lounge_options = ['lounge_1', 'lounge_2','lounge_3','lounge_4','lounge_5','lounge_6','lounge_7','lounge_8','lounge_9']
    $ lounge_chosen = renpy.random.choice(lounge_options)
    if lounge_chosen == 'lounge_1':
        m "It's nice to gather at the William Collins' at the end of the day. The staff almost feels like family!"
    if lounge_chosen == 'lounge_2':
        m """The lounge is usually quiet on weeknights, which makes it harder to get the goss from Naji.

        Guess we'll have to make our own drama *wink*"""
    if lounge_chosen == 'lounge_3':
        m "Naji sometimes gives me free drinks after work. It's nice to have friends in high places!"
    if lounge_chosen == 'lounge_4':
        m """Either there are a disproportionately high number of hotties frequenting the William Collins

        or I'm drunk.

        Probably both."""
    if lounge_chosen == 'lounge_5':
        m """The buzz of the cocktail lounge at night makes me feel like *anything* can happen.

        Celebrity sighting? Designer drugs? The birth of a throuple? I'm there for it!"""
    if lounge_chosen == 'lounge_6':
        m "The days are long, but the drinks Naji makes at the lounge go down as easily as a weekend train. ZING!"
    if lounge_chosen == 'lounge_7':
        m "I've made some new friends at the lounge! What's a whippet?"
    if lounge_chosen == 'lounge_8':
        m """Sometimes I bring coworkers to the lounge, where the atmosphere is always *so* inappropriately romantic.

        I hope nobody gets the *wrong* idea...hehe."""
    if lounge_chosen == 'lounge_9':
        m """Somebody at the William Collins told me they want to see me gobble a glizzy.

        What's it mean?

        Why'd Naji throw them out?"""

label after_week:
    scene city-night with fade
    m """Phew! What a week.

    “Now I can look forward to my weekend plans.”"""

    show allie-smile with dissolve
    al "“Ha, as if you haven't been looking forward to them all week?”"
    m """“That's true. We all need something to keep us going."

    "Do you have anything planned for the weekend, Allie?”"""

    hide allie-smile
    show allie-neutral

label allie_response:
    default allie_response_options = ['allie_1','allie_2','allie_3','allie_4','allie_5','allie_6','allie_7','allie_8','allie_9','allie_10','allie_11','allie_12','allie_13', 'allie_14']
    $ allie_chosen = renpy.random.choice(allie_response_options)
    if allie_chosen == 'allie_1':
        al """
        “Me? I'm going to a friend's birthday party.”

        “Though I'm skeptical that C-section babies are actually "born"” """
    if allie_chosen == 'allie_2':
        al "“I'm going to my biannual clown school reunion.”"
    if allie_chosen == 'allie_3':
        al """“Yeah, I'm going on a hike with my sensei up Bearclaw Mountain.”

        “Do you know where I can buy a weighted blanket?”"""
    if allie_chosen == 'allie_4':
        al """
        “I think I'll check out that 'anti-silent rave' going on downtown.”

        “It's like a silent rave except everyone unplugs their headphones at the same time and plays whatever they're listening to from their phones.” """
    if allie_chosen == 'allie_5':
        al "“I have relatives in town who are dying to see the bathrooms in Rye Bread Park. Tourists, am I right?”"
    if allie_chosen == 'allie_6':
        al """“I've gotta persuade squirrels to eat halal meat in Cilantro Park.”

        “It's for an art installation. About ethics.”"""
    if allie_chosen == 'allie_7':
        al """“I'm checking out that new high concept restaurant, {i}Food For Thought{/i}.”

        “Eating is optional.”"""
    if allie_chosen == 'allie_8':
        al """
        “I'm going to play skee-ball with my psychiatrist.”

        “It's part of my exposure therapy. Healing is hard work!”"""
    if allie_chosen == 'allie_9':
        al """
        “I've got a little home improvement project going on.”

        “That closet altar isn't going to anoint itself!” """
    if allie_chosen == 'allie_10':
        al """“Yeah, I've gotta going to wash my hair... in a swimming pool.”

        “It's cheaper than a salon bleach and twice as fun!”"""
    if allie_chosen == 'allie_11':
        al "“Grocery shopping! Instant borscht, kettlecorn, half-baked bread — you know, pantry staples.”"
    if allie_chosen == 'allie_12':
        al "“It's the solstice this weekend, so I'm just going to stay in...for safety.”"
    if allie_chosen == 'allie_13':
        al "“I'm volunteering at the cockroach shelter. The clients are tough.”"
    if allie_chosen == 'allie_14':
        al "“I'm working at the wax museum. They're short on hands.”"

    m "Allie always has something interesting going on!"

    if self_awareness <=50:
        stop music
        play sound "/audio/impact-slam.mp3"
        scene city-night with vpunch:
            matrixcolor InvertMatrix(value=1.0)
        show allie-neutral at truecenter:
            matrixcolor InvertMatrix(value=1.0)
        i """ Wish you could be half as cool.

        Why does she even hang out with you, Dullsy Duck?"""

        m "*laughs nervously*"

        scene city-night with hpunch
        show allie-neutral
        play music "<from 13>/audio/happily-ever-after.mp3"

    m "“Can't wait to hear about it on Monday!”"