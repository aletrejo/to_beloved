
label joule_date_3:
    play sound "/audio/pencil-write.mp3"
    hide screen open_planner
    hide screen open_insights
    scene city-morning with fade:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}Week [week]{/size}{/font}{/color}{color=#000000}{color=#000000}{font=JustAnotherHand-Regular.ttf}{size=200}\n Weekend!{/size}{/font}{/color}" at truecenter with wiperight
    pause
 ##Date 3: outdoors in the park near the gym. Joule prepares a lunch to thank Menmi for tending to him; becomes more vulnerable around her.
    

    play music "<from 9>/audio/happily-ever-after.mp3" fadein 0.5
    scene gym-inside with dissolve

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

   {i} Shame on me for disappointing him already...

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
