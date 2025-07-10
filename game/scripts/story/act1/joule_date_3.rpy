
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

    m "(Fashion {i}and{/i} function! Talk about cute! Let's go!)"

    scene park-day with slideleft

    m "When I arrive at the park, Joule is already there waiting for me."

    show joule-smile with dissolve
    play music "<from 22>/audio/joules-theme.mp3" volume 0.7

    j "Morning, Menmi!"

    hide joule-smile
    show joule-surprised

    j "Woah! Cool jacket!"
    m """Thanks!{w} Aren't you cold, though?

    Joule's in his usual {i}Planet Figness{/i} sleeveless shirt.

    """

    hide joule-surprised
    show joule-neutral

    j "Nah, I tend to overheat easily.{w} Especially when I work out."

    hide joule-neutral
    show joule-thinking

    j "I don't wear a top at all when I'm training by myself.{w} I'm kind of Anti-Shirt like that."
    m "(He said that so casually, but my face is overheating just imagining it.)"

    hide joule-thinking
    show joule-neutral

    j "Anyway, I thought it'd be fun to change things up a bit today and do some cardio in the park."
    m "I'm wearing my running sneakers and ready to run-ble."

    hide joule-neutral
    show joule-wink

    j "You have a great attitude, as usual!{w} Let's get going -- follow me!"

    hide joule-wink with dissolve

    scene park-day:
        blur 50

    m """Joule and I set off on a lap around the park at a steady pace. 

    Every so often, Joule checks in on me behind him, adjusting his pace to match mine.

    The scenery and people rush by, {w}but I focus on chasing Joule, his navy blue tank billowing as the wind blows its way across his back. 

    He doesn't seem to tire, which makes me push myself even harder to keep up.

    (It's getting harder to breathe, though...)
    """

    scene park-day with flash:
        matrixcolor BrightnessMatrix (value=0.4)
    show joule-sad with dissolve

    j "Woah. Hey, Menmi -- you good? {w}Let's take a break here."

    #picnic basket tucked into the bushes













    



    play sound "/audio/stomach-growl.mp3"
    m """{i}Ummm....did I just say that out loud?

    Stupid, traitorous body!

    I was panicking so much this morning that I totally forgot to eat breakfast.

    Although my usual iced coffee and a breath mint hardly counts as breakfast, I guess...

    """   

    show joule-smile with dissolve
    j "“Tsk tsk, Menmi. Don't tell me you were planning on working out on an empty stomach!”"

    m """

    “I know! I know! It's just that I was so busy and all...”

    """

    hide joule-smile
    show joule-neutral

    j """

    “Hey, no worries.{p} I was just kidding around.”

    “Lots of my clients forget breakfast.{p} That's why I come prepared.”

    """

    show joule-thinking at squirm

    m "Joule reaches into his bag and hands over a clear bottle filled with some kind of beige slush."

    hide joule-thinking
    show joule-smile

    j "“This is my GO! Morning protein shake. It's got a heavy duty amino acid profile that'll fortify your muscles."

    hide joule-smile
    show joule-neutral at hardcore

    j "For a HARD. {p} CORE. {p} workout.”"

    m """

    I wonder if it ever hurts him to hit his abs every time he says that.

    I take the drink from him. {p} While I'm flattered that he put so much thought into our session, the sticky-thick concoction is anything but a bacon of gustatory delight.

    Gosh, I would *kill* for some bacon right now.

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

    show protein-shake with easeinbottom

    m """

    The protein shake feels pleasantly cool in my hand.

    {i} Nothing ventured, nothing gained.

    """

    hide joule-smile with dissolve

    play sound "/audio/gulp.mp3"    

    m """
    I swallow the concoction, surprised by how easily it goes down.

    Despite its consistency, the taste is pretty inoffensive. 

    It's no Starfruitbucks latte, but it isn't putrid mystery glue either.

    """

    show joule-neutral

    m """
    “Not bad. {p}What's in it?”

    Keeping my fingers crossed that the answer isn't something like "3 lbs of chicken breast"
    """

    j "“Ah, you're asking the right questions.”"

    show joule-smile

    j "“It's cooked chicken breast!”"
    i "{i}Feels so wrong to be right."
    j "“...also broccoli, egg whites, potato, oats and strawberry jam for flavor.”"
    m """“...All such delicious ingredients!” {p} Individually!

    """
