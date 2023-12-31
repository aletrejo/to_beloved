label week_1_morning:
    scene image Solid("#ffc6ebff") with dissolve
    show text "{font=fredoka}{size=288}Week 1 \nMorning{/size}{/font}" at truecenter with dissolve
    pause
    scene menmi-apartment-morning with dissolve
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

    Walking towards the water filling station, I can't help but notice how bright and new everything looks, and there are already so many people here early in the morning!

    Everyone here is ripped! I glance at my own figure in the mirror... and cringe.

    Yikes! I gotta firm up these noodle arms!

    Conscience
    I can't believe you thought we looked good this morning.
    """
    scene gym-inside:
        blur 24
    menu:
        m "How do I feel about this?"

        "I should've covered up more...":
            c "Why didn't you wear a sweatshirt? You're not ready for this yet..."
        "Time to start pumping iron":
            $ renpy.notify("+5 Self-Awareness")
            $ self_awareness += 5
            c "Everyone starts somewhere! I have to put in the work, do those reps, and get that bodyodyodyodody."
        "I look great!":
            c "You know what they say – fake it 'til you make it, hot stuff!"
            m "I don't {i}feel{/i} hot, though. I feel exposed. I can't deny *that*."
        "Nobody's judging me":
            c "You're being overly self-conscious. Nobody thinks about you as much as you think about you"
            $ renpy.notify("+10 Self-Awareness")
            $ self_awareness += 10
            m "It's natural to feel self-conscious, but people are probably more preoccupied with their own problems than with me."
    scene gym-inside with vpunch
    m "All of a sudden, I'm jolted out of my thoughts by a harsh voice."
    be "Hey, brat. Quit hogging the watering hole."
    m """
    !!! I spin around, coming face-to-chest with a massive dude with a jutting brow and barrel-big arms.

    He's scowling at me like I'd snatched his wooly mammoth bone.

    I grab my water bottle and step out of the Behemoth's way

    “Oops! Sorry, it's all yours.”

    The Behemoth grunts and slams his empty water bucket under the spout.
    """
    with hpunch
    m "A few measly drops trickle out before the tap runs dry."
    $ behemoth_name = "Behemoth"
    be "Tch. You used up all the water. Selfish brat."
    m """
    He turns toward me, leveling me with a beastly glare.

    He's frightening, but I feel a little bad for emptying the cooler. It's not his fault that the water ran out.

    “If you want, I can pour you some of mine.”

    I don't mind sharing what I have with him if it helps.
    """
    be "...Sure"
    m """
    I release the breath I didn't know I'd been holding in.

    “Great! I'm glad we could resolve-”
    """
    be "But I don't want it in my bottle."
    m """
    A wide grin creeps its way across his face.

    I don't like the way he's looking at me.

    “Wh-what do you mean?”
    """
    be "I want to drink from yours."
    with hpunch
    m """
    “M-mine?” Excuse me? Is this total stranger really asking to put his mouth on *my* water bottle?

    The thought of his viscous saliva slobbering over the mouth of my bottle makes my stomach churn...

    Does he know that he's basically asking for an indirect kiss?
    """
    be "Well? It's just a drink...are you going to be a good girl or what?"
    m "Take it easy, Menmi. Don't want to barf at the gym on your first day."

label choice_6:
    menu:
        m "What should I do?"

        "Comply and get it over with":
            c "Do you really think he'll leave you alone if you give him what he wants? You'd just be encouraging him."
            m "The thought of allowing him to get away with harassment...it just makes me feel small and ashamed."
            c "Did you do something to deserve this?"
        "Politely, but firmly decline":
            c "Put him in his place with a polite, but firm “No.” There's no need to engage with this guy anymore than you already have."
            m "She's right, but why does doing that feel so scary? The way he's staring me down...I don't know, I feel like something bad's going to happen if I make him mad..."
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
label joule_introduction:
    m "It's like there's no right answer. This feeling of powerlessness is so frustrating..."
    j "Leave her alone."
    m "Huh? Who said that?"
    show joule neutral with dissolve
    j "Hey, Beast Mode. Can I help you with a Cool Down routine?"
    be "What did you say, shrimp-fried rice?"
    m """
    The guy standing in front of me is wearing a sleeveless shirt with the gym's logo on it. The ID card around his neck indicates that he works here.

    He's smaller than the Behemoth, but there's no fear at all in his defiant posture.
    """
    j "She's clearly uncomfortable. Is that any way for a real man to act?"
    m """
    The Behemoth growls, veins rising in his biceps like a mountain range.

    He glances at the guy's ID card, though, and releases his grip.
    """
    be "Tch. Talk about crap service. What kind of shitty gym runs out of water on paying customers?"
    j "I've already alerted the appropriate personnel. This station should be refilled within the next few minutes."
    j "Thanks for your patience, sir."
    m """
    His tone is professionally polite, but his smirk says otherwise...

    The Behemoth audibly grumbles, but backs off.

    The tension in my shoulders releases.
    """
    j "You OK? My name's Joule. I'm a trainer here."
    $ joule_name = "Joule"
    m "“Yeah, thanks for that.”"
    j "No worries, but could I give you a piece of advice?"
    m "I tense up, bracing myself for the reprimand."
    m "“Sure, what's up?”, hoping I sound as cool as he does."
    j "You should be more careful. He put you in a really dangerous position. Judging by your build, there's no way you could have taken him if things got physical."
    m """
    He's not *wrong*, but the way he's scolding me rubs me the wrong way.

    Sure, this guy just "saved" me, but he can't be blaming *me* for this, right?
    """
label choice_7:
    menu:
        m "How should I respond?"

        "Speak out":
            $ renpy.notify("+10 Self-Awareness")
            $ self_awareness += 10
            c "Stand up for yourself! That other dude was dangerous, but this guy seems like he'd be willing to hear you out."
            m """
            A sudden wave of shame and fury washes over me as I remember the powerlessness of the moment.

            I won't be able to live it down if I don't correct him now.

            "It wasn't my fault! I was just minding my own business when he approached me."

            "It shouldn't be on the victim to change their behavior here! There was nothing tangible I could say or do that would level out the power imbalance."

            I can see him trying to lift this concept...mentally.
            """
            j "...You're right. I'm sorry that I implied that it was on you to change. That's not fair to you."
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
    j "You were scared, weren't you? I'd be, too"
    m "The look in his eyes...it's kind of sad."
    m "Something tells me this guy is just trying to help."
    j "I'm not trying to shill my services or anything, honestly, but if you ever want to do something about your strength, just give me a ring."
    m """
    He pulls out a business card and hands it to me. There's a black and white photo of him on it, the hard lighting capturing every line and contour of his chiseled build.

    He's kind of hot. Once you get over the patronizing remarks.

    Although there *is* something romantic about a rescue in a high octane situation that makes my inner feminist want to crunch up and die.

    """

    c "Your inner feminist wants you to get swole and squat punch creeps."
    m "Thanks. I'll think about it."

    j "Girls should know how to protect themselves...especially the pretty ones"
    hide joule neutral with dissolve
    scene gym-inside with dissolve:
        blur 24
    m """
    My heart's beating so fast, and I haven't done a single rep.

    D-did he just say what I think he said?

    Thinking about his words, I pushed myself just a little harder that morning.

    """
    jump week_1_day
