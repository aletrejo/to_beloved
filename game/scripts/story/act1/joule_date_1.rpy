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

    It's still early but my body's already abuzz with nerves.

    I've never had a personal trainer before, but it seems like things could get pretty *physical*.

    The thought of *my* limp noodle of a body being so closely scrutinized by someone who could probably break a bench on his abs alone is making me feel all tingly.

    {i} Calm down, Menmi. {p}You need to get through this to get a hot bod and finally earn that confidence!

    """
    stop music
    play sound "/audio/impact-slam.mp3"
    scene gym-inside with vpunch:
        matrixcolor InvertMatrix(value=1.0)

    i "Hope he's not disgusted by you."

     if self_awareness>=40:
        m "*I'm* disgusted by this unhelpful line of thinking"
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

        elif self_awareness<40:
            m """Ahh! What if he is? I've gotta toughen up...{p}like, *now*."
            
            {i} Alright! Crunch time.

            I'm preparing to do six hundred crunches in 5 minutes when the gym door swings open.

            """

    show joule-neutral with dissolve
        j "“Hey hey. Nice to see you again, Menmi.”"

    play sound "/audio/impact-slam.mp3"
    scene gym-inside with vpunch:
        m """
        Eep! I know I was expecting him, but Joule packs such an imposing presence that I can't help but be startled by him.

        {i} Okay, okay. Play it cool. 

        “Hey Joule! You're a little early.” 

        """

    show joule-smile
        j "“Not as early as you, though. {p} On a weekend, too.”"

    show joule-thinking
    hide joule-smile

        m "He pushes a hand through strands of slightly wet hair, his skin carrying the dewey tint of somebody fresh out of the shower."

    hide joule-thinking

        j "“Early riser, are we?”"

        m """
        “Haha, yep! That's me.”

        Just a little white lie, but I don't want him to think I'm a slacker. {p} Gym guys hate lazy ladies...{w}I think.
        """

    if self_awareness>=40:
        c "Hey, you're here aren't you?"
        m "Ugh, true. Begone, imposter complex."
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

    show joule-smile
    j """
    “Have had you breakfast yet?”

    “I brought you something in case you hadn't.”
    """

    hide joule-smile

    j """

    “A lot of my clients usually skip breakfast because they're too busy, or they aren't hungry in the morning.”

    “But breakfast is real important to a healthy body...and a productive workout.”

    “Sometimes you've gotta eat even when you're not hungry. {p} You have to be disciplined.

    “Mind over matter, you feel me?”

    """

    show joule-smile

    j "“Plus, breakfast is delicious!”"

    m "Oof good read."

    play sound "/audio/stomach-growl.mp3"    

    m """
    I consider lying and telling Joule that I'm practicing *intermittent fasting*, but my empty stomach has decided to speak for the both of us.

    The corner of Joule's mouth hooks up as he passes me a clear bottle filled with some kind of beige slush.
    """

    j "“This is my GO Morning protein shake. It's got a heavy duty amino acid profile that'll fortify your muscles for a HARD. {p} CORE. {p} workout.”"

    m """
    He beats a fist on his abs for emphasis.

    “Wow, thanks.”

    While I'm flattered that he thought of me, the chunky contents of the container aren't giving "gustatory delight"
    """

    show joule-sad
    hide joule-smile

    j """
    “No problem.”

    “Consider it an apology for what happened the other day.”
    """

    m """
    The realization that he's thought about my feelings so much makes my throat clog up like sticky dough down a drain. 

    The protein shake feels pleasantly cool in my hand.

    {i} Nothing ventured, nothing gained.

    """

    hide joule-sad

    play sound "/audio/gulp.mp3"    

    m """
    I swallow the concoction, surprised by how easily it goes down.

    Despite its consistency, the taste is pretty inoffensive. 

    It's no Starfruitbucks latte, but it isn't putrid mystery glue either.

    """

    j "“Well, what do you think?”"

    m """
    “Not bad. {p}What's in it?”

    Keeping my fingers crossed that the answer isn't something like "3 lbs of chicken breast"
    """

    j "“Ah, you're asking the right questions.”"

    show joule-smile

    j "“It's cooked chicken breast!”"
    i "{i}Feels so wrong to be right."
    j "“...also broccoli, egg whites, potato, oats and strawberry jam for flavor.”"
    m """“...{p}All such delicious ingredients!”

    Although blending them all together sounds kind of gross. {w}I keep that part to myself, though.

    """

    hide joule-smile

    j """
    “Oh, I almost forgot the most important ingredient: {w}Knowledge.”

    “The knowledge that *you're* in control of what you put into your body,

    and *that's* HARD. {p}CORE.”

    """

    m """
    Joule raps his knuckles against his abs with such sincerity that I can't help but laugh.

    “Sure - but what if you're knowledge-intolerant?{p},”

    “Thinking too hard gives me a tummyache.”
    """

    show joule-smile

    j """
    “I'm serious!”

    Most people think that of the body and brain as separate entities, but they're really interconnected. {p} Inextricable, even.

    I mean just think about it -{p} when you're hungry, you feel crummy. {p} And when you exercise, you feel great!

    The same is true vice versa - when you think about what you put into your body, {p} and not just consuming nutrients on autopilot, {p}the whole experience changes!
    """

    hide joule-smile

    m "Hmmm...maybe he's got a point."

    label choice_12j:
        menu: 
            m "How should I respond?"

            "“I don't know...”":
                c "What's this guy on? Besides 3 lbs of cooked chicken."
                m """
                “I'm not sure if just *thinking* about something will change the facts.”

                “Calories in, calories out, right?”

                “I'm sure the science it more complicated than that, but our bodies have to obey the laws of nature after all.
                """

                show joule-smile

                j """
                “Looks like we've got a natural nutritionist on our hands!”

                “I'm glad to see you're so interested in the science of working out.”
                """

                hide joule-smile
                show joule-wink

                j "“We need more smart girls in the world.”"

                hide joule-wink

            "“If you say so!”":
                c """
                His himbo musings aren't getting you anywhere closer to the boy bait bod you're after.

                Just agree with him and move on. {p}I'm sure he'd like that.
                """  
                m "“Sure, you're the expert!”"
                show joule-smile
                j "“Right on!”"
                hide joule-smile

            "“That makes sense.”":
                c "He might be onto something there.{p} How can you focus on your body when your mind's not in the moment?"
                m """
                “Yeah, that makes sense.”

                {i}Maybe I've been fixating on my end goal of looking hot too much. {p} I need to re-ground myself, feel more at home in my body.

                I take a deep breath, flexing my fingers from wrist to tip. Listening to the hard-working hum of the air conditioner cooling the empty gym.

                Without thinking, I take another gulp of Joule's GO Morning shake. {p}It *does* taste a little sweeter this time around.
                """
                $ renpy.notify("+5 Self-Awareness")
                $ self_awareness += 5
                
                show joule-smile
                j "“Feels good, right? {p} Being connected to your body.”"
                hide joule-smile

    label after choice_12j:

        show joule-neutral
        j "“Alright! Now that we've got breakfast out of the way, I want to get to know you a little better, Menmi.”"

        m """{i}Oh gosh...a date already?

        {i}Go Morning Protein Shake? {w}More like a love potion!

        I narrow my eyes.

        {i}There's no evidence supporting that Joule *isn't* a witch.
        """
        
        hide joule-neutral
        show joule-smile
        j "“An assessment of your health history and habits will help me understand what to look out for and personalize a training regimen suited to your needs.”"
        m """
        {i} Oh, he's just talking about my physical and mental well-being.

        “Sure. What would you like to know?”
        """

        hide joule-smile
        show joule-neutral
        j """Great - I just need to ask you a few questions.

        First off - what are your fitness goals?

        """

        m """
        “I want to be a baddie.”

        Hot Girl Logic 101 - Never hide your intentions. {p}I mean, how mad can you *be* at a hot person?

        “I want to walk into a room and convince people that I have a beach body even when I am not at the beach.”

        """

        hide joule-neutral
        show joule-smile

        j "“Hahaha. How would that even work?{p} Do they all suddenly develop X-ray vision?"
        m "“No I don't want them to know that I have a skeleton.”"

        hide joule-smile
        show joule-neutral

        j """
        “Alright, alright.{p} Fair enough.”

        “Physical aesthetics is a common enough reason for working out. {p}We can definitely work on minimizing body fat and developing lean muscle.” 
        """

        hide joule-neutral
        show joule-wink

        j "“If you ask me, though, you don't need to change your body to be attractive.”"
        m "{i}Eep! I got a compliment."

        if self_awareness<=40:
            i "Oh don't be embarrassing. {p}It's his job to gas you up."

        hide joule-wink
        show joule-neutral

        j """
        “Promise me one thing, though -{w}when we work out, I want you to think about how you're doing this for yourself.”

        "Wanting to feel confident about the way you look is all well and good, {w}but chasing someone else's standards instead of your own satisfaction won't work out in the long run.”

        "Erm - no pun intended.”

        """

        hide joule-neutral
        show joule-sad

        j """“People come and go, but you'll always have yourself.”

        “In my experience, you can't rely on others.”""" 
        

        m """
        The darkness in his tone take me off guard,{w}but the whole 'love yourself before others' speech isn't new to me.

        You hear it all the time from music videos about girl power and older, 30-somethings who think they're passing on some sagely, arcane knowledge that we don't already know or something.

        But none of that applies to me. I already love my life! {p} It's perfect! Especially now that I live in Applecore City and have an amazing job and hotties surrounding me at every turn.

        I'd better be on my best behavior if I want one

        """

        hide joule-sad
        show joule-smile

        j "“Good. Now that we've got that out of the way, let's do some fitness tests.”"

        hide joule-neutral
        hide joule-smile with dissolve
        m """
        We spend the rest of the session measuring my current physical condition so we have a baseline for progress.

        I lower myself into squats and lunges, imagining I'm about to blast off from my corporeal prison into a stronger, hotter version of myself.

        I pump my legs on the treadmill, heart beating faster than the jackhammer outside my window at 7AM.

        All the while, Joule watches me carefully, taking notes on his clipboard.

        I wish he'd tell me how I'm doing, but he's careful not to encourage me too much. This is an assessment after all.

        But I want to know if I'm doing this right!

        At the end of the session, he claps me on the back.
        """

        show joule-neutral with dissolve

        j "“Good job today, Menmi. I think I've got what I need to develop an effective training plan.”"
        m "His broad palm wraps around my shoulder, giving it a squeeze. All my nerves stand on end."

        hide joule-neutral
        show joule-smile
        j "“'Til next time. Take care of yourself, OK?”"
        hide joule-smile with dissolve

        m """
        Even though this wasn't a formal training session, my whole body feels limber, and my head feels light.

        Must've been all those fitness tests.

        I hope my heart rate goes back to normal soon.
        
        """


    





