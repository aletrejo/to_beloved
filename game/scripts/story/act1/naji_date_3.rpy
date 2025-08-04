label naji_date_3:
    $ lover = "Naji"
    play sound "/audio/pencil-write.mp3"
    hide screen open_planner
    hide screen open_insights
    scene city-morning with fade:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}Week [week]{/size}{/font}{/color}{color=#000000}{color=#000000}{font=JustAnotherHand-Regular.ttf}{size=200}\n Weekend!{/size}{/font}{/color}" at truecenter with wiperight
    pause

    stop music
    play sound "/audio/impact-slam.mp3"
    scene menmi-apartment-morning with vpunch:
        matrixcolor InvertMatrix(value=1.0)
    show screen open_planner
    show screen open_insights
    i "You're up early for a weekend."

    scene menmi-apartment-morning
    play sound "/audio/subway-door.mp3"
    m "Yeah, I have a train to catch..."

    scene bakery with pushleft
    play sound "/audio/outdoor-crowd.mp3" volume 0.7
    m "...A hype train, that is!"

    play music "<from 9>audio/cloud.wav"

    m """(A celebrity chef downtown just dropped the latest pastry craze – a combination of a waffle and a macaroon.)

    (They call it...The Wackaroon.)

    (And I consider it my civic duty to stay on the cutting board's edge of pastry innovation.)

    (So here I am, outside Jujubakery, standing on a line that wraps almost entirely around the block.)
    """

    scene bakery with dissolve:
        matrixcolor BrightnessMatrix(value=0.7)
    scene bakery with dissolve:
        matrixcolor BrightnessMatrix(value=0.5)
    scene bakery with vpunch

    m """
    (Feeling both antsy and sleepy at the same time, I fight to stay on my feet as the front of the line comes into view.)

    A worker comes out and hangs a “SOLD OUT” sign over the Wackaroons.
    """

    play sound "/audio/impact-slam.mp3"
    scene bakery with vpunch:
        matrixcolor BrightnessMatrix (value=1.0)
    play sound "/audio/impact-slam.mp3"
    scene bakery with vpunch

    m "NOOOOOOOOO!"

    play sound "/audio/impact-slam.mp3"
    scene bakery with vpunch:
        matrixcolor InvertMatrix(value=1.0)
    i "If you were capable, you'd have gotten here earlier."

    if self_awareness>=70:
        play sound "/audio/awareness-ding.mp3"
        show text "{image=ol_text}" with easeinbottom
        pause
        hide text with dissolve
        m "(I got here as early as I could. How could I predict how much stock they'd have?)"
        $ chosen_sticker = renpy.random.choice(available_stickers)
        image sticker_won = "stickers/sticker-[chosen_sticker].png"
        show sticker_won at rotation:
            xpos 0.5
            ypos 0.5
        show text "{image=stickertext}" with dissolve:
            xpos 0.5
            ypos 0.5
        pause
        hide sticker_won
        hide text
        show screen place_sticker(chosen_sticker)
        $ available_stickers.remove(chosen_sticker)
        pause
        hide screen place_sticker
        $ passed_checks +=1


    elif self_awareness<70:
        m "(Um, I have a medical condition? {w}I wonder if there's a treatment for being chronically {b}STUPID.{/b})"

    scene bakery with vpunch
    m "As I woefully peruse the unWackmarkable leftovers, a familiar golden head comes into view."
    show naji-neutral with dissolve
    play music "/audio/najis-theme.mp3"
    n "“Looks like you just Menmissed out.”"

    play sound "/audio/impact-slam.mp3"
    scene bakery with vpunch
    show naji-smile with vpunch

    m """
    (He's sending my overcaffeinated heart into overdrive.)

    “Don't sneak up on me like that!”

    "What are you doing here? We weren't supposed to meet until later.”
    """
    hide naji-smile
    show naji-neutral
    n "“I know. I was just picking up a treat.”"

    show wackaroon at truecenter with easeinbottom

    m"""
    (He holds out a white paper bag and-OH MY SQUASH.)

    “Is that-?”
    """

    hide naji-neutral
    show naji-laugh at laughter

    m "Naji cackles riotously, lording the bag over my head."

    n "“Sorry, Men. You know what they say -- 'the early bird whacks the worm.'”"
    hide naji-laugh
    hide wackaroon
    show naji-surprised at pushback

    m "“Nobody says that, you macaroon.”"
    hide naji-surprised
    show naji-laugh
    n "“Is that any way to talk to someone who’s wacked his worm?”"
    m "“That sound better in your head?”"
    hide naji-laugh
    show naji-neutral
    n "“Yea.”"

    m "(He *is* right about being punctual, though. As hard as it is to admit, he *did* earn it by being here early.)"

    if self_awareness>=80:
        m """
        (But this is Naji we're talking about.)

        “Please, Naji? Just a tiny bite? A sliver!”
        """
        hide naji-neutral
        show naji-smile
        m "A quirk passes the edge of his lips."
        $ naji_relationship +=10
        show screen relationship_up onlayer overlay
        play sound "/audio/awareness-ding.mp3"
        pause
        hide screen relationship_up
        n "“Ha, ya caught me.”"

    show naji-laugh
    n "“You knew I was planning on sharing them with you all along, right?”"

    m "“Read and visualized like a novel. Shall we eat these in the park?”"

    scene park-day with pixellate

    m """
    “Hello my Menminions! Welcome to Menmi's Wackaroon Reaction Video! Featuring...Naji!”

    I turn my phone's camera to face Naji.
    """

    show naji-frown with dissolve

    m "He looks kind of annoyed, but doesn't say anything."

    m """
    "I'm filming for my Instayam story!"

    """

    show wackaroon at truecenter with easeinbottom
    hide naji-frown with dissolve

    m"""

    I hold the macaroon to the camera, getting a good shot of the brightly colored waffle texture.

    As I take a bite out of the disc, I hand over the other half for Naji.

    """

    if self_awareness >=60:
        m "Why's he just staring at it like that?"
        c "Why'd the Behemoth want to drink from your bottle?"
        m "Oh...{p}I chew faster on the wackaroon."

    define flash = Fade(0.1, 0.0, 0.5, color="#fff")
    play sound "/audio/sparkle.mp3" volume 0.7
    scene park-day with flash
    show wackaroon at truecenter with dissolve

    m """
    (It's delicious!)

    (The outer shell is a perfect balance between chewy and soft. The smooth, sweet filling creates a magical mouthfeel that contrasts with the bumpy waffle crust.)
    """

    show naji-neutral with dissolve
    hide wackaroon
    m """
    (I take a peek next to me, trying to assess Naji's reaction.)

    (He's staring straight ahead, throat bobbing slowly as he swallows.)
    """

    hide naji-neutral
    show naji-lookaway at shake

    n "“Good! {w}So yummy. {w}Wow.”"

    m "(I can tell he doesn't like it. He's putting up a front for me out of consideration for my feelings.)"

label choice_15:
    menu:
        m "How should I respond?"

        "Ask him to be honest":
            c "His consideration is sweet, but unnecessary. He doesn't have to pretend just to please you."
            m """
            “C'mon, how long have we known each other, Naj. You can be honest if you don't like them.”

            “We don't have to agree on everything. I think it's fun that we enjoy different flavors!”

            """
            hide naji-lookaway
            show naji-smile at laughter
            n """
            “...You're right.”

            “In that case, they're gross and taste like crayons”

            “But...{w}that doesn't mean I'm not having fun.”

            """
            show screen selfawareup 
            window hide
            play sound "/audio/awareness-ding.mp3"
            pause
            hide screen selfawareup 
            $ self_awareness += 5
            show screen relationship_up onlayer overlay
            play sound "/audio/awareness-ding.mp3"
            pause
            hide screen relationship_up$ renpy.notify("Naji feels closer to you!")
            $ naji_relationship += 10
        "Play along":
            c "He's being polite for your sake. He'd be embarrassed if you grilled him about his real feelings."
            hide naji-lookaway
            show naji-surprised at hop
            m """
            "Right?" I put on my most convincing PR smile.

            (Naji's reaction definitely dampened the mood, but I have to keep the vibes up.)"""

            hide naji-surprised
            show naji-neutral

            m "“Thanks again for wacking the worm, Naji.”"
            n "“Don't mention it.”"
            hide naji-surprised
            show naji-smile
            n "I wanted to do it."

        "FIGHT him":
            c "If he doesn't like them, that means you're *wrong* for liking them...{w}and {i}that{/i} can't be true!"
            m """
            "You mean that right? You're not just saying that?"

            (I hope the edge in my voice is cutting into him as deeply as it does to me.)
            """
            n "“Woah, woah, Menmi. Fists down. Yes, they're good! I'm having a good time.”"
            m """
            "OK good."

            I sit back down.
            """

label after_choice_15:
    show naji-smile
    n "“We used to eat like this together when we were kids, didn’t we?”"
    n "“You’d always give me your cupcakes back then, remember?”"

    m """
    “I ate them *every* day.”

    “You were doing me a favor by taking them. Trust.”
    """

    m "(What I don't say is how I'd noticed Naji's mom never *quite* packed him enough to eat.)"

    hide naji-smile
    show naji-neutral

    n "“Yeah, that’s what you said back then too.”"

    m "(As silence settles over us, I watch a cool breeze shift across the dappled light in Naji’s locks.)"

    show naji-lookaway

    n "“Do you still feel that way?”"
    m """ (It takes me a second to understand that he’s talking about the cupcakes.)

    “I don’t know. It’s been a while since I’ve had them.” """

    hide naji-lookaway
    show naji-laugh

    m "Naji laughs."

    hide naji-laugh
    show naji-neutral

    n "“Absence makes the heart grow fonder, they say.”"
    m "“They do say that, actually. {w}Unlike the worm-whacking thing.”"

    m """

    (The morning air around shimmers, cool and bright.)

    (Shadows cast by faraway branches pepper Naji's face and shoulders like freckles on a pear.)

    """

    hide naji-neutral
    show naji-smile

    n "“We should revisit the Little Crebbie’s one day.”"
    m "“Mmmm...I think Joule would kill me if I picked up a sugar habit.”"

    hide naji-smile
    show naji-neutral

    m "(I’d expected laughter, but Naji remains quiet, eyes toward the sky.)"

    stop music fadeout 5.0

    m "(Did I misread the vibe? Quick, say something cool and unawkward.)"


    m "What should I say?"

    pause 5.0

    m "I'm drawing a blank."

    play music "<from 107>/audio/reaching-the-sky.mp3" volume 0.5
    show naji-park-breeze with dissolve:
        zoom 1.5
        ease 5.0 zoom 1.0

    m "It’s hard to think when Naji’s right there, downy hair blowing in the breeze, gentle morning sun spreading over his unguarded face."

    pause

    scene park-day with dissolve

    al """
    “Hey there, early birds!”

    “Up wacking the worm?”

    """

    show allie-neutral with dissolve

    m """
    I’m relieved to see Allie walking up to us on the path, picnic blanket and sunglasses in hand.

    I stand up and wave to them, brushing pastel crumbs off my skirt. Naji turns to them and waves.

    The private moment between me and Naji has passed. I smile, sinking back into the comfort of our familiar, friendly dynamic.

    Still, a nagging hole of a feeling inside my chest that makes me feel like I’m missing something.

    """

    $ naji_relationship +=10
    show screen relationship_up onlayer overlay
    play sound "/audio/awareness-ding.mp3"
    pause
    hide screen relationship_up

    $ n3=True
    $ week += 1
    jump week_2_4
