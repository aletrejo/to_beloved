label week_1_day:
    scene image Solid("#ffc6ebff") with fade
    show text "{font=fredoka}{size=288}Week 1 \nDay{/size}{/font}" at truecenter with dissolve
    pause
    scene office-inside with dissolve
    m """
    Phew! I thought the gym was a workout, but my first day at the office makes it look like a promenade through a Victorian garden.

    I was thrown headfirst into the hellfire immediately after orientation.

    It seems that business is booming for the company, and it's all hands on deck.

    Literally. They assigned me slides that are due tonight...

    Truth be told, I'm pretty nervous about finishing them.

    It doesn't help that I'm in this meeting instead of working on them...
    """
    if self_awareness <=20:
        c "They're going to realize that hiring you was a mistake."

    m "I haven't even met my boss yet."
    m "That reminds me, I should be proactive about introducing myself to people!"
    m "Ah! This person who just took the seat next to me looks like they might be friendly."
    show allie neutral with dissolve
    if self_awareness <=20:
        c "Don't say anything weird. You want them to like you.."
    m "“Hey, I'm Menmi. This is my first meeting. Were we supposed to bring gifts?”"
    m "To my relief, they reciprocate my smile."
    al "“Yeah, I'm giving a shit just by showing up. Name’s Allie. I make stuff look good. Well, the graphics anyway, not the people — that's your bag.“"
    al "Cool of you to introduce yourself. Most folks just try to skate by on icebreakers."
    m "“Tell me about it — I feel like I spend more time thinking about what to say than listening to other people's responses.”"
    al "Ha! And by the end of it, you haven't gotten to know anyone, but it's *great* that you made up a name for your first car."
    m """
    {i}Drives{/i} me crazy!

    Allie laughs.

    Something tells me we're going to get along like two peas in pea salad.

    Somebody hushes us as the lights dim.
    """
label devan_introduction:
    scene office-inside-dark with dissolve
    m "I try to look attentive as a slightly harried-looking human resources officer presents a slide on employee retention."
    "Presenter" "So as you can see from this graph, although we're seeing a rise in new business, our current hiring rate isn't keeping pace with the work."
    "Presenter" "Everyone is taking on more work, and people are burning out because of it. If we don't do something, we'll see a significant drop in retention."
    m "Yikes! That explains the accelerated waterboarding, um, onboarding, they put me through."
    "Presenter" "Our proposed solution is to solicit more college graduates. They're fresh and tend to want to prove themselves. More eager, less ego."
    d "And that's a boon to you, is it?"
    m "I look around to see who the smooth baritone belongs to and see a statuesque man standing in the back with his arms folded."
    show dev neutral with dissolve
    "Presenter" "Devan! I didn't even see you there. When did you get back from Tokyolk?"
    $ devan_name = "Devan"
    d "Not long ago. Hours, in fact."
    m """
    His voice is so entrancing, like a talk show host who swallowed crushed velvet. An expression of placid intensity sits on his finely chiseled features.

    There's an untouchable quality to his icy aura.

    Neat.
    """
    d "Younger folks these days have more self-respect. They don't give their labor away as freely as their forebears– and for good reason"
    m "A particularly bushy-tailed junior raises his hand. I catch Allie rolling their eyes beside me."
    "Junior" "Actually, the research shows that workflows for younger employees are significantly more likely to be in lockstep with GANTT chart timeframes, creating ample opportunity to"
    "Junior" "circle back on ancillary client requests."
    m "Were those...words he was saying?"
    al "Don't worry about it. There's always that one guy who needs to say something to feel like he's contributing."
    d "How nice. Thank you."
    m """
    Woof. That guy should've plugged in his laptop because he just got Shut Down.

    Dev turns back to the presenter, his pale eyes cutting into him. The poor guy crumples in on himself like a paper straw five seconds into sitting in iced coffee.
    """
    d "I went over the hiring records prior to this meeting, and it seems that the organization has recruited quite a few upper-level managers in all departments."
    d "So many executives can't possibly be fully billable with their current responsibilities."
    "Presenter" "Are you suggesting that we give managers menial paperwork?"
    d "I wouldn't call the work that keeps the company running menial, but this would be the obvious solution, wouldn't you agree?"
    d "The managers will know how to do the day-to-day work, if they are as experienced as they should be."
    d "Besides, it wouldn't reflect well on leadership if the juniors are toiling away while the execs are day-drinking in their corner offices."
    "Presenter" "I wholeheartedly agree, Devan! Your plan is...logical, no doubt. I just worry that we will experience some pushback..."
    d "Then we will push back harder. We're all busy people. Let's call this meeting adjourned, hm?"

