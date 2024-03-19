default icon_pos_x = 1640
default gym_pos_y = 216
default lounge_pos_y = 440
default work_pos_y = 684
default morning_assigned = False
default day_assigned = False
default evening_assigned = False
default weekend_event = ""
default gym_text = "Mornings are at the gym! Gotta start the day strong with my favorite workout — Spotting hot guys."
default office_text = "Primetime is grind time. I managed to land my dream job at a PR firm. I’m so excited to make a difference in the world!"
default lounge_text = "At the end of the day, I'll unwind with a drink. One of my friends from home is a bartender!"

init python:
    def item_dragged(dragged_items, dropped_on):
        global morning_assigned, day_assigned, evening_assigned
        if dropped_on is not None:
            if dropped_on.drag_name == "morning":
                if dragged_items[0].drag_name == "gym":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    dragged_items[0].draggable = False
                    morning_assigned = True
                elif dragged_items[0].drag_name == "lounge":
                    dragged_items[0].snap(icon_pos_x, lounge_pos_y, 0.5)
                elif dragged_items[0].drag_name == "work":
                    dragged_items[0].snap(icon_pos_x, work_pos_y, 0.5)
            elif dropped_on.drag_name == "day":
                if dragged_items[0].drag_name == "gym":
                    dragged_items[0].snap(icon_pos_x, gym_pos_y, 0.5)
                elif dragged_items[0].drag_name == "lounge":
                    dragged_items[0].snap(icon_pos_x, lounge_pos_y, 0.5)
                elif dragged_items[0].drag_name == "work":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    dragged_items[0].draggable = False
                    day_assigned = True
            elif dropped_on.drag_name == "evening":
                if dragged_items[0].drag_name == "gym":
                    dragged_items[0].snap(icon_pos_x, gym_pos_y, 0.5)
                elif dragged_items[0].drag_name == "lounge":
                    dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.1)
                    dragged_items[0].draggable = False
                    evening_assigned = True
                elif dragged_items[0].drag_name == "work":
                    dragged_items[0].snap(icon_pos_x, work_pos_y, 0.5)
            if morning_assigned and day_assigned and evening_assigned:
                renpy.jump("planner_tutorial_success")

screen planner_drag():
    draggroup:
        drag:
            pos (icon_pos_x, gym_pos_y)
            drag_raise True
            drag_name "gym"
            dragged item_dragged
            add "icons/gym.png"
        drag:
            pos (icon_pos_x, lounge_pos_y)
            drag_raise True
            drag_name "lounge"
            dragged item_dragged
            add "icons/lounge.png"
        drag:
            pos (icon_pos_x, work_pos_y)
            drag_raise True
            drag_name "work"
            dragged item_dragged
            add "icons/work.png"
        drag:
            pos (208, 253)
            draggable False
            drag_name "morning"
            image Solid("#D3C6ED") xysize(150, 150)
        drag:
            pos (210, 543)
            draggable False
            drag_name "day"
            image Solid("#DBC6E5") xysize(150, 150)
        drag:
            pos (214, 817)
            draggable False
            drag_name "evening"
            image Solid("#E4D3D2") xysize(150, 150)

init python:
    def weekend_activity(dragged_items, dropped_on):
        global weekend_event
        if dropped_on is not None:
            weekend_event = dragged_items[0].drag_name
            return True

screen planner_weekend():
    draggroup:
        drag:
            pos (icon_pos_x, 440)
            drag_raise True
            drag_name "going_out"
            dragged weekend_activity
            add "icons/lounge.png"
        drag:
            pos (icon_pos_x, 216)
            drag_raise True
            drag_name "bathtime"
            dragged weekend_activity
            add "icons/bathtime.png"
        drag:
            pos (1046, 343)
            draggable False
            drag_name "weekend"
            image Solid("#F0D5E8") xysize(261, 263)

screen open_planner:
    imagebutton:
        xpos 1780
        ypos 140
        anchor(0.5, 0.5)
        idle "icons/Planner-icon idle.png"
        hover "icons/Planner-icon hover.png"
        action ShowMenu("opened_planner")

screen opened_planner:
    add "planner-base-check.png"
    text "{font=PatuaOne-Regular.ttf}{size=100}{color=#B8556C}[week]{/size}{/font}{/color}":
        xpos 778
        ypos 154
        yanchor renpy.BASELINE
    text "Self-Awareness: [self_awareness]" size 40:
        xpos 1054
        ypos 628
    vbox:
        xpos 580
        ypos 287
        xmaximum 350
        ymaximum 400
        text "[gym_text]" font "JustAnotherHand-Regular.ttf"
    vbox:
        xpos 580
        ypos 570
        xmaximum 350
        ymaximum 410
        text "[office_text]" font "JustAnotherHand-Regular.ttf"
    vbox:
        xpos 580
        ypos 850
        xmaximum 350
        ymaximum 410
        text "[lounge_text]" font "JustAnotherHand-Regular.ttf"

    imagebutton:
        xpos 1620
        ypos 105
        anchor(0.5, 0.5)
        idle "icons/close idle.png"
        hover "icons/close hover.png"
        action Return()
    showif weekend_event == "bathttime" or weekend_event == "":
        add "icons/Bathtime.png" xpos 1260 ypos 370
    showif weekend_event == "going_out":
        add "icons/lounge.png" xpos 1260 ypos 370
