label naji_date_1:
    play sound "/audio/pencil-write.mp3"
    hide screen open_planner
    hide screen open_insights
    scene city-morning with fade:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}Week [week]{/size}{/font}{/color}{color=#000000}{color=#000000}{font=JustAnotherHand-Regular.ttf}{size=200}\n Weekend!{/size}{/font}{/color}" at truecenter with wiperight
    pause

    play music "<from 9>/audio/happily-ever-after.mp3" fadein 0.5
    scene menmi-apartment-morning with dissolve
    show screen open_planner
    show screen open_insights


    m """
    After a long week of work, a night out sounds like just the thing to reinvigorate me.

    “Time to get hyped to hit the town!” """

    stop music
    play sound "/audio/impact-slam.mp3"
    scene menmi-apartment-morning with vpunch:
        matrixcolor InvertMatrix(value=1.0)

    i "Keep your on the prize, girl. Don't forget we're here to find love."

    if self_awareness>=40:
        play sound "/audio/awareness-ding.mp3"
        show text "{image=ol_text}" with easeinbottom
        pause
        hide text with dissolve
        m "That's true, but I've also got time on my side. No need to make myself sick stressing over it."
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

    elif self_awareness<40:
        m "I know. I won't rest until I'm wanted."

    play music "<from 13>/audio/happily-ever-after.mp3" fadein 0.5
    scene city-night with dissolve
    m "Usually, I'll bring Allie or some coworkers to hang out, but tonight, it's just me and Naji."

    m """
    I haven’t seen him much since high school ended, besides at the lounge.

    It’ll be nice to have a proper catch-up while he's off the clock.

    Since it's the weekend, I get the opportunity to wear something nice. I hope this floral minidress works for the occasion. """

label choice_12:
    menu:
        m "How do I look?"

        "Great!":
            show screen selfawareup 
            window hide
            play sound "/audio/awareness-ding.mp3"
            pause
            hide screen selfawareup 
            $ self_awareness += 5
            c "Cute and chic — perfect for a night out. This is *precisely* why you bought this dress!"
            m """That's right. I have to remind myself of how confident and pretty it made me feel when I first tried it on.

            ...And how it was *totally* worth the full retail price hehe."""
        "On second thought...":
            c "Isn't this a little too much? You look like a try-hard."
            m "Maybe I should've gone with a safer option. I hope I don't stick out *too* much."
        "It doesn't matter.":
            c "Whatever. Who's going to stop you? The Fashion Police? Wait, is that why there are so many uniformed individuals around? Why do they look so dowdy?"
            m "It's true that I can be my own harshest critic, but I want to at least *feel* confident."

label after_choice_12:
    play sound "/audio/subway-door.mp3"
    m "Oops. Got lost in the sauce. Better board the train before I get Menmashed against the door."
    stop music fadeout 2.0

    scene lounge-inside with fade
    play music "/audio/najis-theme.mp3"
    show naji-bar-smile with dissolve

    n "“Welcome to the William Collins!”"
    hide naji-bar-smile
    show naji-bar-blush at hop

    n "“Oh! Hey Menmi.”"
    m """(I try not to be unmoored by the deer-in-headlights look he gives me.)

    (The bare air conditioning of the lounge feels especially chilly today against my exposed shoulders.)"""

    m "(Why is he staring? Is it...a *good* stare?)"

    hide naji-bar-blush
    show naji-bar-lookaway

    if self_awareness>=30:
        m "Maybe..."
    if self_awareness<30:
        m "I...am thinking about something else now."

    m "“Hope I'm not catching you at a bad time.”"
    n "“Nope! Just wrapping up my shift.”"

    hide naji-bar-lookaway
    show naji-bar-neutral

    n "“Naya is covering for me. I told her we were hanging out.”"

    hide naji-bar-neutral
    show naji-bar-smile at hop

    m """
    He waves to another waistcoated employee at the other end of the bar.

    I swear she winks at him.
    """

    if self_awareness<=40:
        stop music
        play sound "/audio/impact-slam.mp3"
        scene lounge-inside with vpunch:
            matrixcolor InvertMatrix(value=1.0)
        i "They're definitely dating."
        play music "<from 7>/audio/najis-theme.mp3"
        scene lounge-inside with hpunch
        show naji-bar-smile with dissolve


    m "Naji clears his throat and becomes very interested in wiping down the counter."

    hide naji-bar-smile
    show naji-bar-lookaway

    m "I frantically fish for something to say."


    play sound "/audio/impact-slam.mp3"
    scene lounge-inside with vpunch:
        matrixcolor InvertMatrix(value=1.0)
    show naji-bar-lookaway at truecenter:
        matrixcolor InvertMatrix(value=1.0)
    i "Have I always been this awkward around Naji?"

    scene lounge-inside
    show naji-bar-lookaway with dissolve

    hide naji-bar-lookaway with dissolve
    show naji-bar-neutral

    n "“You look nice today.”"

    hide naji-bar-neutral
    show naji-bar-smile

    n "“Pink suits you.”"
    m """
    “Thanks.”

    (I hope he means my dress and not my cheeks.) """

    hide naji-bar-smile
    show naji-bar-neutral

    m "(Time to change the topic.)"

    m "“We haven't really talked about where you've been since we lost touch.”"


    n "“It's not very interesting, but if you're asking...”"

    m "“Please, Naji?”"

    hide naji-bar-lookaway
    show naji-bar-smile

    n "“OK OK...but first, let me make you a drink.”"

    hide naji-bar-smile
    show naji-bar-neutral

    play sound "/audio/ice-pour.mp3"

    m """
    Before I can make my order, Naji has a bottle of rum in hand and is pouring it into a tumbler.

    I watch transfixed as he adds blended frozen strawberries and a bevy of other ingredients, shaking the concoction with practiced precision.

    His arms move through the air in artfully controlled arcs.
    """
    play sound "/audio/bottle-clink.mp3"

    m "Finally, he pours the drink into a wide glass and garnishes it with a wedge of lime before skillfully sliding across the counter to me."


    show naji-bar-smile
    show strawberry-daiquiri at truecenter with easeinbottom

    n "“You like strawberry daiquiris, right?”"

    hide naji-bar-smile


    n "“I remember trying to make you one with those janky freeze-dried strawberries from the Malwart when we were underage-drinking in school.”"


    m "“You remember that,” I say, taking a sip."

    hide strawberry-daiquiri with dissolve

    m """
    (I'm acutely aware that I can't say the same for myself.)

    (What's Naji's favorite drink? When's the last time I've even *seen* him drink?)

    (Oh gosh, am I a bad friend?)

    """

    play sound "/audio/impact-slam.mp3"
    stop music
    scene lounge-inside with vpunch:
        matrixcolor InvertMatrix(value=1.0)
    i "{i}Scaaaatterbrains!{/i}"

    if self_awareness>=50:
        scene lounge-inside
        play sound "/audio/awareness-ding.mp3"
        show text "{image=ol_text}" with easeinbottom
        pause
        hide text with dissolve
        m "(I'll take this as an opportunity to learn more about him.)"
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

    elif self_awareness<50:
        m "(Maybe I just function with a low-grade concussion at all times.)"

    scene lounge-inside with hpunch
    show naji-bar-neutral with dissolve
    play music "/audio/najis-theme.mp3"

    m "I take a sip of the drink."
    show strawberry-daiquiri at truecenter with dissolve
    play sound "/audio/sparkle.mp3" volume 0.7

    m """
    !!!

    “Oh my god, Naji — it's delicious!”

    (It may be the best daiquiri I've ever tasted — the chilled, sweet flavor of the blended strawberries melts into the heady warmth of rum, sliding easily down my throat.)

    """
    hide strawberry-daiquiri with dissolve
    hide naji-bar-neutral
    show naji-bar-smile

    n "“Glad you like.”"

    hide naji-bar-smile
    show naji-bar-neutral

    n """
    “Again, my story isn't all that interesting.”

    “I did OK in college, but left undergrad not really knowing what to do next.”
    """

    n """
    “It's funny, isn't it?”

    “When we were kids, we'd talk about how free we'd be when we grew up, but when that time finally came...”

    “the choices just weren't there.”

    “Or maybe they are, but I haven't figured them out.”"""

    hide naji-bar-neutral
    show naji-bar-lookaway
    n "“Anyway, I moved to Applecore City with a couple of friends.”"

    hide naji-bar-lookaway
    show naji-bar-neutral

    n "“Not because I had a job lined up like you or anything. I just had to.”"

    m "(That's a surprise...I always thought things came so easily to Naji.)"

    hide naji-bar-neutral
    show naji-bar-lookaway
    stop music fadeout 3.0

    n "“I couldn't stay.”"

    m "(Something about it feels off. I wait for him to elaborate, but Naji just looks away and moves on.)"

    hide naji-bar-lookaway
    show naji-bar-neutral
    play music "<from 7>/audio/secret.mp3"

    n """
    “Anyway, I uh, met someone and she hooked me up with a job. She was a business owner and needed to staff up her bar.”

    “At first, I was more than happy just to help her out, but she ended up teaching me a lot about mixology.”

    """

    m "(The back of my throat tastes acrid.)"

    hide naji-bar-neutral
    show naji-bar-lookaway

    m "(He didn't say it outright, but I can tell from the way he skirts around the topic that their relationship wasn't *just* platonic.)"

    m "(I get the feeling that I don't like this woman.)"

    if self_awareness <=60:
        play sound "/audio/impact-slam.mp3"
        scene lounge-inside with vpunch:
            matrixcolor InvertMatrix(value=1.0)

        m """(The only way to get away from this feeling is to get as many sordid details about it as possible.)

        (Maybe if I could understand it, it wouldn't bother me so much.)"""

        i "That's right, lean into those masochistic tendencies, you little freak. "

        m "(The surge of acrid heat in my chest feels almost...invigorating.)"

        scene lounge-inside with vpunch

    hide naji-bar-lookaway
    show naji-bar-neutral

    n """
    “That's how I ended up at the William Collins. I'd been working here for six months before you reached out.”

    “And...here we are!”
    """

    m "(He seems reluctant to elaborate about the woman he mentioned.)"

    m "(But I'm *so* curious!)"

    m "(Almost morbidly so. Like I want to know everything about his love life so that I know how *I* stack up.)"

    if self_awareness>=70:
            m "(But that doesn't make sense...my worth isn't related to anyone else's.)"

    m "Naji hardly ever talks about his relationships... maybe he's feeling vulnerable?"
    play sound "/audio/impact-slam.mp3"
    scene lounge-inside with vpunch:
        matrixcolor InvertMatrix(value=1.0)
    i "Or maybe you're trying too hard to rationalize your curiosity."
    if self_awareness>=30:
        play sound "/audio/awareness-ding.mp3"
        show text "{image=ol_text}" with easeinbottom
        pause
        hide text with dissolve
        m """
        (*Everything* is a rationalization.)

        (It all depends on how you look at it, and I choose to interpret this as Naji opening up to me.)
        """
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

    elif self_awareness<30:
        m "(I know I'm just being selfish....)"

    scene lounge-inside with vpunch
    show naji-bar-lookaway

label choice_13:
    menu:
        "How should I respond to Naji?"

        "Continue where he left off":
            c "He's trying to change the mood. Don't ruin the vibe!"
            m """
            “And...here we are! Living the dream!”

            I raise my glass, and we toast. It was nice to be reconnected with Naji again, after all this time.
            """
            hide naji-bar-lookaway
            show naji-bar-smile
            n "“Wanna see something cool?”"
        "Change the topic":
            c "Are you uncomfy? I'm uncomfy. These vibes are *not* it."
            m """
            (This conversation...I don't want to continue with it. It feels like I'm wading into dangerous territory.)

            “Uh...so, you know any cool bartending tricks?”

            To my relief, Naji's expression brightens a bit.
            """
            show naji-bar-smile at hop

            n "“Yeah! Watch this.”"
        "Keep listening":
            c "You came here to find out more about Naji. Why not just listen and let him share as much as he wants us to know?"

            m "When we were kids, Naji and I held nothing back from each other."

            m """
            (From drama at school, to getting in trouble with parents, to our anxieties about the future,

            we trusted each other with our feelings, assured in the fact that we wouldn't say or do anything to hurt each other without good reason.)

            """

            m """
            (What changed? I want us to trust each other.)

            (This is about him, not me. The best response I can give him is my attention without judgment.)

            ...
            """
            n """
            ...

            “Let's move on from the past. You wanna see a trick?”
            """
            show screen selfawareup 
            window hide
            play sound "/audio/awareness-ding.mp3"
            pause
            hide screen selfawareup 
            $ self_awareness += 5

            m """
            (...OK. A little anticlimactic, but I shouldn't be surprised.)

            (Seems like he's done with this topic. I can respect that.)

            (I *have* to respect that.)

            "Sure."
            """
        "Ask Naji about the woman":
            c "Naji sounds hurt. Maybe it would help him to talk about it."

            m """
            (That's right. I'm asking for *his* benefit, not mine.)

            “You mentioned a woman. What exactly was your relationship with her?”
            """
            hide naji-bar-neutral
            show naji-bar-frown
            m "There's a sad smile on his face and a slump in his shoulders."
            hide naji-bar-frown
            show naji-bar-smile
            n "“Ha...I had a feeling you'd ask.”"

            if len(dialogue_matches) > 0:
                show screen insight(dialogue_matches)
                m "(What's *that* supposed to mean?)"
            hide naji-bar-smile
            show naji-bar-lookaway
            n "“Sigh. I wouldn't call it ‘dating', but we had a...thing. She was a little older than me and wasn't looking for anything beyond casual.”"
            hide naji-bar-lookaway
            show naji-bar-frown
            n "“Hope that satisfies your curiosity.”"

            play sound "/audio/impact-slam.mp3"
            scene lounge-inside with vpunch:
                matrixcolor InvertMatrix(value=1.0)
            show naji-bar-frown at truecenter:
                matrixcolor InvertMatrix(value=1.0)

            m "(Even though I expected it, a part of me recoils hearing about Naji doing things like that.)"

            if self_awareness >=50:
                m "(Am I...jealous?)"

            scene lounge-inside
            show naji-bar-lookaway
            m "“And you? What did you want?”"
            hide naji-bar-lookaway
            show naji-bar-frown at squirm
            n "“...I'm not sure, honestly. I was just going with the flow.”"
            hide naji-bar-frown
            show naji-bar-neutral at hop
            n "“Anyway, that's what happened. Hey, wanna see something cool?”"
            m """
            (Surprise, surprise. He changed the topic.)

            (At least he seems more excited now. He sounds like he's about to show me a new Pokébowlmon card or something.)

            "Yeah, OK."
            """
        "Ask him why he had to leave home":
            c """
            Think. You're hyperfocusing on the mystery woman when there's a bigger issue here.

            Naji's love life might hold the spicier tea, but what did he *really* sound upset about?
            """
            m "(Naji's voice tightened when he was talking about leaving home.)"

            scene lounge-inside
            show naji-bar-lookaway
            m """
            (I know more about Naji's childhood than the average person. Could it be that he *wants* me to ask?)

            (It could be that *he* isn't aware of either)

            “What did you mean when you said you ‘couldn't stay'? Did you mean about home?”
            """
            show screen selfawareup 
            window hide
            play sound "/audio/awareness-ding.mp3"
            pause
            hide screen selfawareup 
            $ self_awareness += 5

            hide naji-bar-lookaway
            show naji-bar-neutral

            m "Naji clenches, unclenches a fist."
            n "“Well, you know how my mom's always been sort of...unwell?”"

            m """
            (I do remember.)

            (Naji's mother struggled to raise him on her own and was always latched onto one guy or another like a barnacle.)

            (She said she'd was looking for a father figure for Naji, but I think she was lonely and wanted to feel special to someone.)

            (Just not her child.)
            """

            if self_awareness <=50:
                m "I was lucky, in comparison."
                m "(That's what my parents used to say, anyway)"


            hide naji-bar-lookaway
            show naji-bar-frown
            n """
            “As I got older, Mom became more reliant on me for basic things. She couldn't even run out to buy smokes without without spiraling.”

            “It was hard, seeing her like that...and if I'm being honest, frustrating too.”

            “She's never been the most self-assured.”
            """

            hide naji-bar-frown
            show naji-bar-neutral

            n """“After a while, I realized that she wasn't ever going to get better if I stuck around, so I had to leave.”

            “For both our sakes.”"""

            m "“I'm sorry, Naj...that must have been a really difficult decision. Thank you for trusting me with that.”"
            $ renpy.notify("Naji feels closer to you!")
            $ naji_relationship += 10
            n "“Yeah...thanks for asking. I feel lighter just by telling you.”"
            n "Hey, do you want to see a trick?"

            hide naji-bar-neutral

label after_choice_13:
    stop music fadeout 1.0
    play music "/audio/najis-theme.mp3"
    show naji-bar-smile

    m """
    Shaker in one hand, Naji passes a bottle over the nape of his neck around his shoulders.

    The shaker rolls down his arm in an elegant swoop. With his extended hand, He catches the shaker-bottle with the other and gracefully pours the fizzy contents into the glass.

    Naji completes his trick, figure poised in a confident flourish, though his red cheeks and crooked grin belie his embarrassment.
    """

    hide naji-bar-smile
    show naji-bar-neutral

    m """My face hurts from smiling as I clap enthusiastically.

    It was an awesome performance, but I can't help teasing Naji."""

    m "“That was pretty impressive. You've come a long way from those disgusting movie theater soft drink experiments.”"

    hide naji-bar-neutral
    show naji-bar-laugh at laughter

    m "A smirk inches its way across his face."
    n "“The world just isn't ready for Maximum Energy Wildberry Cool Blue Diet Mountain Brew.”"

    hide naji-bar-laugh
    show naji-bar-neutral

    m "“It tasted like carsick”"

    hide naji-bar-laugh
    show naji-bar-frown

    n "“To *you*”"
    m """ “Didn't you put popcorn butter in it too?”

    Naji shrugs."""

    hide naji-bar-frown
    hide naji-bar-laugh
    hide naji-bar-neutral
    show naji-bar-smile at hop

    n "“It was *there*. What else were we going to do with it?”"

    m """
    ...

    “I guess that *is* how we became friends, too.” """

    hide naji-bar-smile
    show naji-bar-neutral

    m "(The look in Naji's eyes is wistful as he carefully wipes clean the bar area around me.)"

    m "(He's so considerate.)"

    m "(I can't help but be amazed that I've known this person since he was a soda-stained kid with curly hair and clammy hands.)"
    n "“I don't do it for everyone, you know. Little tricks every now and then are cool, but any more than that is showing off, you know?”"
    m """“Right, and you're no show-off.”

    I laugh, rolling my eyes. Instead of matching my quip, though, Naji surprises me by replying in a soft voice."""

    hide naji-bar-neutral
    show naji-bar-lookaway

    n "“I'm not. For most people.”"

    hide naji-bar-lookaway with dissolve

    $ renpy.notify("Naji feels closer to you!")
    $ naji_relationship += 10

    m "(Why does that make me feel kind of happy?)"

    $ n1=True

label after_naji_date:
    scene menmi-apartment-night with fade
    m "Hanging out with Naji always feels new and familiar at the same time."

    if week == 4:
        jump reading_time
    elif week<4:
        m "It's a shame that the weekend's over, but there's always next weekend! What should I do?"
        hide screen open_planner
        hide screen open_insights
        #Choose next weekend activity in planner
        scene planner-week-unfilled with dissolve
        m "I'll just drop the activity sticker I want in the 'Weekend' box!"
        call screen planner_weekend(_with_none=False) with dissolve
        jump reading_time
