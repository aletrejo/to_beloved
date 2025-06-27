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

play music "<from 9>/audio/happily-ever-after.mp3" fadein 0.5
scene gym-inside with dissolve

m "Today, Joule is teaching me how to lift weights"

show joule-neutral with dissolve
