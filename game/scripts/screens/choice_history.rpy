screen choice_history(history):
    frame:
        background Frame("insights-page.png")
        xalign 0.5
        yalign 0.5
        vbox:
            xpos 0.2
            ypos 0.2
            viewport id "vp":
                draggable True
                mousewheel True
                scrollbars "vertical"
                vbox:
                    xmaximum 1000
                    ymaximum 400
                    for choice in history:
                        text "{font=JustAnotherHand-Regular.ttf}[choice]{/font}":
                            line_spacing 5
                        add "divider"
