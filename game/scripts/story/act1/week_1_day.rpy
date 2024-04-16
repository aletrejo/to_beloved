label week_1_day:
    play sound "/audio/pencil-write.mp3"
    scene city-day with dissolve:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}Week [week]{/size}{/font}{/color}{color=#000000}{font=JustAnotherHand-Regular.ttf}{size=200}\n Day{/size}{/font}{/color}" at truecenter with wiperight
    pause
    scene office-inside with dissolve
    play sound "/audio/office-sounds.mp3"
    play music "<from 54>/audio/happily-ever-after.mp3" fadein 1.0 volume 0.7
    m """
    Phew! I thought the gym was a workout, but my first day at the office makes it look like a promenade through a Victorian garden.

    I was thrown headfirst into the hellfire immediately after orientation.

    It seems that business is booming for the company, and it's all hands on deck.

    Literally. The slides I was assigned are due *tonight*...

    To be honest, I'm pretty nervous about finishing them in time.

    It doesn't help that I'm in this meeting instead of working on them...
    """
    stop music
    play sound "/audio/impact-slam.mp3"
    scene office-inside with vpunch:
        matrixcolor InvertMatrix(value=1.0)
    i "They're going to realize that hiring you was a mistake."
    if self_awareness >=20:
        m "(It's *only* my first day! I'm still learning the ropes.)"
        play sound "/audio/awareness-ding.mp3"
        show text "{image=ol_text}" with easeinbottom
        pause
        hide text with dissolve
        $ passed_checks +=1
    elif self_awareness<20:
        m "(I do not know what I'm doing and would like to throw myself out the window.)"

    scene office-inside
    play music "<from 20>/audio/happily-ever-after.mp3"
    m "(I just hope my boss doesn't judge me. {p}Wait, I haven't even met my boss yet.)"
    m "(That reminds me, I should be proactive about introducing myself to people!)"

    play sound "/audio/chair-sit.mp3"
    show allie-neutral with dissolve
    m "(Ah! This person who just took the seat next to me looks like they might be friendly.)"

    stop music
    play sound "/audio/impact-slam.mp3"
    play music "<from 13>/audio/cave-streams.mp3"
    scene office-inside with vpunch:
        matrixcolor InvertMatrix(value=1.0)
    i "Don't say anything weird. You want them to like you.."
    if self_awareness >=10:
        play sound "/audio/awareness-ding.mp3"
        show text "{image=ol_text}" with easeinbottom
        pause
        hide text with dissolve
        $ passed_checks +=1
        m "(Hush! You're making me anxious. Socially.)"
        stop music fadeout 1.0
        play music "<from 20>/audio/happily-ever-after.mp3"
        scene office-inside
        show allie-neutral with dissolve
        m "“Hey, I'm Menmi. This is my first meeting. Were we supposed to bring anything?”"
        m "(To my relief, they reciprocate my smile.)"
    elif self_awareness<10:
        m "“Um, do you work here?”"
        i "What are you *asking*? They're here with you. In the office. Obviously they work here."
        m """
        (Their blank stare tells me I just flubbed it.)

        I take a deep breath and try again.
        """
        stop music fadeout 1.0
        play music "<from 20>/audio/happily-ever-after.mp3"
        scene office-inside
        show allie-neutral with dissolve
        m "“Um, I mean, were we supposed to bring anything to this meeting?”"

    hide allie-neutral
    show allie-smile

    al """
    “Yeah, I'm giving a crap just by showing up.”

    “Name’s Allie.”

    “I make stuff look good. Well, the graphics anyway, not the people — that's your bag.”"""

    hide allie-smile
    show allie-neutral

    al "“Cool of you to introduce yourself. Most folks just try to skate by on icebreakers.”"
    m "“Tell me about it — I feel like I spend more time thinking about what to say than listening to other people's responses.”"

    hide allie-neutral
    show allie-smile

    al "“Ha! And by the end of it, you haven't gotten to know anyone, but it's *great* that you made up a name for your first car.”"
    m """
    “{i}Drives{/i} me crazy!”

    Allie laughs. """

    hide allie-smile
    show allie-neutral

    m """
    (Nice, we're going to get along like two peas in pea salad.)

    Somebody hushes us as the lights dim.
    """
    stop sound
    stop music fadeout 2.0

label devan_introduction:
    scene office-inside-dark with dissolve

    m "I try to look attentive as a slightly harried-looking human resources officer presents a slide on employee retention."
    "Presenter" "“So as you can see from this graph, although we're seeing a rise in new business, our current hiring rate isn't keeping pace with the work.”"
    "Presenter" "“Everyone is taking on more work, and people are burning out because of it. If we don't do something, we'll see a significant drop in retention.”"
    m "(Yikes! That explains the accelerated waterboarding, um, onboarding, they put me through.)"
    "Presenter" "“Our proposed solution is to solicit more college graduates. They're fresh and tend to want to prove themselves. More eager, less ego.”"

    stop music fadeout 1.0
    play music "/audio/devs-theme.mp3"

    d "“And that's a boon to you, is it?”"
    m "I look around to see who the smooth baritone belongs to and see a statuesque man standing in the back with his arms folded."
    show devan-neutral with dissolve
    "Presenter" "“Devan! I didn't even see you there. When did you get back from Tokyolk?”"
    $ devan_name = "Devan"
    d "“Not long ago. Hours, in fact.”"
    m """
    (His voice is so entrancing, like a talk show host who swallowed crushed velvet. An expression of placid intensity sits on his finely chiseled features.)

    (There's an untouchable quality to him.)

    (Neat.)
    """

    hide devan-neutral
    show devan-thinking

    d "“Younger folks these days have more self-respect. They don't give their labor away as freely as their forebears– and for good reason.”"

    hide devan-thinking
    show devan-neutral
    m "(A particularly bushy-tailed junior raises his hand. I catch Allie rolling their eyes beside me.)"
    "Junior" "“Actually, the research shows that workflows for younger employees are significantly more likely to be in lockstep with timelines, creating openings to circle back on ancillary requests.”"
    m "“Were those...words he was saying?”"
    al "“Don't worry about it. There's always that one guy who needs to say something to feel like he's contributing.”"

    hide devan-neutral
    show devan-thinking

    d "“How nice. Thank you.”"
    m "(Woof. That guy should've plugged in his laptop because he just got Shut Down.)"

    hide devan-thinking
    show devan-neutral

    m "Dev turns back to the presenter, his pale eyes cutting into him. The poor guy crumples in on himself like a paper straw five seconds into sitting in iced coffee."
    d "“I went over the hiring records prior to this meeting, and it seems that the organization has recruited quite a few upper-level managers in all departments.”"
    d "“So many executives can't possibly be fully billable with their current responsibilities.”"
    "Presenter" "“Are you suggesting that we give managers menial paperwork?”"

    hide devan-neutral
    show devan-thinking

    d "“I wouldn't call the work that keeps the company running *menial*, but this would be the obvious solution, wouldn't you agree?”"
    d "“It wouldn't reflect well on leadership if the juniors are toiling away while the execs are day-drinking in their corner offices.”"

    hide devan-thinking
    show devan-neutral

    d "“Appearances are *everything*, after all.”"
    "Presenter" "“I wholeheartedly agree, Devan! Your plan is...logical, no doubt. I just worry that we will experience some pushback...”"
    d "“I'm sure they'll see reason. And if they dont, well -- there are ways to persuade them.”"
    d "“Let's call this meeting adjourned, hm?”"

    stop music fadeout 1.0
    hide devan-neutral with dissolve

label after_team_meeting:
    scene office-inside with dissolve
    "Junior" "“Yeah circle back!”"
    m """
    (He looks so proud of himself.)

    (Good for him.)

    Unable to protest, the presenter wraps up and people begin to file out. I move to exit with them, but feel a tap on my shoulder.
    """

    play music "/audio/devs-theme.mp3"
    show devan-neutral with dissolve
    m "(I forget to catch my breath as my eyes catch pure glacier blue.)"

    hide devan-neutral
    show devan-smile

    d "“Of course, the suggestion applies to myself as well.”"
    m "“P-pardon?” (He's even more intimidating up close.)"
    d "“My apologies. I haven't introduced myself properly. My name is Devan. I will be your senior touchpoint.”"
    m "(It takes me a moment to register what he means.)"
    m "“Y-you're my boss?”" with vpunch

    hide devan-smile
    show devan-neutral


    d """
    “Not a big fan of that word, but yes, essentially.”

    “Please feel free to reach out to me if you have questions or need help completing any work.”
    """
    m """
    (I freeze up. Aren't bosses supposed to be distant and stern? Is this a trick?)

    (It seems too good to be true that he's offering to help. Maybe I should tell him about this project due tonight...)

    (Then again, it's my first day. I don't want to make a bad impression. I want him to *like* me, after all.)
    """
label choice_8:
    menu:
        m "What should I say?"

        "Act confident":
            c "You can't let him know you're in over your head. Fake it 'til you make it."
            m """
            (Maybe Buzzwords McBushytail was onto something...)

            (Besides, if I get used to him jumping in whenever I need help, he'll never respect me.)

            “Don't worry about me, sir. I can handle whatever you throw at me."

            Devan clasps his hands behind his back, expression as stiff as a wet blanket in winter.
            """
            d "“I see. Well, I commend your dedication, but don't overdo it. Take care, Menmi.”"
            hide dev neutral
            call after_choice_8 from _call_after_choice_8
            jump choice_8a
        "Accept his help":
            $ renpy.notify("+10 Self-Awareness")
            $ self_awareness += 10
            c "Listen to him. He's trying to tell you that he's got your back. Does this seem like the type of guy who'd try to test you?"
            m """
            (The truth is, I don't know *what* kind of guy he is, but he has made it clear that he's on my side.)

            “Thank you, sir. To be honest, I am worried about the deck due tonight...”"""

            hide devan-neutral
            show devan-smile

            m "The tip of his lips rise ever so slightly."

            d """
            “Thanks for letting me know, Menmi. It takes courage to admit that you need help.”

            “I'll see what I can do to push the deadline.”
            """
            hide dev neutral
            m "(Whew! That worked out better than I thought.)"
            call after_choice_8 from _call_after_choice_8_1
            jump choice_8b
label after_choice_8:
    stop music fadeout 1.0
    hide devan-neutral with dissolve
    hide devan-smile with dissolve
    scene office-inside:
        blur 20
    play music "<from 54>/audio/happily-ever-after.mp3" fadein 2.0 volume 0.7

    m """
    Devan leaves, taking my breath with him.

    (So that was my boss- uh, senior touchpoint?)

    (He's got that cool guy rizz for sure.)
    """
    c "Back up, girl. Boss-subordinate romances are dicey territory. Are you sure you want to explore that?"
    m "(What *is* it about power imbalances that make people go ga-ga?)"
    return

label choice_8a:
    m """
    Reinvigorated, I spend the rest of the day grinding out the deck.

    I barely make the deadline. It's not my best work, but it's something.

    I'm entirely depleted by the end of the day. I wonder if I even have the energy to meet my friend Naji.

    I can see why burnout is a problem here.

    At Allie's insistence though, I manage to rally. I have to finish out this day in style!
    """
    jump week_1_night

label choice_8b:
    m """
    Thanks to Devan, I continue my work at a leisurely pace.

    It's amazing how much more focused and creative I feel when I'm not being pressured by a deadline.

    At the end of the day, I'm ready to go out! I'm excited to see my friend Naji, who's a bartender at a hotspot downtown.
    """
    jump week_1_night
