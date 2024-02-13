label week_1_night:
    play sound "/audio/pencil-write.mp3"
    scene city-night with dissolve:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}Week 1{/size}{/font}{/color}{color=#000000}{font=JustAnotherHand-Regular.ttf}{size=200}\n Night{/size}{/font}{/color}" at truecenter with wiperight
    pause

    play music "<from 9>/audio/happily-ever-after.mp3" fadein 1.0
    scene city-night with dissolve
    m "“Aahhh, it's finally over! Work is finally over!”"
    show allie-smile with dissolve
    al "“Time to drink booze, let loose.”"
    m "“Yes, please! There's a place I've been meaning to check out. One of my friends from home is a bartender there!”"
    al "“You don't say? Sounds like an opportunity for free drinks. Let's go!”"

label naji_introduction:
    scene lounge-outside with dissolve
    show allie-neutral at right with dissolve
    m "“I think this is it – The William Collins”"
    al "“Ooh la la...a cocktail lounge. You've got some fancy friends.”"
    m """
    “Haha Naji's just a regular guy! We were neighbors growing up.”

    “He's the most unpretentious person you'll ever meet.”

    Although hanging out at an upscale establishment certainly improves my chances of meeting a dashing gentleman who'll sweep me off my feet...
    """

    if self_awareness <=30:
        stop music
        play sound "/audio/impact-slam.mp3"
        play music "<from 13>/audio/cave-streams.mp3"
        scene lounge-outside with vpunch:
            matrixcolor InvertMatrix(value=1.0)
        i "If you don't trip over your tongue first."
        m "I can pronounciate words just fine!"
        play music "<from 20>/audio/happily-ever-after.mp3"
        scene lounge-outside
        show allie-neutral at right

    m """
    I hold out my hand to Allie and bow obsequiously.

    “Shall we?”
    """
    al "“Let's.”"
    scene lounge-inside with dissolve
    stop music fadeout 2.0

    m "“Wow, look at this place. Doesn't it just scream ‘romance’?”"

    play music "<from 9>/audio/monkey-business.mp3"

    "Rowdy Patron" "“Oh yeah? Just try to touch me, tough guy. I freakin' dare ya!”"
    "Unruly Guest" "“I wouldn't touch you if you were a Kopenhagen mink coat!”"

    show allie-neutral at right with dissolve

    al "“It's screaming something, that's for sure.”"

    hide allie-neutral with dissolve

    m "What's going on? A fight?"
    "Unruly Guest" "“I saw you knock over my drink on purpose! I demand payment for the cleaning of my Louboutins!”"
    "Rowdy Patron" "“Looking down on me, eh? I'll have you know I own SEVEN Bouloutins.”"
    "Unruly Guest" "“I don't care how many Louboutins you own, just give me my money!”"

    stop music fadeout 5.0

    m """
    A crowd is gathering around the ruckus, servers and customers looking on in transfixed horror.

    Someone's got to do something.

    Before I can even start to formulate a plan, a firm voice calls out.
    """

    play music "<from 50>/audio/najis-theme.mp3"

    show naji-bar-neutral with dissolve
    n "“Good evening, gentlemen.”"
    m """
    Naji!

    I want to call out to him, but this doesn't feel like the right moment.
    """
    $ naji_name = "Naji"
    n """
    “If you don't mind me cutting in, I saw the whole thing from the bar.”

    “I'm sorry that your new shoes were caught in an accident, sir. Those were a gift from your late nephew, weren't they?”
    """
    "Unruly Guest" "“Y-yes, he was always on the cutting edge of fashion, you know? A little hype bee, that one.”"

    hide naji-bar-neutral
    show naji-bar-frown

    n "“Hype beast,” Naji clarifies."
    "Unruly Guest" "“Poor boy, he was strangled by his own shoelaces when they got caught in an airplane turbine. Flown so young.”"
    n "“So fly.”"
    m "“Why was he wearing shoelaces around his neck?”"

    show allie-neutral at right with easeinright

    al "“Neckshoeties. So hot right now.”"

    hide allie-neutral at right with easeoutright

    "Unruly Guest" "“I'm surprised that you remember that, Naji. I told you that a while ago.”"

    hide naji-bar-frown
    show naji-bar-smile

    n """
    “It's part of a bartender's job to listen to their customers.”

    “And from what I observed about the incident at hand, it was an accident. This fellow was picking up your wallet and knocked your drink over on the way up.”

    “You know what they say – ‘No good deed goes unpunished’. It must have been frustrating to be wrongly accused, but we can talk this out.”
    """
    hide naji-bar-smile
    show naji-bar-neutral

    "Rowdy Patron" "“Yes! That's exactly what happened. Thank you. Here, your wallet.”"
    "Unruly Guest" "“!!! I hadn't even noticed I'd dropped it. I'm so embarrassed – I was blaming you when this whole thing was caused by my own carelessness...”"
    "Rowdy Patron" """
    “That's alright, man. I'm sorry I got heated. It's just that...everybody always assumes I'm up to no good just because of my face.
    I just get defensive, is all.”"""
    "Unruly Guest" "“No offense taken. And for what it's worth...there's nothing wrong with your face.”"
    "Rowdy Patron" "“Hey...you wanna go somewhere? Grab a drink or something?”"
    "Unruly Guest" "“I-I've already had a couple.”"
    "Rowdy Patron" "“Not one on me, you haven't.”"

    hide naji-bar-neutral with dissolve

    m "I can hardly believe it, but the two walk out smiling."
    show allie-neutral with dissolve
    al "“Wow...that guy's got a way with people.”"
    m "Is that guy...really my friend?"
    hide allie-neutral with dissolve
    m """
    Allie's not the only one who's impressed. Several of the bar patrons and staff crowd around Naji, patting him on the back and showering him with praise.

    I overhear a waitress talking to a customer swirling a dirty martini.
    """
    "Customer" "“The new guy's charming, isn't he? Easy on the eyes, too.”"
    "Waitress" "“You don't even know. He's been picking up shifts, settling disputes, even helping folks out with their personal errands. We all love him here!”"
    "Customer" "“There's no way a guy like that's single.”"
    "Waitress" "“You'd be surprised. I've never seen him bring anyone around.”"

    stop music fadeout 2.0

    m """
    It feels a little strange to hear about Naji from their perspective.

    I mean, this is the kid who ate leaves with me off of our neighbors' bushes because I told him that's where salad came from."""

    play music "<from 69>audio/cave-streams.mp3" fadein 1.0

    m "I've never thought about him like that before..."


    scene lounge-inside:
        blur 24
    m """
    I look down at myself, suddenly hyper-aware of the coffee stain on my Ham Taylor blouse.

    I'm no hype bee.
    """
    al "“Hey, Town Hero over there is your friend, right? Aren't you going to say ‘hi’?”"
    m "But he's surrounded by all those people. What if he thinks I'm annoying?"
label choice_9:
    menu:
        m "What should I do?"

        "Call out to Naji":
            $ renpy.notify("+5 Self-Awareness")
            $ self_awareness += 5
            c """
            Naji is expecting you. You came here to see him. Why wouldn't he want to see you, too?

            He's been your friend for...how long have you been avoiding salads?
            """
            stop music fadeout 2.0
            play music "<from 16>/audio/najis-theme.mp3" fadein 1.0
            m "I'm getting too into my own head over this. I need to snap out of it."
            $ renpy.notify("+5 Self-Awareness")
            $ self_awareness += 5
            $ naji_relationship += 5
            m "“Hey, Naj! Over here!”"
            call choice_9a from _call_choice_9a
            jump after_choice_9
        "Wait for Naji to come over":
            c "Don't get in his way. He'll see you eventually. Wait for him."
            m """
            And just...stare at him until he comes over? Very cool, very suave, Menmi.

            Why do I feel so weird about calling out to him?

            Normal people wouldn't think twice about this. Why am I so *painfully* awkward?
            """
            call choice_9bc from _call_choice_9bc
            jump after_choice_9
        "Don't bother him":
            c "He's busy. What makes you think you're worthy of his attention right now?"
            m "I'd better not bother him..."
            call choice_9bc from _call_choice_9bc_1
            jump after_choice_9

label choice_9a:
    scene lounge-inside with dissolve
    show naji-bar-neutral with dissolve
    m "Naji turns around, expression transforming as he registers my voice."
    hide naji-bar-neutral
    show naji-bar-smile
    n "“Menmi! You're here!”"
    hide naji-bar-smile
    show naji-bar-neutral
    m """
    His face is more angular, but his eyes shine the same way they did when he used to peek out at me from behind the curtains of the house across the street.

    “Nice negotiation skills, bud. Where were those when we got grounded for tattooing my parents' couch?”
    """

    hide naji-bar-neutral
    show naji-bar-laugh

    n "“In our defense, it had arms”"
    m "“So did those hooligans who were just here. I thought I was about to witness my first city bar brawl.”"
    return

label choice_9bc:
    scene lounge-inside with dissolve
    show allie-neutral with dissolve
    stop music fadeout 2.0
    play music "/audio/najis-theme.mp3"
    m """
    I try to chat with Allie about work, but their eyes remain trained on Naji.

    I don't know why I feel sad about that. Who wouldn't be in awe of him?

    Allie holds out their hand, enthusiastically waving over the bar.
    """
    al "“Yoo-hoo! Can we get some service down here?”"
    hide allie-neutral with dissolve
    show naji-bar-smile with dissolve
    n "“Of course! Thanks for waiting–”"
    hide naji-bar-smile
    show naji-bar-surprise
    n "“Menmi? How long have you been here?”"
    m "Naji blinks at me. He seems surprised."
    n "“Why didn't you say ‘hi’?”"
    m "“Ah, I didn't want to disturb you while you were...busy”"
    if self_awareness <=30:
        stop music
        play sound "/audio/impact-slam.mp3"
        play music "<from 13>/audio/cave-streams.mp3"
        scene lounge-inside with vpunch:
            matrixcolor InvertMatrix(value=1.0)
        i "Way to be weird."
        play music "<from 20>/audio/happily-ever-after.mp3"
        scene lounge-inside
        show naji-bar-surprise
    return

label after_choice_9:
    hide naji-bar-laugh
    show naji-bar-neutral
    n "“Oh, that? It wasn't a big deal.”"
    n "“You'd do the same.”"
    m """
    His smile is so warm.

    “Naj. This is my friend, Allie. New friend, meet old friend. Old friend, new friend.”
    """
    al "“It's an honor to be served a cosmo by a local hero.”"
    m "Smooth way to order a drink."

    hide naji-bar-neutral
    show naji-bar-smile

    n "“Ha - copy that.”"
    m "Naji's cheeks dimple as he smiles to himself and makes Allie their drink."
    n "“Enough about me. How have you been, Menmi? Today was your first day of city life, wasn't it?”"
    m "“It's been eventful!”"

    hide naji-bar-smile
    show naji-bar-surprise

    m "“A personal trainer gave me his card, and my mysterious boss might moonlight as a model.”"
    al "“It's true — we've seen him lunch with Heidi Plum.”"
    m "I pretend not to notice Naji fumble the tumbler he's pouring out of."

    hide naji-bar-surprise
    show naji-bar-smile

    n "“Is that so? Glad to hear it.”"
    m """
    The smile's still plastered to his face, but there's a flatness to his tone that feels off.

    As Naji wipes down the already spotless counter in front of me, I debate whether to press him on it.
    """

label choice_10:
    menu:
        m "What should I do?"

        "Ask Naji about his feelings":
            label choice_10a:
            c "He won't tell you what's bothering him if you don't ask."
            m """
            Naji's never been the most transparent about his feelings.

            “Did I say something to upset you, Naji?”
            """
            hide naji-bar-smile
            show naji-bar-surprise
            m "His boyish curls seem to stiffen."
            if naji_relationship <=0:
                jump choice_10a_deflect
            if naji_relationship >0:
                jump choice_10a_honest
        "Change the subject":
            label choice_10b:
            c "This doesn't seem like the right time to probe. You've just reunited after a long time apart, after all. Who knows what's going on with him?"
            m """
            Naji's never been the most forthcoming about his feelings.

            It might be too early to discuss something he doesn't want to talk about.

            Besides, am *I* even sure I want to know?

            Better to keep things light...for now, at least. """
            $ renpy.notify("+5 Self-Awareness")
            $ self_awareness += 5
            jump after_choice_10
        "Feel him out":
            c "He's not saying how he really feels, but you don't want to harsh the vibe when you've only just reunited."
            m """
            I watch Naji closely.

            At a glance, his smile seems to come easily as he serves Allie their drink, but there's a stiffness to his motions that wasn't there before.

            He seems focused on not looking my way. """
            menu:
                "Probe Naji":
                    jump choice_10a
                "Drop it":
                    jump choice_10b

    label choice_10a_deflect:
        hide naji-bar-surprise
        show naji-bar-neutral
        n "“Course not. If anything, I'm more offended you didn't bring your new friends to meet me.”"
        m """
        He totally just dodged the question. With a joke.

        Oh well, I'll have to meet him where he's comfortable. Back to baseline banter.

        “You didn't give me enough backstage passes to the show.”"""

        hide naji-bar-neutral
        show naji-bar-smile

        m "He seems to like that."
        n "“Do I look like an idol to you?”"

        show allie-neutral at right with easeinright
        al "*Sips drink*"
        hide allie-neutral at right with easeoutright
        m "“More like a comedian.”"

        hide naji-bar-smile
        show naji-bar-surprise

        m "Naji's eyes widen in mock shock as he clutches at his “broken” heart."

        jump after_choice_10


    label choice_10a_honest:
        hide naji-bar-surprise
        show naji-bar-lookaway
        n "“Nothing...it's just...”"

        hide naji-bar-lookaway
        show naji-bar-neutral

        n "“It caught me off guard to hear that you've met so many potential love interests.”"
        m "!!! “I never said I was trying to *date* them.”"
        n """
        “Oh come on, Menmi. You've been in love with 'love' since before 'puberty' even entered our vocabulary.”

        “Remember all those Fishney princess movies you used to make me watch with you?” """

        m """
        “Don't assume things about me!”

        “Besides, better a lover than a hater.”

        I stick my tongue out at him. I know it's immature, but Naji tends to bring out this side of me.
        """


label after_choice_10:
    hide naji-bar-smile
    show naji-bar-neutral
    m "“Remember when you used to make me watch all your *hilarious* stand-up comedy specials?”"
    hide naji-bar-neutral
    show naji-bar-surprise
    n "“Hey, they were funny!”"
    m "“Nobody who's actually funny has to actually try that hard.”"
    hide naji-bar-surprise
    show naji-bar-neutral
    n "“Oh yeah? Explain this then.”"
    hide naji-bar-neutral with easeoutbottom
    m "Naji slowly lowers himself behind the bar into a crouch."
    n "“Menmi, you set the bar too damn high.”"
    m "An involuntary chortle forces its way out of my throat."
    m """
    “You're right...truly inexplicable behavior.”

    The familiar comfort I feel around Naji me forget all about the awkwardness from before."""

    show naji-bar-laugh with dissolve
    stop music fadeout 5.0

    m """
    What was I thinking? This was my old friend. The fact that he's popular in the dating pool shouldn't change anything...

    I think.
    """


    if self_awareness <=30:
        stop music
        play sound "/audio/impact-slam.mp3"
        scene lounge-inside with vpunch:
            matrixcolor InvertMatrix(value=1.0)
        i """
        Maybe it's something you should keep in mind...just in case.

        Don't want to make a fool of yourself...though that might not be avoidable even if you tried.
        """

    scene lounge-inside
    play music "<from 22>/audio/happily-ever-after.mp3" fadein 1.0
    show naji-bar-smile
    m """
    We spend the rest of the evening chatting companionably over delicious cocktails Naji whips up like some sort of mixed drink magician.

    At some point around midnight, we said goodbye to Naji, and I stumbled home singing to myself, feeling as bubbly inside as the nightcap I just downed.

    So this is life in Applecore City? Maybe it's not all sunshine and rainbows, sure, but that's why I've got to work hard!
    """
    scene city-day with fade
    m """
    The rest of the week flew by so quickly, I barely have a chance to register what was going on.

    Gym in the mornings...work all day...the occasional trip to the Collins' when I'm not too beat.
    """
    scene city-night with dissolve
    m "It's a whirlwind of activity, but I find the blistering pace intoxicating."
    jump weekend_1
