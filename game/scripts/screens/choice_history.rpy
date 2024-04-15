screen choice_history(history):
    frame:
        background Frame("insights-page.png")
        align (0.5, 0.5)
        xsize 1600
        ysize 1000
        vbox:
            xpos 0.1
            ypos 0.2
            viewport id "vp":
                xmaximum 1420
                ymaximum 780
                draggable True
                mousewheel True
                scrollbars "vertical"
                vbox:
                    for choice in history:
                        text "{font=JustAnotherHand-Regular.ttf}[choice]{/font}":
                            line_spacing 5
                        add "divider"
