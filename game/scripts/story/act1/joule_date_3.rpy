
label joule_date_3:
    $ lover = "Joule"
    play sound "/audio/pencil-write.mp3"
    hide screen open_planner
    hide screen open_insights
    scene city-morning with fade:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}Week [week]{/size}{/font}{/color}{color=#000000}{color=#000000}{font=JustAnotherHand-Regular.ttf}{size=200}\n Weekend!{/size}{/font}{/color}" at truecenter with wiperight
    pause
 ##Date 3: outdoors in the park near the gym. Joule prepares a lunch to thank Menmi for tending to him; becomes more vulnerable around her.
 #Menmi wears a new jacket because it's a little brisk out and accidentally rips it while they're training. Joule whips out a sewing kit and fixes it for her.

    
    scene menmi-apartment-morning with squares

    m """For today's weekend workout, Joule asked me to meet him in the park by the gym.

    (I wonder what he has in store!{w} I'm so excited! It's almost like a date.)

    (And if I want to impress Joule, I've got to look and feel my best!)

    """

    scene menmi-apartment-morning with vpunch

    m """
    (That's why I warmed up by doing high kicks and shadowboxing in the kitchen!)

    (Who am I shadowboxing?)

    """

    i "Your form is all wrong, and you're embarrassing yourself."

    if self_awareness>=50:
        c "Practice makes perfect! Besides, nobody can see you."
        play sound "/audio/awareness-ding.mp3"
        show screen sticker_get
        pause
        hide screen sticker_get
        show screen place_sticker(chosen_sticker)
        $ available_stickers.remove(chosen_sticker)
        pause
        hide screen place_sticker
        $ passed_checks +=1
        m "(Yeah! Shut up, Intrusive Inner Voice! I'm going to high kick you out of here...)"
    elif self_awareness<50:
        m "(I'm a klutz as usual!)"

    m """
    (OK -- now that I've warmed up, I just have to get dressed.)

    (It's kind of chilly out today.{w}I know! This is the perfect opportunity to break out my new windbreaker!)

    """

    play sound "/audio/whoosh.mp3"
    show windbreaker at truecenter with easeinbottom

    m "(Fashionable {i}and{/i} functional! Let's go!)"

    scene park-day with slideleft

    m "When I arrive at the park, Joule is already there waiting for me."

    show joule-smile with dissolve
    play music "<from 22>/audio/joules-theme.mp3" volume 0.7

    j "“Morning, Menmi!"

    hide joule-smile
    show joule-surprised

    j "“Woah! Cool jacket!"
    m """

    “Thanks!” (He noticed!)

    Joule's in his usual {i}Planet Figness{/i} sleeveless shirt.

    “Aren't you cold?”

    """

    hide joule-surprised
    show joule-neutral

    j "“Nah, I tend to overheat easily.{w} Especially when I'm exerting myself.”"

    hide joule-neutral
    show joule-thinking

    j "“Truth be told, {w}I don't wear a top at all when I'm working out by myself.{w} I'm kind of Anti-Shirt like that.”"
    m """My face heats up. (How can he say something like that so casually?)

    (I wish I had a shirt right now...for my face.)

    “M-me too.”

    """

    hide joule-thinking
    show joule-smile at laughter

    j "“You just get it, Menmi.”"

    hide joule-smile
    show joule-neutral

    j "“Anyway, I thought it'd be fun to change things up today and work on our cardio in the beauty of nature!”"
    m "“I'm wearing my running sneakers and ready to run-ble.”"

    hide joule-neutral
    show joule-wink

    j "“Great attitude, as usual!{w} Let's get going -- follow me!”"

    hide joule-wink with dissolve

    scene park-day:
        blur 50

    m """Joule and I set off on a lap around the park at a steady pace. 

    The scenery and people rush by, {w}but I focus on chasing Joule, his navy blue tank billowing as the wind blows its way across his back. 

    Every so often, Joule checks in on me behind him, adjusting his pace to match mine.

    He doesn't seem to tire, which makes me push myself even harder to keep up.

    (It's getting harder to breathe, though...)
    """

    play sound "audio/huff.mp3"
    scene park-day with flash:
        matrixcolor BrightnessMatrix (value=0.4)
    scene park-day with flash
    show joule-sad with dissolve

    j "“Woah. Hey, Menmi -- you good? {w}Let's take a break here.”"
    m """“No, no. I'm fine. {w}I can keep going.”

    (I say, desperately gasping for breath like a fish out of water.)
    """

    hide joule-sad
    show joule-neutral

    j "“It's great to push through to progress sometimes,{w} but I've worked with you long enough to know when you need a break.”"
    
    hide joule-neutral
    show joule-sad

    m "“I...I just want to do well for you!”"
    j "“Hey, hey listen...you're already doing well.”"

    hide joule-sad
    show joule-softsmile

    j """“Your tenacity and commitment to self-improvement is impressive enough.”

    “Besides, you should always consider yourself before me.{w} And you're at your aerobic limit.”

    “Let's take a break. {w}This is a good spot, anyway.”

    """

    hide joule-softsmile with dissolve

    m """

    It's early on the weekend so there aren't many people around.

    Joule pulls a {i}Planet Figness{/i} duffle bag out of the bushes.

    ??? “{w}Where did that come from???”
    """

    show joule-smile at dissolve

    j "“Haha -- don't worry. {w}I dropped it off earlier before you got here.”"

    hide joule-smile
    show joule-neutral

    j "“It's not some random bag filled with shady stuff or anything.”"

    m 
    m """

    Joule unpacks a blanket from the bag and flicks it up, letting it float flat onto the grass. He gestures for me to sit on it.

    (How convenient!)

    As I settle myself on the blanket, {w}Joule reaches into the bag and withdraws a thermos, which he offers to me.
    """

    hide joule-neutral
    show joule-softsmile
    show protein-shake with easeinbottom

    j "“Drink this. {w}Your body needs to replenish its nutrients.”"
    m """

    I take a peek at the sticky-thick beige-adjacent slush in the bottle.

    “What is it?”

    """

    hide joule-softsmile
    show joule-smile with vpunch
    j "“This is my GO! Morning protein shake. It's got a heavy duty amino acid profile that'll fortify your muscles.”"

    hide joule-smile
    show joule-hardcore

    j "“After a workout, it goes {w}HARD. {w}CORE.”"

    hide joule-hardcore
    show joule-neutral

    m """I'm a little hesitant about the concoction, but my mouth is so dry that it could compete with my boss' sense of humor.

    The bottle is pleasantly cool in my hand.

    (Nothing ventured, nothing gained!)

    """

    play sound "/audio/gulp.mp3"    

    m """
    (I swallow the concoction, surprised by how easily it goes down.)

    (Despite its consistency, the taste is pretty inoffensive...{w}pleasant, even.)

    (It's no Starfruitbucks latte, but it isn't putrid mystery glue either.)

    """

    m """!!! Not bad, Joule. What's in it?

    (I'm hoping the answer isn't something like "5 pounds of raw chicken")

    """

    hide joule-neutral
    show joule-smile at hop

    j "“It's cooked chicken breast!”"
    m "(Feels so wrong to be right.)"
    j "“...also broccoli, egg whites, potato, oats and maple syrup.”"
    m """“...All such delicious ingredients!” {p}(Individually!)

    (Still, it's not as bad as I thought it'd be.) I take another gulp.

    """

    hide joule-smile
    show joule-thinking

    j "Menmi...I want you to be honest with me."
    m "“OK,”{w} I agree dishonestly."
    c "Menmi!"
    m "(It depends on what he asks!)"

    hide joule-thinking
    show joule-annoyed

    j "You didn't have breakfast, did you?"
    m """!!! {w}(Now that I think about it, I suppose I didn't.)

    “Um...do iced coffee and a breath mint count as breakfast?”

    """

    j "No."
    m """

    “Ehehehe....sorry, Joule. I forgot this morning.{w}” (I was busy getting ready for our park date!)

    (Joule just sighs, making my heart drop.)

    """

    hide joule-annoyed
    show joule-neutral

    j "“It's OK.{w} It's actually not unusual for my clients to miss breakfast.”"

    hide joule-neutral
    show joule-hardcore

    j "“Even though breakfast gives you energy and jump starts your metabolism{w}HARD. {w}CORE.”"

    hide joule-hardcore
    show joule-smile

    j "“I understand that people get busy, though, so I came prepared.”"
    hide joule-smile
    show joule-neutral

    m """Joule reaches into the bag again, pulling out a surprisingly cute lunch box. Neatly packed inside are triangular white packets wrapped in glossy seaweed. 

    “Are these...rice balls?”

    """
    hide joule-neutral
    show joule-smile
    j """“Yeah! Onigiri!{w} There's grilled salmon, tuna mayo, and pickled plum.”

    “I made plenty, so eat up!”

    """

    hide joule-smile
    show joule-wink

    j "“Think of this as a thank-you for tending to my ankle last time.”"

    hide joule-wink with dissolve

    m "He hands me a rice ball from the top of the pile, and I take it gladly, feeling its warmth radiate in my palm. My stomach rumbles in anticipation."

    show pinkgradient with dissolve
    hide pinkgradient with dissolve
    play sound "sparkle.mp3"

    m """“It's...{w}really good!”

    Each pebble of rice is chewy and perfectly seasoned, bringing out the creaminess of the tuna mayo.

    “It's soooo yummy!{w} You made these???”

    """

    show joule-neutral with softsmile

    j "“Mm-hmm.”"
    m """It's all he says for a bit, as I'm savoring bite after bite. I can't stop!

    “Joule?”

    """
    j "“Ah, sorry. {w}I was just thinking how nice it was to watch you enjoying the food.”"

    hide joule-softsmile
    show joule-smile

    j "“You eat with such passion!{w} Like you're really getting lost in the moment.{w}It's cute.”"
    m """A wave of warmth flushes through me as I look away.

    (It's a little embarrassing...{w}but also kind of nice.)

    """

    hide joule-smile
    show joule-surprised

    j "“Sorry! I didn't mean to make you feel self-conscious.”"

    hide joule-surprised
    show joule-neutral

    m """“No, it's OK. {w}I was just so surprised by how tasty it is. {w}The shake, too. I can tell they were made with love and care.

    You're a talented chef, Joule!”

    """

    hide joule-neutral
    show joule-awkward

    j "“Yeah, but just so you know...I cook because nutrition is a part of my job. {w}It's not like I like it or anything.”"

    m "(That seemed to have struck a nerve with him, but why?)"

    if hobbies == True:
        m "(Now that I think about it, he got kind of weird when I asked him about his hobbies before too.)"

    m "(Maybe I should ask him about it...)"

    hide joule-awkward
    show joule-surprised

    j "“Hold up...{w}Menmi.”"

    hide joule-surprised with dissolve

    
    m """Joule suddenly leans in close to me,{w} the heat of his body meeting mine as he brushes his hand up towards my shoulder.

    His face is so intense, a slight furrow in his brow mirrored by the curve of his lips.

    """

    show joule-sad
    j "“When did this happen?”"
    m "I snap out of it, looking to where Joule's hand is placed."

    scene park-day with vpunch
    m """(Ahh!! There's a tear in my windbreaker!)

    “Nooooo I just got this...”

    (I shrug the jacket off and stare woefully at the loose threads surrounding the hole. It's right at the shoulder seam.)

    “I must have snagged it on a branch...”

    (OOOooohhh Menmi you scatterbrains!!)

    """

    j "Can I see for a sec?"
    m "“Yeah...it looks real bad. I can't believe it's ruined.”" 

    hide joule-sad
    show joule-thinking
    j "Not necessarily. {w}It looks like it's mendable. {w}Do you have a sewing kit?"

    hide joule-thinking
    show joule-surprised
    m "Even if I did, I don't know the first thing about sewing."
    j "Huh...I kind of thought all girls knew how to sew."
    m "I mean, maybe 200 years ago...(I barely know how to button my blouses.)"
    hide joule-surprised
    show joule-thinking

    j "I think I might be able to help..."

    hide joule-thinking with dissolve

    m """Joule goes back into the bag again, rummaging around the pockets.{w} He pulls out a small pouch with sewing needles and thread.

    To my surprise, he threads the needle easily and begins dipping it in and out of the fabric with expert precision.

    """

    show joule-neutral with dissolve

    m "Wow -- you carry that around with you?"

    hide joule-neutral
    show joule-thinking at squirm

    j """No! It probably dropped into my bag...{w} from somebody else's bag. 

    I mean, somebody must have put it in there!

    ...
    """

    show joule-annoyed with vpunch

    j "I-it's useful to have sometimes!"

    hide joule-annoyed
    show joule-awkward

    m """(He got defensive again...{w}something is definitely up).

    (Joule seems to be good at lots of things that don't have to do with exercise,{w} so why does he seem so ashamed of it?)

    (I want to understand, but I have to approach this carefully.)

    """ 


    label choice_15j:
        menu:
            m "How should I discuss Joule's nervousness about his hobbies?" 

            "Be direct.":
                c "You just have to be honest and say what's on your mind!"
                m "Hey Joule...why are you getting defensive about your hobbies?"
                j "I'm not defensive!{W} YOU'RE defensive!"
                jump joule_defense
            "Make an observation.":
                c "If you frame it as a neutral observation, maybe he won't see it as a threat."
                m "Hey Joule, I notice that you seem a little self-conscious when we talk about your hobbies. "
                j "I'm {i}not{/i} self-conscious about {i}anything{/i}.{w} My heart rate is perfectly within resting range."
                m "(I don't know how I'd confirm that or how it relates to anything, but OK.)"
            "Ask about his feelings.":
                c "Hone in on the heart of the issue -- his {i}emotions."
                m "Joule...{w} do you feel ashamed of your hobbies?"
                j "WHAT! Of course not!"
                label joule_defense:
                    hide joule-awkward
                    show joule-annoyed with vpunch
                    j """
                    And they're {i}not{/i} hobbies.

                    Secondly, I do them out of necessity{w}. That's it.

                    I'm a young guy living by himself.{w} Why shouldn't I know how to cook and sew?

                    It's not like I have anybody else to do it for me.

                    """

                    m "(Gosh, that *really* struck the wrong chord.{w}I'd better change the subject)"
                    hide joule-annoyed
                    jump after_choice_15j

            "Lead with curiosity.":
                c "If he's getting defensive, it's because he feels threatened. Show him you don't mean any harm."
                m """(I have to make it clear that I'm coming from a place of understanding, not judgment.)

                You don't have to tell me if you don't feel like it, Joule...but I'm curious about how you came to be so good at cooking and sewing. 

                It's cool that you're so skilled with your hands!

                """

                hide joule-thinking
                show joule-surprised

                j "Really? You don't think it's weird for a guy to do this stuff?"
                m "Why would I think it's weird? {w}Don't guys wear clothes and eat too?"
                hide joule-surprised
                show joule-awkward
                j "Yeah...I guess that's true."

                hide joule-awkward
                show joule-neutral

                j """I learned how to sew from my mom. She's a seamstress. 

                I used to get into a lot of fights when I was younger,{w} and my clothes were always getting ripped.

                """

                m "So you started getting ripped too?"

                hide joule-neutral
                show joule-wink

                j "Look at you! {i}Ripped{/i} the words right out of my mouth, that's for sure."
                m "Haha (he seems to be feeling more comfortable)."

                hide joule-wink
                show joule-awkward
                j "Anyway, yeah. It was a hassle for my mom to always be repairing clothes for me, and we didn't have the money to replace them--"

                hide joule-awkward
                show joule-neutral

                extend "So it was just easier for me to learn how to fix them myself."

                hide joule-neutral
                show joule-softsmile

                j "To be honest, I...actually kind of enjoy it.{w} I like working with my hands and making things better."

                hide joule-softsmile
                show joule-blush

                j "It's just -- {w}I didn't want you to think I was soft and weak."
                
                m """

                (Poor Joule, it feels like he really thought I'd judge him for that.)

                Being able to sew doesn't mean you're weak! {w}It's resourceful and practical. There's nothing weak about it.

                You're repeatedly stabbing at something with a pointy needle and pulling the material back together!{w}That's HARD.{w}CORE.

                """

                hide joule-blush
                show joule-surprised

                j "Hmmm...I've never thought about it that way before...{w}Thanks, Menmi...for accepting me."

                $ joule_relationship +=10
                show screen relationship_up onlayer overlay
                play sound "/audio/awareness-ding.mp3"
                hide screen relationship_up

                m """

                Of course!

                (I didn't know Joule was so conscious about how people perceive him. {w}I thought it was just me...)

                (I feel like I understand him a little better now.)

                """

                $ renpy.notify("+5 Self-Awareness")
                $ self_awareness += 5

                hide joule-surprised

            "Drop it.":
                c "If he's bristling, he doesn't want you to know. It's none of your business."
                m "(I don't want to make Joule any more uncomfortable than he already is. {w}I'll just change the topic.)"

    label after_choice_15j:
        show joule-neutral
        m "You mentioned before that cooking is part of your job. What did you mean by that?"
        hide joule-neutral
        show joule-smile
        j """That's right. Nutrition is an integral component of your health. {w}It's important to optimize your macronutrient profile to optimize your workouts.

        The right balance of proteins, carbohydrates, and fats at the right time determines how much muscle you build over time.
        """
        hide joule-smile
        show joule-wink
        j "Ha...sorry...didn't mean to start nerding out on you like that."
        m "Don't be! It's interesting to listen to you talk about a topic you care about."
        hide joule-wink
        show joule-neutral
        j "Thanks. Let me know if I'm getting carried away, though. {w}There's nothing worse than being a vibe killer."
        hide joule-neutral
        show joule-wink
        j "Uptight just ain't right."

        hide joule-wink
        show joule-neutral

        j """

        “Anyway -- the impacts of nutrition are more than physical.”

        “Did you know, Menmi? {w}The connection between belly and brain are well documented.”

        “Most people think that of the body and brain as separate entities, but they're really interconnected. {w}Inextricable, even.”

        “I mean just think about it --{w} when you're hungry, you feel crummy. {w}And when you exercise, you feel great!”

        """

        hide joule-neutral
        show joule-surprised

        m "“And when I feel nervous, my tummy hurts -- like it's twisting itself into knots.”"

        hide joule-surprised
        show joule-smile

        j """

        “Exactly! Psychosocial factors can influence the movement of the GI tract. That's the gut-brain connection.”

        “Even the conscious act of eating breakfast - {w}thinking about what you're putting in your body vs consuming nutrients on autopilot--

        it can help you feel more in control of your life, {w}and that's empowering.”

        """

        m "I've never thought about it that way!"
        hide joule-smile
        show joule-hardcore
        j "Yeah! Pretty HARD{w}. CORE."
        hide joule hard-core with dissolve

        m """We sit in silence for a bit, listening to the sounds of bird chirping against the quiet rumble of traffic in the distance.

        Beside me, Joule gracefully dips his needle in and out of my jacket sleeve."""

        
        play music "<from 107>/audio/reaching-the-sky.mp3" volume 0.5
        show joule-park-sewing with dissolve:
            zoom 1.5
            ease 5.0 zoom 1.0

        m """

        (My time with Joule has taught me to view my body more conscientously.)

        (Not in a bad way, but with more awareness that the choices that I make mentally affects who I am physically.)
 
        (Joule's kinda like that, too --{w}contradictory, yet cohesive.)

        (He's always projecting the aura of a HARD. CORE. party boy jock, but he has a thoughtful and sensitive side, too.)

        (I hope I can get to know the real Joule someday...)

        """

        pause

        scene park-day with dissolve
        show joule-neutral with dissolve

        j "Alright, it's done."
        m """

        I take the windbreaker from him, admiring the tidy new row of blue stitches at the seam.


        Thanks, Joule! It looks even better than before.

        """

        hide joule-neutral
        show joule-smile

        j "I don't know about 'better', but--"

        hide joule-smile
        show joule-softsmile

        extend "I'm glad that I could fix it for you."
        m "Yeah. {w}Thanks for taking care of me today, Joule."
    
        $ joule_relationship +=10
        show screen relationship_up onlayer overlay
        play sound "/audio/awareness-ding.mp3"
        hide screen relationship_up

        hide park-day with dissolve


    $ j3=True
    $ week += 1
    jump week_2_4



  