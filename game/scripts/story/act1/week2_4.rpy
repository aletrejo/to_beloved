label week 2_4:
    play sound "/audio/pencil-write.mp3"
    scene city-morning with dissolve:
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
    play sound "/audio/office-sounds.mp3"
    play music "<from 54>/audio/happily-ever-after.mp3" fadein 1.0 volume 0.7
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
