screen choice_history(history):
    frame:
        xpos 0.1
        ypos 0.1
        xmaximum 0.8
        ymaximum 0.8
        background Solid("#ffffffbf")
        vbox:
            viewport id "vp":
                draggable True
                mousewheel True
                scrollbars "vertical"

                vbox:
                    for choice in history:
                        text choice:
                            line_spacing 5
                            xalign 0.5
                        add "divider" xalign 0.5