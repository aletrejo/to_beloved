label week_2_4:
    play sound "/audio/pencil-write.mp3"
    hide screen open_planner
    hide screen open_insights
    scene city-morning with fade:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}Week [week]{/size}{/font}{/color}{color=#000000}" at truecenter with wiperight
    play music "<from 9>/audio/happily-ever-after.mp3" fadein 0.5
    scene menmi-apartment-morning with dissolve
    show screen open_planner
    show screen open_insights

    m "Good morning MenME! I'm feeling refreshed and ready for the week ahead!"

    while dialogue_matches:
        $ dialogue_matches.pop()

    default unlocks_dialogue = ["I have to be better about that", "I need to be a better person", "I wish I could redo some decisions", "I keep second-guessing myself and thinking about other possibilities...", "I'll learn from my mistakes"]
    default dialogue_matches = []
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
        scene menmi-apartment-morning with vpunch:
            matrixcolor InvertMatrix(value=1.0)
        i "You'll have to do better this week to make up for your mistakes."
        scene menmi-apartment-morning
        m "I'll work hard to put myself back on track!"

    $ unlocks_dialogue = ["Things might not work out, but that's a natural part of life", "I'm going to have faith and enjoy the ride", "I think I just have to learn to accept that I don't know everything, but...", "They may have shaped my past, but the future isn't set in stone."]
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
        m "Whatever the future holds, I'll try to remain open so I can enjoy every moment as they come."

    $ unlocks_dialogue = ["It's all coming true like I planned", "It's nice to know that I'm capable of achieving happiness for myself", "I believe in myself"]
    $ dialogue_matches = check_for_matches(unlocks_dialogue, bathtime_1_choices)
    if len(dialogue_matches) > 0:
        show screen insight(dialogue_matches)
        m "Alright! I'm satisfied with my progress last week. I just have to keep it up, and I'll be living out my dreams in no time."
        scene menmi-apartment-morning with vpunch:
            matrixcolor InvertMatrix(value=1.0)
        i "Harder. Better. Faster. Stronger. You've got a lot working against you. That's why you have to push yourself on the path to success!"
        scene menmi-apartment-morning


label gym_auto:
    scene gym-inside with fade
    default gym_options = ['gym_1', 'gym_2', 'gym_3','gym_4','gym_5','gym_6','gym_7','gym_8','gym_9']
    $ gym_chosen = renpy.random.choice(gym_options)
    if gym_chosen == 'gym_1':
        m "Workouts are working out just fine."
        $ gym_text="Workouts are working out just fine."
    if gym_chosen == 'gym_2':
        m "My morning gym routine is kicking me in the tighty whities (that's my butt)!"
        $ gym_text="My morning gym routine is kicking me in the tighty whities (that's my butt)!"
    if gym_chosen == 'gym_3':
        m "With every push-up at the gym, I get closer to my final {b}form{/b}."
        $ gym_text="With every push-up at the gym, I get closer to my final {b}form{/b}."
    if gym_chosen == 'gym_4':
        m "These workouts are literal exercises in endurance. I just gotta keep my body on my mind and my mind on the man bodies."
        $ gym_text="These workouts are literal exercises in endurance. I just gotta keep my body on my mind and my mind on the man bodies."
    if gym_chosen == 'gym_5':
        m "Making gains or making eyes? I'm a multitasker."
        $ gym_text="Making gains or making eyes? I'm a multitasker."
    if gym_chosen == 'gym_6':
        m "It's always a pleasure to witness the fitness of the morning gym crowd."
        $ gym_text="It's always a pleasure to witness the fitness of the morning gym crowd."
    if gym_chosen == 'gym_7':
        m "Joule's head pats always reinvigorate me to work hard!"
        $ gym_text="Joule's head pats always reinvigorate me to work hard!"
    if gym_chosen == 'gym_8':
        m "My AM gym routine gets my heart rate {i}going!{/i}"
        $ gym_text="My AM gym routine gets my heart rate {i}going!{/i}"
    if gym_chosen == 'gym_9':
        m "I'm more familiar with ripped bodices than ripped bodies, but I'm giving it my best at the gym!"
        $ gym_text="I'm more familiar with ripped bodices than ripped bodies, but I'm giving it my best at the gym!"
    $ gym_options.remove(gym_chosen)

label work_auto:
    scene office-inside with fade
    default work_options = ['work_1', 'work_2','work_3','work_4','work_5','work_6','work_7','work_8','work_9']
    $ work_chosen = renpy.random.choice(work_options)
    if work_chosen == 'work_1':
        m "Work is hectic, but I make it work."
        $ office_text="Work is hectic, but I make it work."
    if work_chosen == 'work_2':
        m """
        Commiserated with my coworkers today.

        Yeah! Team bonding!
        """
        $ office_text="Commiserated with my coworkers today. Yeah! Team bonding!"
    if work_chosen == 'work_3':
        m "I've got a ton going on at work, but I need money to get the honey. Do your best, MenME!"
        $ office_text="I've got a ton going on at work, but I need money to get the honey. Do your best, MenME!"
    if work_chosen == 'work_4':
        m "Everyone at the office is so busy, but I appreciate that Devan always makes time to check in with me."
        $ office_text="Everyone at the office is so busy, but I appreciate that Devan always makes time to check in with me."
    if work_chosen == 'work_5':
        m """I bought a plant to decorate my desk.
        It's not real, but it's good practice for the future (probably)."""
        $ office_text="I bought a plant to decorate my desk. It's not real, but it's good practice for the future (probably)."
    if work_chosen == 'work_6':
        m "Work is about as fun as you'd expect. Let's get that dread, baby."
        $ office_text="Work is about as fun as you'd expect. Let's get that dread, baby."
    if work_chosen == 'work_7':
        m "I hardly see Devan at the office, but his brief appearances always makes my heart hammer like the constant construction going on outside.

        Oh my gosh what are they even working on?"
        $ office_text="I hardly see Devan at the office, but his brief appearances always makes my heart hammer like the construction going on outside."
    if work_chosen == 'work_8':
        m """I'm really starting to feel at home at work!
        Because I'm there 10 hours a day!"""
        $ office_text="I'm really starting to feel at home at work! Because I'm there 10 hours a day!"
    if work_chosen == 'work_9':
        m """
        Sometimes I entertain myself during work by thinking about the personalities of Office Apps.

        Would Dev be more of a Powerpoint or an Excel?

        Personally, I identify as Calendar.

        Asking some seriously important questions here."""

        $ office_text="Sometimes I entertain myself during work by thinking about the personalities of Office Apps. Personally, I identify as Calendar."

    $ work_options.remove(work_chosen)


label lounge_auto:
    scene lounge-inside with fade
    default lounge_options = ['lounge_1', 'lounge_2','lounge_3','lounge_4','lounge_5','lounge_6','lounge_7','lounge_8','lounge_9']
    $ lounge_chosen = renpy.random.choice(lounge_options)
    if lounge_chosen == 'lounge_1':
        m "It's nice to gather at the William Collins' at the end of the day. The staff almost feels like family!"
        $ lounge_text= "It's nice to gather at the William Collins' at the end of the day. The staff almost feels like family!"
    if lounge_chosen == 'lounge_2':
        m """The lounge is usually quiet on weeknights, which makes it harder to get the goss from Naji.

        Guess we'll have to make our own drama *wink*"""
        $ lounge_text= "The lounge is usually quiet on weeknights, which makes it harder to get the goss from Naji. Guess we'll have to make our own drama"
    if lounge_chosen == 'lounge_3':
        m "Naji sometimes gives me free drinks after work. It's nice to have friends in high, um {w}drunk places!"
        $ lounge_text= "Naji sometimes gives me free drinks after work. It's nice to have friends in high, um {w}drunk places!"
    if lounge_chosen == 'lounge_4':
        m """Either there are a disproportionately high number of hotties frequenting the William Collins

        or I'm drunk.

        I'm drunk."""
        $ lounge_text= "Either there are a disproportionately high number of hotties frequenting the William Collins. Or I'm drunk."
    if lounge_chosen == 'lounge_5':
        m """The buzz of the cocktail lounge at night makes me feel like *anything* can happen.

        Celebrity sighting? Designer drugs? The birth of a throuple? I'm there for it!"""
        $ lounge_text= "The buzz of the cocktail lounge at night makes me feel like *anything* can happen."
    if lounge_chosen == 'lounge_6':
        m "The days are long, but the drinks Naji makes at the lounge go down as easily as a weekend train. ZING!"
        $ lounge_text= "The days are long, but the drinks Naji makes at the lounge go down as easily as a weekend train. ZING!"
    if lounge_chosen == 'lounge_7':
        m "I've made some new friends at the lounge! What's a whippet?"
        $ lounge_text= "I've made some new friends at the lounge! What's a whippet?"
    if lounge_chosen == 'lounge_8':
        m """Sometimes I bring coworkers to the lounge, where the atmosphere is always *so* inappropriately romantic.

        I hope nobody gets the *wrong* idea...hehe."""
        $ lounge_text= "Sometimes I bring coworkers to the lounge, where the atmosphere is always *so* inappropriately romantic."
    if lounge_chosen == 'lounge_9':
        m """Somebody at the William Collins told me they want to see me gobble a glizzy.

        What's it mean?

        Why'd Naji throw them out?"""
        $ lounge_text= "Somebody at the William Collins told me they want to see me gobble a glizzy. What's it mean? Why'd Naji throw them out?"
    $ lounge_options.remove(lounge_chosen)

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
        al """“I'm helping to organize a triathlon for dogs.”

        “No, the dogs won't be competing. They're spectating.”
        """
    if allie_chosen == 'allie_3':
        al """“Yeah, I'm going on a hike with my chess sensei up Bearclaw Mountain.”

        “Do you know where I can buy a weighted blanket?”"""
    if allie_chosen == 'allie_4':
        al """
        “I think I'll check out that 'anti silent rave' going on downtown.”

        “It's just like a regular rave except everyone plays their own music from their phone out loud at the same time.” """
    if allie_chosen == 'allie_5':
        al "“I have relatives in town who are *dying* to free climb a skyscraper. Tourists, am I right?”"
    if allie_chosen == 'allie_6':
        al "“I'm going hunting for the Jersey Devilled Egg.”"
    if allie_chosen == 'allie_7':
        al """“I'm checking out that new high concept restaurant, {i}Food For Thought{/i}.”

        “The menu is a series of poems written by Emory DeSassi, and each course is named after a different Middle Eastern philosopher.”"""
    if allie_chosen == 'allie_8':
        al """“I'm going to play skee-ball with my high school guidance counselor.

        Gotta get good enough to join a league”"""
    if allie_chosen == 'allie_9':
        al """
        “I've got a little home improvement project going on.”

        “That closet altar isn't going to anoint itself!” """
    if allie_chosen == 'allie_10':
        al """“Yeah, I've gotta going to wash my hair... in a swimming pool.”

        “It's cheaper than a salon bleach and twice as fun!”"""
    if allie_chosen == 'allie_11':
        al "“Grocery shopping! Raw turkey breast, kettlecorn, half-baked bread — you know, pantry staples.”"
    if allie_chosen == 'allie_12':
        al "“It's the Thanksgiving's Day Parade this weekend, so I'm just going to stay in...for safety reasons.”"
    if allie_chosen == 'allie_13':
        al "“I'm volunteering at the cockroach shelter. The clients are tough.”"
    if allie_chosen == 'allie_14':
        al "“I'm working at the wax museum. They're short on hands.”"

    m "Allie always has something interesting going on!"
    $ allie_response_options.remove(allie_chosen)

    if self_awareness <=40:
        stop music
        play sound "/audio/impact-slam.mp3"
        scene city-night with vpunch:
            matrixcolor InvertMatrix(value=1.0)
        show allie-neutral at truecenter:
            matrixcolor InvertMatrix(value=1.0)
        i """ Wish you could be half as cool.

        Why do they even hang out with you, Dullsy Duck?"""

        m "*laughs nervously*"

        scene city-night with hpunch
        show allie-neutral
        play music "<from 13>/audio/happily-ever-after.mp3"

    m "I'm lucky to have such an interesting friend!"
    hide screen open_insights
    hide screen open_planner

    if week == 5:
        jump act_1_climax
    elif weekend_event == "bathtime":
        jump week_2_4_bathtime
    elif weekend_event == "going_out":
        if n1==False:
            jump naji_date_1

        elif n2==True:
            jump naji_date_3

        elif n1==True and n2==False:
            jump naji_date_2
