default stickers = []

init python:
    class Sticker:
        def __init__(self, img, xpos=0, ypos=0):
            self.img = "stickers/sticker-" + img + ".png"
            self.xpos = xpos
            self.ypos = ypos
            self.name = img

    def sticker_dropped(dropped_on, dragged_items):
        global stickers
        if len(dragged_items) > 0:
            sticker = Sticker(dragged_items[0].drag_name, dragged_items[0].x, dragged_items[0].y)
            stickers.append(sticker)
            dragged_items[0].draggable = False
    def remove_sticker(sticker):
        global stickers
        for i, item in enumerate(stickers):
            if item.name == sticker:
                stickers.pop(i)

screen place_sticker(sticker):
    draggroup:
        drag:
            align (0.5, 0.5)
            draggable False
            droppable True
            dropped sticker_dropped
            add "planner-cover-[planner_cover].png"

        drag:
            align(0.5, 0.5)
            drag_raise True
            drag_name sticker
            add "stickers/sticker-[sticker].png"
    for s in stickers:
        add s.img:
            xpos s.xpos
            ypos s.ypos
    text "{size=30}{image=placestickertext}{/size}":
        xpos 0.37
        ypos 0.7
    textbutton "Skip":
        xpos 0.5
        ypos 0.8
        action [Function(remove_sticker, sticker), Return()]

screen relationship_up:
    add "pinkgradient.png" at backgroundappear
    add "images/doily-1.png" at rotation_repeat:
        zoom 0.9
        alpha 0.7
        xalign 0.2
        yalign 1.2
    add "images/doily-2.png" at rotation_repeat:
        zoom 1.0
        alpha 0.8
        xalign 0.7
        yalign 0.2
    add "images/doily-3.png" at rotation_repeat:
        zoom 0.7
        alpha 0.5
        xalign 0.2
        yalign 0.1
    add "images/[lover]-smile.png":
        xalign 0.5
        yalign 0.85
    text "[lover] feel closer to you!" at disappear_up:
        style "closer_text"
        
     


