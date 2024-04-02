label week_1_morning:
    play sound "/audio/pencil-write.mp3"
    scene city-morning with fade:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}Week [week]{/size}{/font}{/color}{color=#000000}{font=JustAnotherHand-Regular.ttf}{size=200}\n Morning{/size}{/font}{/color}" at truecenter with wiperight
    pause

    play music "<from 9>/audio/happily-ever-after.mp3" fadein 0.5
    scene menmi-apartment-morning with dissolve
    show screen open_planner
    m """
    *Yaaaaawwwnnn* Good morning to the first day of the rest of my life!

    Gosh, I slept like a rock. I thought I'd be so nervous that I'd be up all night, but I guess I underestimated how draining the move would be.

    A morning workout should wake me right up!

    I pull on the cute crop top and shimmy into the patterned leggings I'd laid out the night before.

    I don't always plan my outfits, but this is my first time at a Mangottan gym. I need to look like a chic city girl to attract a cool city guy!

    Hehe...just thinking about it gets my blood pumpin'.

    """
label gym:
    scene gym-inside with dissolve
    m """
    Wow, so this is Planet Figness?

    Walking towards the water filling station, I can't help but notice how bright and new everything looks.

    There are already so many people here early in the morning!

    It's so admirable! But...am I 'mirin *too* much?

    """

    play sound "/audio/squeaky-toy-sad.mp3"

    m "Everyone here is built like raw chicken while I'm parading around with noodle arms."

    stop music
    play music "<from 13>/audio/cave-streams.mp3"
    play sound "/audio/impact-slam.mp3"

    scene gym-inside with vpunch:
        matrixcolor InvertMatrix(value=1.0)

    i "I can’t believe you thought you looked good this morning."

    m """I'm suddenly hyper aware of being *perceived*. Cool sweat coats my palms.

    Why am I doing this again? I don't belong here.

    I can't even stand correctly. Oh gosh, am I breathing weird?

    I'm spiraling.

    Calm down, Menmi.

    """

    scene gym-inside with vpunch:
        blur 24
    stop music
    play music "/audio/happily-ever-after.mp3"

label choice_5:
    menu:
        m "How should I think about this?"

        "I should’ve covered up more...":
            c "Why didn't you wear your teenage regretshirt? You're not ready for this yet..."
        "Time to start pumping iron":
            $ renpy.notify("+5 Self-Awareness")
            $ self_awareness += 5
            c "Everyone starts somewhere! Put in the work, rip out some reps, and get that bodyodyodyodody."

        "I look...great?":
            c "You know what they say – fake it ‘til you make it, hot stuff!"
            m "I don't *feel* hot. I feel exposed. Maybe that was too far a leap."

        "Nobody's judging me":
            $ renpy.notify("+10 Self-Awareness")
            $ self_awareness += 10
            c "You're being overly self-conscious. Nobody thinks about you as much as you think about you."
            m """
            They don't know what they're missing out on!

            But it's true...everybody's leading their own rich inner lives (is it privileged to assume everybody's inner lives are rich?) """



label behemoth_incident:
    scene gym-inside with hpunch

    m "All of a sudden, I’m jolted out of my thoughts by a harsh voice."
    be "“Hey, brat. Quit hogging the watering hole.”"
    m "!!! I spin around, coming face-to-chest with a massive dude with a jutting brow and barrel-big arms."

    play music "<from 9>/audio/faked-desire.mp3" fadein 1.0
    show behemoth with dissolve

    m """He’s scowling at me like I’d snatched his wooly mammoth bone.

    I grab my water bottle and step out of the Behemoth’s way.

    “Oops! Sorry, it’s all yours.”

    The Behemoth grunts and slams his empty water bucket under the spout.
    """
    stop music fadeout 1.5
    scene gym-inside with vpunch
    show behemoth
    play sound "/audio/impact-slam.mp3"

    m "A few measly drops trickle out before the tap runs dry."

    $ behemoth_name = "Behemoth"

    be "“Tch. You used up all the water. Selfish brat.”"

    m """He turns toward me, leveling me with a beastly glare.

    He’s frightening, but I feel a little bad for emptying the cooler. It’s not his fault that the water ran out.

    “If you want, I can pour you some of mine.”

    I don’t mind sharing what I have with him if it helps.

    """

    play music "<from 9>/audio/faked-desire.mp3" fadein 2.0

    be "“...Sure.”"

    m """

    I release the breath I didn’t know I’d been holding in.

    “Great! I’m glad we could resolve-” """

    be "“But I don't want it in my bottle.”"

    play sound "/audio/monster-growl.mp3"

    hide behemoth
    show behemoth-smile

    m "A wide grin creeps its way across his face. Predatory."

    m """

    I don’t like the way he’s looking at me.

    “What do you mean?” I'm trying to keep my voice level.

    """

    be "“I want to drink from yours.”"

    play sound "/audio/impact-slam.mp3"
    scene gym-inside with vpunch
    show behemoth-smile


    m """

    A shudder runs through me.

    “M-mine?” Excuse me? Is this total stranger really asking to put his mouth on *my* Stanlychee water bottle?

    The thought of his viscous saliva slobbering over the mouth of my bottle makes my stomach churn...

    Does he know that he’s basically asking for an indirect kiss?

    """

    be "“Well? It’s just a drink...are you going to be a good girl or what?”"

    m """ What a nauseating man.

    Take it easy, Menmi. Don’t want to barf at the gym on your first day.

    """

label choice_6:
    menu:
        m "What should I do?"

        "Comply and get it over with":
            c "Do you really think he'll leave you alone if you give him what he wants? You'd just be encouraging him."
            m "The thought of allowing him to get away with harassment...it just makes me feel small and ashamed."
            c "Did you do something to deserve this?"
        "Politely, but firmly decline":
            c "Put him in his place with a polite, but firm “No.” There's no need to engage with this guy anymore than you already have."
            m "I know that that's the right course of action, but why does it feel so scary? The way he’s staring me down...I don’t know, I feel like something bad’s going to happen if I make him mad..."
        "If he wants a tongue-lashing, I'll give it to him":
            c "Don't let him talk to you like that! Who cares if he's humongous? You can take him!"
            m "“I don't know how you can be so thirsty when you're clearly drinking your own Kool-Aid.”"
            be "Why you-!"
            m """
            Out of nowhere, the Behemoth seizes my arm in his massive fist.

            Ah, it hurts...
            """
        "Ignore him and walk away":
            c "Any further engagement with this loser will only provoke him. Let's go."
            m "Easier said than done...it's not like I can just hop over this human wall."

play sound "/audio/impact-slam.mp3"
scene gym-inside with vpunch:
    matrixcolor InvertMatrix(value=1.0)
stop music fadeout 2.0

label joule_introduction:
    play sound "/audio/heartbeat-fast.mp3"
    m """
    It's like there's no right answer. This feeling of powerlessness is so frustrating...

    What should I do? Fight? Run? Call the manager?

    It's hard to think over the relentless thrumming of my heart."""

    stop sound fadeout 1.0

    scene gym-inside with hpunch
    play music "<from 22>/audio/joules-theme.mp3" volume 0.7


    j "“Leave her alone.”"
    m "Huh? Who said that?"
    show joule-neutral with dissolve
    j "“Hey, Beast Mode. Can I help you with a Cool Down routine?”"

    show behemoth at left with vpunch
    be "“What did you say, Shrimp-Fried Rice?”"
    m """
    The guy standing in front of me is wearing a sleeveless shirt with the gym's logo on it. The ID card around his neck indicates that he works here.

    He's smaller than the Behemoth, but there's no fear at all in his defiant posture.
    """
    show joule-annoyed

    j "“She's clearly uncomfortable. Is that any way for a real man to act?”"
    m """
    The Behemoth growls, veins rising in his biceps like a mountain range.

    He glances at the guy's ID card, though, and releases his grip.
    """
    be "“Tch. Talk about crap service. What kind of shitty gym runs out of water on paying customers?”"
    j "“I've already alerted the appropriate personnel. This station should be refilled within the next few minutes.”"

    hide joule-annoyed
    show joule-smile

    j "“Thanks for your patience, sir.”"
    m """
    His tone is professionally polite, but his smirk says otherwise...

    The Behemoth audibly grumbles, but backs off. """

    hide behemoth with dissolve
    m "The tension in my shoulders releases."

    hide joule-smile
    show joule-neutral

    j "“You OK? My name's Joule. I'm a trainer here.”"
    $ joule_name = "Joule"
    m "“Yeah, thanks for that.”"
    j "“No worries, but could I give you a piece of advice?”"
    m "I tense up, bracing myself for the reprimand."
    m "“Sure, what's up?”, hoping I sound as cool as he does."

    show joule-annoyed
    j "“You should be more careful. He put you in a really dangerous position. Judging by your build, there's no way you could have taken him if things got physical.”"
    m """
    He's not *wrong*, but the way he's scolding me rubs me the wrong way.

    Sure, this guy just "saved" me, but he can't be blaming *me* for this, right?
    """

    stop music fadeout 15.0

label choice_7:
    menu:
        m "How should I respond?"

        "Speak up":
            $ renpy.notify("+10 Self-Awareness")
            $ self_awareness += 10
            c "Stand up for yourself! That other dude was dangerous, but this guy seems like he'd be willing to hear you out."
            m """
            A sudden wave of shame and fury washes over me as I remember the powerlessness of the moment.

            I won't be able to live it down if I don't correct him now.

            "It wasn't my fault! I was just minding my own business when he approached me."

            "It shouldn't be on the victim to change their behavior here! There was nothing I could say or do that would level out the power imbalance."""

            hide joule-annoyed
            show joule-thinking

            m "I can see him trying to lift this concept...mentally."

            hide joule-thinking
            show joule-neutral

            j "...You're right. I'm sorry that I implied that it was on you to change. That's not fair to you."

            m "It's not ideal, but his apology makes me feel slightly better about the situation."

        "Apologize":
            c "This guy just did a nice thing for you. Don't ruin it by being ungrateful"
            m """
            I feel bad about making a scene, but was this really even my fault?

            I push down my frustration. It's better to keep the peace.

            "Sorry I caused you trouble."
            """
            j "It's OK — I'm glad you're alright"
            m "A part of me throws up, then dies a little, then throws up AGAIN."
        "Walk away":
            c "Uncomfy feelings?! In *my* body? Disengage."
            m "I try to walk away, but he grabs my hand."
label joule_response:
    play music "<from 21>/audio/reaching-the-sky.mp3" fadein 1.0
    hide joule-annoyed
    show joule-sad
    j "“You were scared, weren't you? I'd be, too”"
    m "The look in his eyes...it's kind of sad."
    m "Something tells me this guy is just trying to help."

    hide joule-sad
    show joule-neutral
    j "“I'm not trying to shill my services or anything, honestly, but if you ever want to do something about your strength, just give me a ring.”"
    m """
    He pulls out a business card and hands it to me. There's a black and white photo of him on it, the hard lighting capturing every line and contour of his chiseled build.

    He's kind of hot. Once you get over the patronizing remarks.

    There *is* something romantic about a high octane situation rescue situation from a lecherous troll.

    """
    i "*Definitely* sounds like something your inner feminist would say."

    if self_awareness >=10:
        play sound "/audio/awareness-ding.mp3"
        show text "{image=ol_text}" with easeinbottom
        pause
        hide text with dissolve
        $ passed_checks +=1
        m "Maybe my inner feminist wants me to to get swole and squat punch creeps."
    elif self_awareness<10:
        m "Grrrr...stop it, Menmi! You're not supposed to *like* getting rescued. What's wrong with you?"

    m "Thanks. I'll think about it."
    j "“Girls should know how to protect themselves...especially the pretty ones.”"
    hide joule neutral with dissolve
    scene gym-inside with dissolve:
        blur 24
    m """
    Against my better instincts, my heart is racing a mile a minute.

    Looks like he's helping me with cardio already.
    """

    stop music fadeout 5.0
    jump week_1_day
