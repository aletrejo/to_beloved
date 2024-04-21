screen insight(thoughts):
    zorder 100
    style_prefix "insight"
    vbox at insight_transform:
        for thought in thoughts:
            frame:
                text "{b}Insight{/b}: [thought]":
                    xmaximum 400

    timer 2.5 action Hide('insight')

transform insight_transform:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style insight_frame:
    background Frame("gui/insight_bg.png", gui.notify_frame_borders, tile=False)
    padding (50, 50)


style insight_vbox:
    align(0.15, 0.25)
    spacing 20

init python:
    def check_for_matches(insights, choices):
        matches_found = []
        for insight in insights:
            if insight in choices:
                matches_found.append(insight)
                renpy.play ("audio/insight-chime.mp3")
        return matches_found

screen open_insights:
    imagebutton:
        xpos 1570
        ypos 140
        anchor(0.5, 0.5)
        idle "icons/insights idle.png"
        hover "icons/insights hover.png"
        action ShowMenu("opened_insights")

screen opened_insights:
    add "insights-page.png" at truecenter
    vbox:
        xpos 390
        ypos 256
        viewport id "vp":
            xmaximum 1280
            ymaximum 770
            draggable True
            mousewheel True
            scrollbars "vertical"
            vbox:
                for thought in bathtime_1_choices:
                        text "{font=JustAnotherHand-Regular.ttf}{size=50}[thought]{/size}{/font}":
                            line_spacing 5
                        add "divider"

    imagebutton:
        xpos 1620
        ypos 105
        anchor(0.5, 0.5)
        idle "icons/close idle.png"
        hover "icons/close hover.png"
        action Return()

style oinsight_frame:
    padding gui.notify_frame_borders.padding
