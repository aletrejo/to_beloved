default stickers = []

init python:
    class Sticker:
        def __init__(self, img, xpos=0, ypos=0):
            self.img = "stickers/sticker-" + img + ".png"
            self.xpos = xpos
            self.ypos = ypos

        def set_xpos(self, value):
            self.xpos = value

        def get_xpos(self):
            return self.xpos

        def set_ypos(self, value):
            self.ypos = value

        def get_ypos(self):
            return self.ypos

        def get_img(self):
            return self.img

    def sticker_dropped(dropped_on, dragged_items):
        global stickers
        if len(dragged_items) > 0:
            sticker = Sticker(dragged_items[0].drag_name, dragged_items[0].x, dragged_items[0].y)
            stickers.append(sticker)
            dragged_items[0].draggable = False


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


screen planner_with_stickers():
    add "planner-cover-[planner_cover].png":
        align (0.5, 0.5)
    for sticker in stickers:
        add sticker.img:
            xpos sticker.xpos
            ypos sticker.ypos
    text "{font=PatuaOne-Regular.ttf}{size=60}{color=#EB266A}Week [week]{/size}{/font}{/color}":
        align (0.4, 0.37)
