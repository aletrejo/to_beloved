
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

    m "(Fashion {i}and{/i} function! Who says I'm scatterbrained? Let's go!)"

    scene park-day with slideleft

    m "When I arrive at the park, Joule is already there waiting for me."

    show joule-smile with dissolve
    play music "<from 22>/audio/joules-theme.mp3" volume 0.7

    j "“Morning, Menmi!"

    hide joule-smile
    show joule-surprised

    j "“Woah! Cool jacket!"
    m """“Thanks!{w} Aren't you cold, though?”

    Joule's in his usual {i}Planet Figness{/i} sleeveless shirt.

    """

    hide joule-surprised
    show joule-neutral

    j "“Nah, I tend to overheat easily.{w} Especially when I'm physically exerting myself.”"

    hide joule-neutral
    show joule-thinking

    j "“Truth be told, {w}I don't wear a top at all when I'm working out by myself.{w} I'm kind of Anti-Shirt like that.”"
    m "(He said that so casually, but my face is overheating just imagining it.)"

    hide joule-thinking
    show joule-neutral

    j "“Anyway, I thought it'd be fun to change things up a bit today and do some cardio in the park.”"
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

    m """“Joule takes me by the hand gently and leads me to a green clearing beneath the shade. 

    His palm is cool and surprisingly soft.

    It's early on the weekend so there aren't many people around.

    Joule pulls a {i}Planet Figness{/i} duffle bag out of the bushes.

    ??? “{w}Where did that come from???”
    """

    show joule-smile at dissolve

    j "“Haha -- don't worry. {w}I dropped it off earlier before you got here.”"

    hide joule-smile
    show joule-neutral

    j "“It's not a random shady duffle filled with drugs or anything, {w}if that's what you're thinking.”"
    m """(I was not thinking that.)

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

    j "“After a workout, it goes {w}HARD. {w} CORE.”"

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

    j "It's OK.{w} It's actually pretty common for clients to miss breakfast."

    hide joule-neutral
    show joule-hardcore

    j "Even though breakfast gives you energy and jump starts your metabolism{w}HARD. {w}CORE. "

    hide joule-hardcore
    shouw joule-smile

    j "I thought this might happen, so I came prepared."
    hide joule-smile
    show joule-neutral

    m """Joule reaches into the bag again, pulling out a few white triangular packets that fit into my palm.

    Are these...rice balls?

    """
    hide joule-neutral
    show joule-smile
    j """Yeah! Onigiri!{w} There's chicken, tuna mayo, and pickled plum.

    I made plenty, so eat up!

     """












    





    j """

    “Most people underestimate how important breakfast is to a healthy body...and a healthy mind.”

    “Did you know, Menmi? {p}The connection between belly and brain are well documented.

    Most people think that of the body and brain as separate entities, but they're really interconnected. {p} Inextricable, even.

    I mean just think about it -{p} when you're hungry, you feel crummy. {p} And when you exercise, you feel great!

    """

    hide joule-neutral
    show joule-shocked

    m "“And when I feel nervous, my tummy hurts -- like it's twisting itself into knots.”"

    hide joule-shocked
    show joule-smile

    j """

    “Exactly! Psychosocial factors can influence the movement of the GI tract. That's the gut-brain connection.”

    “Even the conscious act of eating breakfast - {p}thinking about what you're putting in your body vs consuming nutrients on autopilot -

    it can help you feel more in control of your life, {p}and that's empowering.”

    """

    m "{i}He makes some good points...{p}Is Joule actually...really smart?"

    



  