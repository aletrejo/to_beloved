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
#Menmi feels similarly pressured to conform to other peoples' expectations of "what Joules gf should look liek"
#Control your body, control your life -- lack of control from feeling weak; always on the defensive; on high alert to appear strong in order to avoid judgment

    play music "/audio/joules-theme.mp3" fadein 0.5
    scene gym-inside with dissolve

    m "After a week of trying out simple resistance exercises, Joule is showing me how to lift weights today."

    show joule-smile with dissolve

    j "This kind of strength training has full body benefits."
    m """(Full body, huh?)

    I glance at the sewer-cover-sized weight plates that flank the steel bar.

    (I'll definitely need every fiber of my strength to lift that...)
    """

    hide joule-smile
    show joule-neutral

    j "From your joints to your heart to your metabolism, and even your blood sugar, strength training has been shown to reinforce your body's core functions and increase your lifespan."
    m """I'm here for a good time, not a long time.

    (I heard that in a commercial for bathroom supplements once.)

    """

    hide joule-neutral
    show joule-smile at laughter

    j "Haha! You can actually have both!"

    hide joule-smile
    show joule-neutral

    j """
    There's *strong* evidence that suggests that strength training can improve mood and self-esteem, along with other mental health benefits.

    Some weightlifters credit the psychological benefits to the cycle of intensity followed by regular pauses, which allow them to check in with themselves.

    """
    m "Like having bathtime after a busy week!"

    hide joule-neutral
    show joule-smile

    j "Right on!"

    hide joule-smile
    show joule-neutral

    j "And just like a bath, the best way to do this is to ease into it."

    hide joule-neutral
    show joule-pumped

    j "So are you ready for this, Menmi???"
    m """(I was nervous at first, but the exercises I've done over the week have me feeling a bit more confident.)

    (Still, I'm not sure if my noodly arms have it in them to lift literal those dummy thicc dumbbells.)

    (What if I get hurt?)

    (Or worse, do it *wrong*?)
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
                m """Screaming with Joule really pumps me up! {w}It's like I'm making it real by shouting it!

                (I CAN do this!)

                “YEEEEAAAHHH!”
                """
            "Yeah...":

            jump to joule_pep_talk

            "No."
            jump to joule_pep_talk

    label joule_pep_talk

    label after_choice_13j:
        j "That is HARD. CORE."