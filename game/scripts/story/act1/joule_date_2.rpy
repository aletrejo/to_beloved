label joule_date_2:
    play sound "/audio/pencil-write.mp3"
    hide screen open_planner
    hide screen open_insights
    scene city-morning with fade:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}Week [week]{/size}{/font}{/color}{color=#000000}{color=#000000}{font=JustAnotherHand-Regular.ttf}{size=200}\n Weekend!{/size}{/font}{/color}" at truecenter with wiperight
    pause

#He tries to bandage himself but he can't because he hurt his dominant hand. Menmi insists on helping him. While she is bandaging him, she talks to him to distract him from the pain. She asks about his instaHam, his goals, and his family (loops back in choice)
#Joule reveals his values: he wants to be strong enough to protect the ones he loves and stand up fr the weak. 
#Menmi being perfectionistic about working out; wanting immediate results; not taking rests  
#Joule central problem: He loses his way and tries to optimize optics. Comparing yourself to others is pointless because there’s no way of knowing a person’s eating habits, sleep schedule, genetic makeup, and all the other things that affect body composition and performance. 
#He lets other people affect his hard core == shattering his sense of self in favor of min maxing and comparing himself to others
#Menmi feels similarly pressured to conform to other peoples' expectations of "what Joules gf should look liek" -- joules ex (client) shading menmi for weightlifting bc "arent you afraid of getting buff?"
#Control your body, control your life -- lack of control from feeling weak; always on the defensive; on high alert to appear strong in order to avoid judgment

    play music "/audio/joules-theme.mp3" fadein 0.5
    scene gym-inside with dissolve

    m "After a week of trying out simple resistance exercises, Joule is showing me how to lift weights today."

    show joule-smile with dissolve

    j "“This kind of strength training has full body benefits.”"
    m """(Full body, huh?)

    I glance at the sewer cover-sized weight plates that flank the steel bar.

    (You're telling me the Fruit Ninja Turtles lift {i}those{/i} every time they leave the sewer???)

    (I'll definitely need every fiber of my strength for this...)
    """

    hide joule-smile
    show joule-neutral

    j "“From your joints to your heart to your metabolism, and even your blood sugar, strength training has been shown to reinforce your body's core functions and increase your lifespan.”"
    m """“I'm here for a good time, not a long time.”

    (I heard that in a commercial for bathroom supplements once.)

    """

    hide joule-neutral
    show joule-smile at laughter

    j "“Haha! You can actually have both!”"

    hide joule-smile
    show joule-neutral

    j """
    “There's *strong* evidence that suggests that strength training can improve mood and self-esteem, along with other mental health benefits.”

    “Some weightlifters credit the psychological benefits to the cycle of intensity followed by regular pauses, {w}which allow them to check in with themselves.”

    """
    m "“Like having bathtime after a busy week!”"

    hide joule-neutral
    show joule-smile

    j "“Right on!”"

    hide joule-smile
    show joule-neutral

    j "“And just like a bath, the best way to do this is to ease into it.”"

    hide joule-neutral
    show joule-pumped

    j "“So are you ready for this, Menmi?”"
    m """(I was nervous at first, but the exercises I've done over the week have me feeling a bit more confident.)

    (Still, I'm not sure if my noodly arms have it in them to lift those dummy thicc dumbbells.)

    (What if I get hurt?)

    (Or worse, do it {i}wrong{/i} and {i}embarrass{/i} myself???)
    """

    label choice_13j:
        menu: 
            m "{i}Am{/i} I ready for this?"

            "Yeah!!!":
                c "You've practiced for this. And, like Joule said, you'll ease into it. Trust the process."
                m """(That's right. Even if I don't have full confidence in myself, I have to trust Joule.)

                (Joule is a pro, and he believes in me! I believe in the he who believes in me!!)

                “LET'S GO!!”

                """
                $ renpy.notify("+5 Self-Awareness")
                $ self_awareness += 5

                hide joule-pumped
                show joule-smile

                j "That's the spirit, Menmi!!! {w}LET'S GOOOOO!"
                m """(Even though it feels a little silly, screaming with Joule really pumps me up!) 

                (It's like I'm making it real by shouting it!)

                (I CAN do this!)

                “YEEEEAAAHHH!”
                """
                hide joule-smile
                show joule-hardcore
                j "I just want to say, Menmi. {w}Your determination is HARD. CORE."
                hide joule-hardcore
                show joule-smile
                m "(Joule's energy is really infectious!)"
                hide joule-smile with dissolve

            "Yeah...":
                c "Your answer reflects what you're feeling -- a realistic mix of excitement and apprehension."
                m "It's fun to try new things, but people who dive in headfirst usually suffer concussions."
                hide joule-pumped
                show joule-thinking
                j "“Hmmm...not the enthusiastic response I'd hoped for”."
                hide joule-thinking
                show joule-smile
                j "“But I wouldn't be doing my job if I couldn't fix that!”"
                jump joule_pep_talk

            "No.":
                c "Girl, you're not ready."
                m "“I can't do this!!!”"
                hide joule-pumped
                show joule-sad
                j "“Aw hey, I get it. Trying new things can be intimidating.”"
                hide joule-sad
                show joule-smile
                j "“I think I know what'll pump you up, though!”"
                jump joule_pep_talk

    label joule_pep_talk:
        stop music fadeout 1.0
        hide joule-smile with dissolve
        m "Joule disappears into a back room tucked into the corner of the gym."
        show joule-pep at hop
        play music "<from 22>/audio/joules-theme.mp3" volume 0.7
        m """!!! “{w}Joule?”

        “What are you doing? {w}WHAT are you wearing??”"""
        j "“Menmi, as your #1 cheerleader, I'm here to tell you--”"

        hide joule-pep
        show joule-pep

        j "“YOU. ARE HARD.{w} CORE.”"
        m "“Hahaha. But what's with the fuel nozzles?”"

        hide joule-pep
        show joule-pep at hop

        j "“I'm GASSING you up.”"
        m """“Hahahahaha.”

        (I know that Joule's being a total cheeseball, but I can feel the pressure of performance *lift* off of me.)

        """
        j """“Hey, Menmi.{w} I think it's really cool that you want to improve yourself and are taking steps to achieve it.”

        “I knew from our first meeting that you're a strong person{w}--inside and out.”

        “That's why I have no doubt that you can do this!”

        """

        hide joule-pep
        show joule-pep at hardcore

        j "“Say it with me - YOU. ARE HARD.{w} CORE.”"
        m "“Haha I don't know...(it feels silly)”"
        j """“It's OK if you don't believe it just yet--”

        “That just means you have to shout it until you do!”

        “Let your body lead your mind in this.{w} Trust.”"""

        if self_awareness>=60:
            m "(He's right. There are times when I shouldn't overthink things.)"
        elif self_awareness<60:
            m "(I don't get how shouting will change my lack of physical ability,{w} but I guess I should try for Joule...)"

        m "“OK...{w}I am hardcore.”"
        j “"Nice! {w}Again!”"
        m "“I am hardcore!”"
        hide joule-pep
        show joule-pep at squirm
        j "“Now you're talking! AGAIN!”"
        m "“I. AM HARD. CORE.”"
        show gym-inside with vpunch
        hide joule-pep
        show joule-pep at hop
        j "That's the spirit! LET'S GOOOOOOO!!”"
        show gym-inside with vpunch
        m """“LET'S GOOOOOO!!”
        (I can't quite believe it myself, but I really do feel more ready!)"""
        j """“As you wish, my lady.”

        “Let's get down to business!”"""
        hide joule-pep with dissolve
        m "Joule disappears into the backroom again and reemerges without his accessories."


    label after_choice_13j:
        m """He walks over to the power rack and affixes the lightest set of weights to the steel bar.

        (They might be the lightest set, but they still look kind of heavy...)

        He gestures for me to stand behind the bar.

        After adjusting the bar above the center of my feet, Joule mimes for me the proper technique.

        """
        show joule-neutral

        j """“When you go down, keep your shoulder blades over the barbell and your feet apart.”

        “And when you come up, push with your legs while keeping your chest lifted.”

        """

        hide joule-neutral with dissolve
        stop music fadeout 0.5
        play audio "/audio/heartbeat-fast.mp3" volume 1.5

        m "Joule is behind me, making gentle adjustments to my form."
        j "“Don't squeeze your shoulder blades and keep your back erect with a slight arch.”"
        m """A thrill chases through me as I feel his hand against the small of my back.

        Joule's arms suddenly encircle my waist, gripping the barbell in front of me.

        """
        j "“Remember to keep the barbell close to your body, rolling it over your thighs until your hips and knees lock.”"
        m """I feel Joule's closeness as the warmth spreads its way across my back.

        When he speaks, his voice rumbles softly in my ear.

        """
        j "“And remember, Menmi{w}. Keep your spine firm.{w} I don't want you to get hurt.”"


        play music "/audio/joules-theme.mp3" fadein 0.5
        show joule-smile with dissolve

        j "“And that's all there is to it! Any questions?”"
        x "“Yeah I gotta question, Joule{w}!”"
        hide joule-smile
        show joule-surprised
        extend "“Where do we get the filtered water to refill the drinking station?{w} From the fridge?”"
        hide joule-surprised
        show joule-blush
        j "“Sorry, Menmi. That's the new guy.{w} I didn't know he was going to be here this morning.”"
        x "“Don't tell me we have to get bottles from the vending machines...I'm not carrying any change.”"
        hide joule-blush
        show joule-annoyed with vpunch
        j "“The machine filters the water, Stu!{w} And the vending machines don't take cash!”"
        hide joule-annoyed
        show joule-shocked with vpunch
        x "“Oh, in that case, I'll just use water from the bathroom...”"

        j "“J-just hold on, OK?{w} I'll be there in a sec!”"

        hide joule-annoyed
        show joule-sad
        j "“I'm {i}really{/i} sorry about this Menmi, but he needs my help.”"
        hide joule-sad
        show joule-smile
        j "“Just hang tight for a moment, OK? I'll be back soon.”"
        m "“Don't worry about me! {w}Go get Stu before he contaminates the water supply!”"
        stop music fadeout 1.0
        hide joule-smile with dissolve
        m """As Joule instructs Stu on a different kind of training, I marvel at his breadth of knowledge.

        (Not only does he remember all the details about the technique and biological benefits, {w}he knew how to make me feel comfortable about trying something new!)

        (...)

        (He really is a good teacher. {w}A true pro.)

        (...)

        (I hope I don't disappoint him.)

        (Maybe if I just try it a little bit myself...{w}I'll have a better grasp of this when Joule gets back.)

        (What better way to show him that his instruction is working?)

        I imagine Joule's response upon seeing me lift the weight all by myself.

        """

        scene gym-inside with dissolve:
            blur 50
        show joule-surprised with dissolve

        j "“Woah, Menmi!{w} You're SO. {w}HARD. {w}CORE.”"

        hide joule-surprised
        show joule-smile

        j "“I {i}love{/i} a woman who takes initiative! It's SO {w}HARD. {w}CORE.”"

        hide joule-smile
        show joule-wink

        j "“You really know how to get me going. {w}HARD. {w}CORE.”"

        hide joule-wink
        scene gym-inside with dissolve

        m """(!!!)

        (OK -- I'm nervous, but I'm gonna try!)

        (Nothing wagered, nothing gain(s)ed!)

        Remembering Joule's advice, {w}I keep my back firm and lower myself to pick up the weight.

        The bar is cold and a little bumpy against my palm. 

        As I pull up, I dig my toes into the ground, just as Joule instructed.

        (Oh my gosh!)

        """

        scene gym-inside with vpunch

        extend "(I'm doing it! I'm really doing it!)"

        show joule-surprised with vpunch
        j "“Menmi!”"
        m "“AAAaaaahhh!!!”"

        hide joule-shocked
        scene gym-inside with vpunch
        scene gym-inside with flash
        play sound "/audio/crash.mp3"
        scene gym-inside with vpunch

        m "(He startled me and I dropped the dumbbell!)"
        
        show joule-pain with dissolve
        play music "audio/secret.mp3" fadein 0.5
        j "“Menmi...{w} Are you hurt?”"
        m """“{i}I'm{/i} not hurt!”

        (Thanks to Joule, {w}who swooped in to catch the falling dumbbell.)

        (Unfortunately, it landed Joule's foot...{w}in a bad way, it seems.)

        (He's stooped low to the ground, clutching his ankle.)

        (Aaaahhh...{w}I feel {i}terrible.)

        “Joule...I'm so, {i}so{/i} sorry!”

        """
        j "“No, no it's OK--{w} it was my own fault for surprising you.”"
        hide joule-pain
        show joule-sad
        j "“I was just so scared of you getting hurt.”"

        hide joule-sad
        show joule-annoyed with vpunch

        j "“Please don't do anything unsupervised like that again!”"
        hide joule-annoyed
        show joule-pain
        m "“I'm sorry, Joule. I really won't. {w}I promise.”"

        if self_awareness >=60:
            c "You live and you learn."
            m """(I wasn't wrong for wanting to try something for myself, {w}but this wasn't the time and place for it.)

            (I'll carry this lesson with me into the future. {w}This feels so bad that I don't ever want it to happen again!)

            """

        elif self_awareness<60:
            m """
            (How could I have been so {i}stupid?{/i})

            (Because of me, Joule got hurt.)

            (It's all my fault.{w}I can't trust myself to make good decisions.)

            """

        j "“Good.”"
        
        hide joule-pain
        show joule-pain with hpunch
        
        j "“Ah!”"
        m """“Joule!” 

        (I'm pretty sure his ankles aren't supposed to look that swole.)

        “Let me get you an ice pack.”
        """
        
        hide joule-pain
        show joule-surprised
        j "“No!{w} You're a client. You're not responsible for me.”"
        hide joule-surprised
        show joule-annoyed
        j "“I can take care of myself--”"
        hide joule-annoyed
        show joule-pain with hpunch
        j "“Ah!”"
        m """“You shouldn't try to walk right now.”

        “I know where the ice is. {w}I saw you show Stu.”"""

        hide joule-pain with dissolve
        scene gym-inside:
            blur 50
            matrixcolor BrightnessMatrix (value=-0.4)

        m """
        Before he can protest again, I run to the kitchen, locating the freezer.

        I fill a paper towel with ice cubes and bring them back to Joule.
        """

        play sound "/audio/ice-pour.mp3"

        scene gym-inside
        show joule-pain with dissolve

        m "Begrudgingly, he allows me to press the ice pack to his ankle."
        m "Does it hurt?"

        hide joule-pain 
        show joule-pain at squirm

        j "No."
        m "(He's a such a bad liar.)"

        hide joule-pain
        show joule-smile
        j """
        Thanks for that, Menmi! 

        We should get back to training now, though. We're on the clock, after all.
        """

        m "In a moment. Let's just wait for the swelling to go down."
        
        hide joule-smile
        show joule-sad

        j "But-!"
        m """No 'buts'!{w} It's my time that I paid for, and I want to help you recover!

        (That gets him to stop.{w} Huh, he's so easy to chastise.)

        (Now that I think of it, this could be a good opportunity to get to know Joule better.)

        """
    label choice_14j:
        menu:
            m "What should I ask Joule about?"

            "His muscles":
                m "So Joule...you're pretty swole."
                hide joule-sad
                show joule-wink
                j "So you've noticed?"
                hide joule-wink
                show joule-surprised
                m "I was wondering, since we talked about my motivation for working out, why do {i}you{/i} do it?"
                hide joule-surprised
                show joule-softsmile
                j "No client's ever asked me that before."
                hide joule-softsmile
                show joule-neutral
                j "I guess the short answer is that I love what I do --{w}the satisfying burn after each workout, the gains I can see in the mirror, knowing that my choices and dedication led to them."
                hide joule-neutral
                show joule-smile
                j "And helping other people reach their goals is really rewarding!"
                hide joule-smile
                show joule-neutral
                m "I see. It's kind of like, planning for your future and making moves to manifest your dreams each day."
                hide joule-neutral
                show joule-smile
                j "Yeah! That's a good way of putting it too."

                label joule_motivation:
                hide joule-smile
                show joule-thinking
                j """It's kind of like, a way to control your fate, right?

                There's so many things in this world that we can't control,{w} but at the very least, we're in charge of our own bodies.

                """
                hide joule-thinking
                show joule-sad
                j """Truth be told, I was a pretty short and scrawny kid growwing up.

                Despite that, I had a big attitude,{w} and I guess that rubbed people the wrong way sometimes.

                I was always getting into fights at school, {w}and losing them, to be honest. It really worried my family.

                """

                hide joule-sad
                show joule-annoyed

                j """I just got so fed up one day. I decided that I wasn't going to be weak anymore. 

                I wanted to be strong --{w}so that I could not only defend myself, but the people I care about.

                """

                hide joule-annoyed
                show joule-smile

                j """I started running, lifting weights, and training in mixed martial arts.

                And I got bigger and stronger.{w} I felt more confident in myself too.

                I didn't start winning all my fights per se, {w}but I got good enough that my bullies thought twice about messing with me.

                """

                hide joule-smile
                show joule-neutral

                m "So you wanted to be strong so that you could defend yourself?"
                j """Exactly. I felt powerless, and training was my way of gaining power.

                Power over my bullies. My body. The trajectory of my life.

                """
                hide joule-neutral
                show joule-smile

                 $ joule_relationship +=10
                 $ renpy.notify("Joule feels closer to you!")

                m """That's so inspiring!

                (I'm really glad Joule felt comfortable enough with me to share that).

                """

            "His hobbies":
                m ""
            "His family":
                m ""
            "His dreams":
                m ""
            

        



    $ j2=True





