label joule_date_1:
    play sound "/audio/pencil-write.mp3"
    hide screen open_planner
    hide screen open_insights
    scene city-morning with fade:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}Week [week]{/size}{/font}{/color}{color=#000000}{color=#000000}{font=JustAnotherHand-Regular.ttf}{size=200}\n Weekend!{/size}{/font}{/color}" at truecenter with wiperight
    pause

    play music "<from 9>/audio/happily-ever-after.mp3" fadein 0.5
    scene gym-inside with dissolve

    m """
    Today's my first session with my very own personal trainer! 

    It's still early but I'm already abuzz with nerves.

    (Sure is chilly in the gym...)

    The thought of *my* limp noodle of a body being so closely scrutinized by someone who could probably break a bench on his abs alone is making me feel...kind of bad.
            
    (Alright! Crunch time.)

    I'm preparing to do six hundred sit-ups in 5 minutes when the gym door swings open.

    """

    play sound "/audio/impact-slam.mp3"
    show joule-neutral with vpunch
    j "“Nice to see you again, Menmi.”"
   
    m """
    (AAaaaa!!! He surprised me. {w} Oh no, I'm still on the floor. {w} What do I do?)

    (From this angle, Joule looks gargantuan...)"""

    hide joule-neutral
    stop music
    play music "<from 13>/audio/cave-streams.mp3"
    play sound "/audio/impact-slam.mp3"
    scene gym-inside with vpunch:
        blur 24
        matrixcolor InvertMatrix(value=1.0)

    m "And being in the same space as my encounter with the Behemoth is giving me flashbacks of the unwanted variety."

    show behemoth with dissolve
    play sound "/audio/monster-growl.mp3"

    
    m """
    (The air is so cold, and I'm hyper-aware of how uncovered my arms are...)

    (Am I inviting attention? {w} Isn't that what I want?)

    ({i}Don't look at me.)

    """

    hide behemoth with dissolve

    i "Stop acting so stupid, Menmi."

    if self_awareness>=50:
        scene gym-inside:
        c "It's OK. You're safe. That was then. Stay in the here and now."
        m "(It's easy to stay grounded when you're on the ground!)"
         play sound "/audio/awareness-ding.mp3"
        show text "{image=ol_text}" with easeinbottom
        pause
        hide text with dissolve
        $ chosen_sticker = renpy.random.choice(available_stickers)
        image sticker_won = "stickers/sticker-[chosen_sticker].png"
        show sticker_won at rotation:
            xpos 0.5
            ypos 0.5
        show text "{image=stickertext}" with dissolve:
            xpos 0.5
            ypos 0.5
        pause
        hide sticker_won
        hide text
        show screen place_sticker(chosen_sticker)
        $ available_stickers.remove(chosen_sticker)
        pause
        hide screen place_sticker
        $ passed_checks +=1

    elif self_awareness<50:
        m "OK.{p} Since I told myself to stop acting stupid, I will. {p}Easy as that."
    play sound "/audio/impact-slam.mp3"
    scene gym-inside with vpunch:
        blur 24
        matrixcolor InvertMatrix(value=1.0)
        m "(No it's not! What useless advice!)"
        scene gym-inside


    m """
    A soft wheeze brings me back to reality.

    Joule's cheeks are puffed out like he's trying not to laugh."""

    show joule-smile with dissolve
    j "“Need some help?”"

    hide joule-smile
    show joule-smile with dissolve at truecenter:
        zoom 1.5

    m """He holds out a wide palm to me, and I take it. 

    In one smooth motion, I'm back on my feet, body levelled in perfect balance. {w} I'm so amazed by how well he controlled the lift that I almost forget about how close he's standing.

    Joule lets go of my hand."""

    hide joule-smile
    show joule-neutral with dissolve

    j "“Doing a warm-up, huh? Good, I like the hustle.”"
    m """{i}He complimented me! {w} How do I get him to do it again?

    “I...I was just so excited to get started!”

    """

    hide joule-neutral
    show joule-smile

    j "“That's great. Strong people know what they want in life and go for it.”"
    m "{i}I could go for anything as long as you're the one telling me to, Joule."

    hide joule-smile
    show joule-neutral

    j "“That's why I want to start today by talking about your personal fitness goals.”"

    m "He takes out a clipboard holding a printout with the {i}Planet Figness{i} logo on it."

    m """I sneak a peek over the top of the clipboard, watching Joule inscribe my name in one fine motion.

    {i} Menmi. 

    His handwriting is surprisingly delicate. {w} It's almost strange to see such precise curves come out of such sturdy, calloused hands.

    My breath catches.{w} It feels kind of intimate. Like I'm seeing something secret. 

    When I look up, Joule is gazing at me with his full attention.

    """
    
    j "“An assessment of your health history and habits will help me understand what to look out for so I can create a personalized training regimen suited to your needs.”"

    m """

    I've never had anyone pay such careful attention to me before.{w} It's a flattering feeling, having someone devote their expertise to you.

    “Sure! Ask me anything.” """

    j "“Great. Let's start with the most important one - your goals. What do you want to get out of your training program?”"

    m"""

    Does "getting your personal trainer to fall in love with you" qualify as a personal fitness goal?

    Can I say that? {w} I cannot say that. {w} Out loud, at least.

    And, if I'm being honest with myself, it's not my *only* goal.
    """

    label choice_12j:
        menu: 
            m "How should I answer Joule's question about my fitness goals?"

            "“I just want to feel good and have fun.”":
                c "Physical health aside, moving your body is a nice way to distance and distract yourself from the constant roil of anxious thoughts bouncing around in here."
                $ renpy.notify("+5 Self-Awareness")
                $ self_awareness += 5
                m """
                {i}What anxious thoughts?{w} Should I be worried that I'm having anxious thoughts?

                {i}Although I guess I *did* stop thinking about how weird I was feeling after I started doing crunches.

                {i}It'd be nice if I could just let loose and feel good in my body.
                """

                hide joule-neutral
                show joule-smile

                j "“Cool! Exercise *is* really fun!”"

                hide show-smile
                show joule-neutral

                j "“There is a significant body of evidence that shows how regular exercise can have a host of benefits to mental health, including reduced stress and improved mood, sleep and even self-esteem.”"

                hide joule-neutral
                show joule-thinking

                j "“It's just that... Hmmm...”"

                hide joule-thinking
                show joule-awkward

                j "“You don't really need a personal trainer to do that, do you?”"
                m """{i}That's true...if my goal is to have fun, having someone monitor my every move and tellimg me what to do doesn't exactly seem like a good time.
 
                {i} Ugh, why do I feel like I've just given the wrong answer? {w}But maybe I'm just not saying what I mean.

                What do I do?
                """
                    label choice_12j_a_followup:
                        menu: 
                            m "Should I explain myself?"

                            "Yes":
                                c "You deserve to be understood. {w} And this guy has proven to you before that he's capable of listening."
                                m """{i}Yeah, I should be honest with Joule...I mean he *asked*.

                                {i}Even if the thought of being vulnerable kind of makes my skin crawl.

                                """
                                hide joule-awkward
                                show joule-neutral
                                m """Yeah, actually...{w}I've been feeling pretty bad about myself. {w}And I want it to stop. {w} C-can you help me?

                                {i} Ugh, that was kind of tough to get out...{w}I'm not sure if I just threw up or if I want to throw up.

                                """
                                hide joule-neutral
                                show joule-sad
                                m """{i}Great...{p}Joule's looking at me like I'm some sad baby with a dirty diaper that I can't clean for myself."""
                                hide joule-sad
                                show joule-smile
                                m "{i}But then his face lifts into a soft smile."
                                j "“Yeah...{w}I know what you mean.”"
                                $ joule_relationship +=10
                                $ renpy.notify("Joule feels closer to you!")
                                j """“I've been there myself...{w}Like you feel disconnected from your body. Like you'd rather run or hide than exist and be seen as you are.”

                                “Don't worry. I can help you feel more confident about yourself. {w}Confidence comes from within, but that doesn't mean it always starts there.”
                                """
                                hide joule-smile
                                show joule-neutral
                                j "“Thanks for putting your faith in me, Menmi.{w} I won't let you down.”"
                            "No, just drop it.":
                                c "He knows what he's talking about...better than you, anyway."
                                m """{i}It was silly of me to give such a flippant answer.

                                I thought it would make me sound like a cool party girl, I guess.

                                “Yeah, I guess...I don't really know what I want out of this.”

                                """
                                hide joule-neutral
                                show joule-smile
                                j "“That's alright.{w}You don't have to have everything figured out right now.”"
                                hide joule-smile
                                show joule-neutral
                                j"“Let's say for now...you just want to get stronger.{w}That sound fair enough?”"
                                m "{i}Why do I feel like he means something more by that...?"
            "“I want to be the most jacked ever.”":
                c "Why shoot for a goal if you aren't going to shoot for the top?"
                m """That's right - I've gotta prove to Joule that Menmi's not the type of girl to do anything halfway.

                Besides, I don't ever want to be made to feel as scared as that water-hogging jerk made me feel on my first day!

                “I want to be strong!”

                """
                $ renpy.notify("+5 Self-Awareness")
                $ self_awareness += 5
                
                hide joule-neutral
                show joule-smile

                j """
                “Awesome. I'm glad you took what I said about defending yourself to heart.”

                “I promise, you're going to feel empowered when we're done because...well, you'll be powerful!”

                """

                hide joule-smile
                show joule-wink
                j """

                “I like that you're so driven, Menmi. {w}It's important to have a sense of direction in life.”

                “It's like having a strong core.{w} Having a goal to work towards will help support you in almost every other aspect of your workout - and life.”

                “And that's HARD.{w}CORE.”

                """

                m "As if to emphasize his point, Joule raps his knuckles against his abs in sincere conviction."

                j """

                “But you'll need guidance. Physical strength might not be your usual domain, but we can help you get there.”

                “I'll develop a training plan that'll check every box -- targeted strength training, cardio, HIIT, you name it.”
                """

                m "“Wow, Joule. You'd really do all that for me?”"

                j "Of course. I've got your back.{w}And your core. {w}And your arms.{w} Oh, and can't forget legs..."

                $ joule_relationship +=10
                $ renpy.notify("Joule feels closer to you!")

                hide joule-wink with dissolve

            "“I want to look hot so that everyone will love me.”":
                c "Hotness starts from within. {w}If you can't answer this question with complete, transparent confidence, how are you ever going to be a baddie?"
                m "Why would I even lie about this? It's true. {w}How am I going to attract the man of my dreams looking like *myself*?"

                hide joule-neutral
                show joule-laugh
                j "“Hahaha. I appreciate the honesty. A lot of people don't have the guts to admit to that, even if it is the case.”"

                hide joule-laugh
                show joule-neutral

                j """“Many deny it out of an idealized sense of fairness...{w}but the harsh truth is that the world we live in is shallow.”

                “People make snap judgments about each other all the time. {w} And usually, the first thing they learn about you is the way you look.”

                “My motto? You can't spell "first impression" without "impress".

                Especially with social media and all these days.”

                """
                m """{i}Those black and white photos in Joule's profile come to mind.

                “You must know that well--{w} being an influencer yourself.”

                """

                hide joule-neutral
                show joule-awkward

                j "“Geez. That stuff's embarrassing. {w}I wouldn't do it if I didn't have to promote myself, to be honest.”"
                m "“Oh, please. I bet you have *so* many hotties sliding into your DMs.”"
                j "Nah, I can't read all that...{w}You know, being a dumb jock and all."

                if self_awareness>=30:
                    m """(Huh. I didn't take Joule to be the self-deprecating type.)

                    (I wonder if he really believes that he's dumb?)

                    (Oh well, I guess everybody has their hang-ups.)

                    """

                hide joule-awkward
                show joule-wink

                j "“Although...I wouldn't mind sounding out some letters if *you* were the one sending them.”"
                m "{i}!!!{w}Ironically, I'm at a loss for words."
            
    label after_choice_12j:
  
            j """
            “I don't think you need any physical improvements, personally, but I can help you get closer to the body you feel best in.”

            We'll run through some HIIT style cardio training to optimize fat burning and some targeted strength exercises to help you sculpt that lean muscle.”

            Now that we've got that out of the way, let's do some fitness tests.”
            """  

    hide joule-neutral
    hide joule-smile with dissolve
    m """
    We spend the rest of the session running a few tests to measure my physical condition.

    And I mean literally *running*."""

    play sound "/audio/treadmill.mp3" volume 0.7


    m """
    I squeeze my abs like I'm crushing grapefruit for the sweet smoothie I'll reward myself with after this.

    I lower myself into squats and lunges, imagining I'm about to blast off from my corporeal prison into a stronger, hotter version of myself.

    I pump my legs on the treadmill, heart beating faster than the jackhammer outside my window at 7AM.

    All the while, Joule watches me carefully, taking notes on his clipboard."""

    play audio "/audio/pencil-write.mp3"


    m "Every so often, he pushes a button on the treadmill, making it harder to keep up."

    play audio "/audio/button-press.mp3"

    m """
    {cps=30}(I wonder how I'm doing?){/cps}

    {cps=60}(Am I doing this right?){/cps}

    {cps=90}(Is there a right way to run?){/cps}

    {cps=120}(Why didn't Joule tell me about it?){/cps}

    {cps=170}(I wish he'd say {i}something!{/i}){/cps}
    """

    play audio "/audio/button-press.mp3"

    stop sound


    

    show joule-neutral with dissolve

    j "“Good job today, Menmi. I think I've got what I need to develop an effective training plan.”"
    m "His broad palm wraps around my shoulder, giving it a squeeze. All my nerves stand on end."

    hide joule-neutral
    show joule-smile
    j "“'Til next time. Take care of yourself, OK?”"
    hide joule-smile with dissolve

    m """
    (Even though this wasn't a formal training session, I do feel lighter than when I came in.)

    (Maybe there is something to this whole exercise thing.)

    (Look out, world. Menmi's making her metamorphosis!)
    
    """

    $ j1=True
    





