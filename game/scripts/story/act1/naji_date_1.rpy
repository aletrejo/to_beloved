label naji_date_1:
    play sound "/audio/pencil-write.mp3"
    scene city-morning with fade:
        blur 10
    show text "{font=PatuaOne-Regular.ttf}{size=230}{color=#EB266A}Week [week]{/size}{/font}{/color}{color=#000000}{color=#000000}{font=JustAnotherHand-Regular.ttf}{size=200}\n Weekend!{/size}{/font}{/color}" at truecenter with wiperight
    pause

    play music "<from 9>/audio/happily-ever-after.mp3" fadein 0.5
    scene menmi-apartment-morning with dissolve

    #Relevant Insights: Meeting new people, experiencing new things, chasing down a whirlwind romance...; I'm going to have faith and enjoy the ride
    m """
    After a long week of work, a night out sounds like just the thing to reinvigorate me.

    “Time to get hyped to hit the town!” """

    stop music
    play sound "/audio/impact-slam.mp3"
    scene menmi-apartment-morning with vpunch:
        matrixcolor InvertMatrix(value=1.0)

    #Relevant Insights: It's nice to know that I'm capable of achieving happiness for myself; I believe in myself
    i "Keep your on the prize, girl. Don't forget we're here to find love."

    if self_awareness <=40:
        #Relevant Insights: Everyone has to believe in something, and I choose to believe in love!
        m "I know. I won't rest until I'm wanted."

    play music "<from 13>/audio/happily-ever-after.mp3" fadein 0.5

    scene city-night with dissolve
    m "Usually, I’ll bring Allie or some coworkers to hang out, but tonight, it’s just me and Naji."

    #Relevant Insights: We were pretty close through high school, but lost touch after graduation.;We were pretty close through high school, but lost touch after graduation; He's changed.; It makes me feel insecure that I don't know everything about him; I hope he can be open with me someday...; Naji's grown with time. I'm curious about what else about him has changed...
    m """
    I haven’t seen him much since high school ended. It’ll be nice to catch up.

    Since it’s the weekend, I get the opportunity to wear something nice. I hope this floral minidress works for the occasion. """

label choice_12:
    menu:
        m "How do I look?"

        "Great!":
            #Relevant Insights:  I believe in myself; I'm going to have faith and enjoy the ride; It's nice to know that I'm capable of achieving happiness for myself.; I choose to believe in myself!
            $ renpy.notify("+5 Self-Awareness")
            $ self_awareness += 5
            c "Cute and chic — perfect for a night out. This is *precisely* why you bought this dress!"
            m """That's right. I have to remind myself of how confident and pretty it made me feel when I first tried it on.

            ...And how it was *totally* worth the full retail price hehe."""
        "On second thought...":
            #Relevant Insights: Sometimes I feel insecure.; I have regrets.; I'm uncertain...; I'm doubtful...;What if things don't go as planned?
            c "Isn't this a little too much? You look like a try-hard."
            m "Maybe I should've gone with a safer option. I hope I don't stick out *too* much."
        "It doesn't matter.":
            #Relevant Insights: I can't go back now, though; I need to move on.; There are times when I admit I can be hard on myself.
            c "Whatever. Who's going to stop you? The Fashion Police? Wait, is that why there are so many uniformed individuals around? Why do they look so dowdy?"
            m "It's true that I can be my own harshest critic, but I want to at least *feel* confident."

label after_choice_12:
    play sound "/audio/subway-door.mp3"
    m "Oops. Got lost in the sauce. Better board the train before I get Menmashed against the door."
    stop music fadeout 2.0

    scene lounge-inside
    play music "/audio/najis-theme.mp3"
    show naji-bar-smile with dissolve

    n "“Welcome to the William Collins!"

    hide naji-bar-smile
    show naji-bar-surprise

    n "Oh! Hey Menmi."

    hide naji-bar-surprise
    show naji-bar-blush
    m """I try not to be unmoored by the deer-in-headlights look he gives me.

    The bare air conditioning of the lounge feels especially chilly today against my exposed shoulders."""

    #If any of these Insights were selected: It's romantic to fall for the best friend who's been with you all along. Who knows me better than him?; There were times I wondered if we could be more than friends...;By the time we were in high school, I could see how he would be considered attractive...physically
    #Why is he staring? Is it...a *good* stare?

    if self_awareness>=30:
        m "Maybe..."
    if self_awareness<30:
        m "I...am thinking about something else now."
        m "“Hope I’m not catching you at a bad time.”"

    hide naji-bar-blush
    show naji-bar-lookaway

    n """
    “Nope! Just wrapping up my shift.”
    "Ada is covering for me. I told her we were hanging out.
    """

    m """
    He waves to another waistcoated employee at the other end of the bar.

    I swear she winks at him.
    """

    if self_awareness<=40:
        i "They're definitely dating."
        stop music
        play sound "/audio/impact-slam.mp3"
        scene lounge-inside with vpunch:
            matrixcolor InvertMatrix(value=1.0)

    m """
    Naji clears his throat, eyes shifting away from mine.

    I frantically fish for something to say.
    """

    i "His shoulders are as broad as the shelves."
    m "Wow good thing I always have such useful thoughts."
