default icon_pos_x = 1640
default gym_pos_y = 216
default lounge_pos_y = 440
default work_pos_y = 684
default morning_assigned = False
default day_assigned = False
default evening_assigned = False

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