screen insight(thoughts):
    zorder 100
    style_prefix "insight"
    vbox at insight_transform:
        for thought in thoughts:
            frame:
                text "{b}Insight{/b}: [thought]"

    timer 2 action Hide('insight')

transform insight_transform:
    xalign 0 yalign .1

    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style insight_frame:
    ypos .1
    #Reuse from notify screen
    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding


style insight_vbox:
    spacing 20

init python:
    def check_for_matches(insights, choices):
        matches_found = []
        for insight in insights:
            if insight in choices:
                matches_found.append(insight)
                renpy.play ("audio/insight-chime.mp3")
        return matches_found
