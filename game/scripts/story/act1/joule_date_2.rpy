label joule_date_2:
    play sound "/audio/pencil-write.mp3"
    hide screen open_planner
    hide screen open_insights
    scene city-morning with fade:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}Week [week]{/size}{/font}{/color}{color=#000000}{color=#000000}{font=JustAnotherHand-Regular.ttf}{size=200}\n Weekend!{/size}{/font}{/color}" at truecenter with wiperight
    pause

#Date 2: Menmi is trying out weightlifting. Joule gets called over by a newbie to fix the water cooler. He tells Menmi to stay put. WAnting to impress Joule, Menmi goes ahead and tries to lift it anyway. The weight falls but Joule saves her at the last moment, crushing his hand in the process. 
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
            jump to joule_pep_talk

            "No.":
                c "Girl, you're not ready."
                m "“I can't do this!!!”"
                hide joule-pumped
                show joule-sad
                j "“Aw hey, I get it. Trying new things can be intimidating.”"
                hide joule-sad
                show joule-smile
                j "“I think I know what'll pump you up, though!”"
            jump to joule_pep_talk

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
        show joule-pep at hardcore

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

        j """When you go down, keep your shoulder blades over the barbell and your feet apart.

        And when you come up, push with your legs while keeping your chest lifted.

        """

        hide joule-neutral with dissolve
        stop music with fadeout 0.5
        play audio "/audio/heartbeat-fast.mp3" volume 1.5

        m "Joule is behind me, making gentle adjustments to my form."
        j "Don't squeeze your shoulder blades and keep your back erect with a slight arch."
        m """A thrill chases through me as I feel his hand against the small of my back.

        Joule's arms suddenly encircle me, gripping the barbell in front of me.

        """
        j "Remember to keep the barbell close to your body, rolling it over your thighs until your hips and knees lock."
        m """I feel Joule's closeness as the warmth of his chest spreads its way across my back.

        He speaks, {w} breath hot and soft, {w}into the shell of my ear.

        """
        j "And remember, Menmi{w}. Keep your spine firm and neutral.{w} I don't want you to get hurt."


        play music "/audio/joules-theme.mp3" fadein 0.5
        show joule-smile with dissolve

        j "And that's all there is to it! Any questions?"
        x "Yeah I gotta question, Joule{w}!"
        hide joule-smile
        show joule-surprised
        extend "Where do we get the filtered water to refill the drinking station?{w} From the fridge?"
        hide joule-surprised
        show joule-blush
        j "Sorry, Menmi. That's the new guy.{w} I didn't know he was going to be here this morning."
        x "Don't tell me we have to get bottles from the vending machines...I'm not carrying any change."
        hide joule-blush
        show joule-annoyed
        j "The machine filters the water, Stu!{w} And the vending machines don't take cash!"
        hide joule-annoyed
        show joule-shocked
        x "Oh, in that case, I'll just use water from the bathroom..."

        j "J-just hold on, OK?{w} I'll be there in a sec!"

        hide joule-annoyed
        show joule-sad
        j "I'm {i}really{/i} sorry about this Menmi, but he needs my help."
        hide joule-sad
        show joule-smile
        j "Just hang tight for a moment, OK? I'll be back soon."
        m "Don't worry about me! {w}Go to Stu before he poisons the water supply with toilet water!"
        hide joule-smile with dissolve



