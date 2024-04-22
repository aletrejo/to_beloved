init python:
    g = Gallery()
    g.transition = dissolve
    g.button("alt_title")
    g.image("images/gallery/tobeloved-title-screen-alt.jpeg")
    g.button("alleyway")
    g.image("images/gallery/alleyway.png")
    g.button("applecore")
    g.image("images/gallery/applecore-city.png")
    g.button("bakery")
    g.image("images/gallery/bakery.png")
    g.button("bathtime-classic")
    g.image("images/gallery/bathtime-classic.png")
    g.button("bathtime-fruity")
    g.image("images/gallery/bathtime-fruity.png")
    g.button("bathtime-romantic")
    g.image("images/gallery/Bathtime-romantic.png")
    g.button("gym")
    g.image("images/gallery/gym-inside.png")
    g.button("lounge")
    g.image("images/gallery/lounge-inside.png")
    g.button("office")
    g.image("images/gallery/office-inside.png")
    g.button("park")
    g.image("images/gallery/park-day.png")
    g.button("naji-park")
    g.image("images/gallery/naji-park-breeze.png")
    g.button("devan")
    g.image("images/gallery/devan-neutral.png")
    g.button("joule")
    g.image("images/gallery/joule-neutral.png")
    g.button("naji-bar")
    g.image("images/gallery/naji-bar-neutral.png")
    g.button("naji-neutral")
    g.image("images/gallery/naji-neutral.png")

screen gallery:
    tag menu
    add "planner-page-bg"

    frame:
        background None
        xysize(0.9, 0.9)
        xpos 100
        ypos 20
        grid 4 4:
            xfill True
            yfill True

            add g.make_button(name="alt_title", unlocked="images/gallery/tobeloved-title-screen-alt thumbnail.jpeg", xalign=0.5, yalign=0.5)
            add g.make_button(name="alleyway", unlocked="images/gallery/alleyway thumbnail.png", xalign=0.5, yalign=0.5)
            add g.make_button(name="applecore", unlocked="images/gallery/applecore-city thumbnail.png", xalign=0.5, yalign=0.5)
            add g.make_button(name="bakery", unlocked="images/gallery/bakery thumbnail.png", xalign=0.5, yalign=0.5)
            add g.make_button(name="bathtime-classic", unlocked="images/gallery/bathtime-classic thumbnail.png", xalign=0.5, yalign=0.5)
            add g.make_button(name="bathtime-fruity", unlocked="images/gallery/bathtime-fruity thumbnail.png", xalign=0.5, yalign=0.5)
            add g.make_button(name="bathtime-romantic", unlocked="images/gallery/Bathtime-romantic thumbnail.png", xalign=0.5, yalign=0.5)
            add g.make_button(name="gym", unlocked="images/gallery/gym-inside thumbnail.png", xalign=0.5, yalign=0.5)
            add g.make_button(name="lounge", unlocked="images/gallery/lounge-inside thumbnail.png", xalign=0.5, yalign=0.5)
            add g.make_button(name="office", unlocked="images/gallery/office-inside thumbnail.png", xalign=0.5, yalign=0.5)
            add g.make_button(name="park", unlocked="images/gallery/park-day thumbnail.png", xalign=0.5, yalign=0.5)
            add g.make_button(name="naji-park", unlocked="images/gallery/naji-park-breeze thumbnail.png", xalign=0.5, yalign=0.5)
            add g.make_button(name="devan", unlocked="images/gallery/devan-neutral thumbnail.png", xalign=0.5, yalign=0.5)
            add g.make_button(name="joule", unlocked="images/gallery/joule-neutral thumbnail.png", xalign=0.5, yalign=0.5)
            add g.make_button(name="naji-bar", unlocked="images/gallery/naji-bar-neutral thumbnail.png", xalign=0.5, yalign=0.5)
            add g.make_button(name="naji-neutral", unlocked="images/gallery/naji-neutral thumbnail.png", xalign=0.5, yalign=0.5)

    textbutton "Return" action Return() xalign 0.95 yalign 0.97