label after_team_meeting:
    scene office-inside with dissolve
    "Junior" "Yeah circle back!"
    m """
    He looks so proud of himself. Good for him.

    Unable to protest, the presenter wraps up and people begin to file out. I move to exit with them, but feel a tap on my shoulder.
    """
    show dev neutral with dissolve
    m "I forget to catch my breath as my eyes catch pure glacier blue."
    d "Of course, the suggestion applies to myself as well."
    m "“P-pardon?” He's even more intimidating up close.”"
    d "My apologies. I haven't introduced myself properly. My name is Devan. I will be your senior touchpoint."
    m "It takes me a moment to register what he means."
    m "“Y-you're my boss?”" with vpunch
    d """
    Not a big fan of that word, but yes, essentially.

    Please feel free to reach out to me if you have questions or need help completing any work.
    """
    m """
    I'm frozen in place. Aren't bosses supposed to be distant and stern? Is this a trick?

    It seems too good to be true that he's offering to help. Maybe I should tell him about this project due tonight...

    Then again, it's my first day. I don't want to make a bad impression. I want him to *like* me, after all.
    """
label choice_8:
    menu:
        m "What should I say?"

        "Act confident":
            c "You can't let him know you're in over your head. Fake it 'til you make it."
            m """
            Maybe Buzzwords McBushytail was onto something...

            Besides, if I get used to him jumping in whenever I need help, he'll never respect me.

            “Don't worry about me, sir. I can handle whatever you throw at me."

            Devan clasps his hands behind his back, expression as stiff and blank as a chalkboard.
            """
            d "I see. Well, I commend your dedication, but don't overdo it. Take care, Menmi."
            hide dev neutral
            call after_choice_8
            jump choice_8a
        "Accept his help":
            $ renpy.notify("+10 Self-Awareness")
            $ self_awareness += 10
            c "Listen to him. He's trying to tell you that he's got your back. Does this seem like the type of guy who'd try to test you?"
            m """
            The truth is, I don't know *what* kind of guy he is, but he has made it clear that he's on my side.

            “Thank you, sir. To be honest, I am worried about the deck due tonight...”

            The tip of his lips rise ever so slightly.
            """
            d """
            Thanks for letting me know, Menmi. It takes courage to admit that you need help. Thank you for your trust.

            I'll see what I can do to push the deadline.
            """
            hide dev neutral
            m "Whew! That worked out better than I thought."
            call after_choice_8
            jump choice_8b
label after_choice_8:
    m """
    Devan leaves, taking my breath with him.

    So that was my boss- uh, senior touchpoint?

    He's got that cool guy rizz for sure.
    """
    c "Back up, girl. Boss-subordinate romances are dicey territory. Are you sure you want to explore that?"
    m "What *is* it about power imbalances that make people go ga-ga?"
    return

label choice_8a:
    m """
    Reinvigorated, I spend the rest of the day grinding out the deck.

    I barely make the deadline. It's not my best work, but it's something.

    I'm entirely depleted by the end of the day. I wonder if I even have the energy to meet my bartender friend Naji.

    I can see why burnout is a problem here.

    At Allie's insistence though, I manage to rally. I have to finish out this day in style!
    """
    jump week_1_night

label choice_8b:
    m """
    Thanks to Devan, I continue my work at a leisurely pace.

    It's amazing how much more focused and creative I feel when I'm not being pressured by a deadline.

    At the end of the day, I'm ready to go out! I'm excited to see my friend Naji at his bar.
    """
    jump week_1_night
