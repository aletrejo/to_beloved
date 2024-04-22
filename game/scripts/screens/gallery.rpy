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

    grid 4 4:

        xfill True
        yfill True

        add g.make_button(name="alt_title", unlocked="images/gallery/tobeloved-title-screen-alt copy.jpeg", xalign=0.5, yalign=0.5)
        add g.make_button(name="alleyway", unlocked="images/gallery/alleyway copy.png", xalign=0.5, yalign=0.5)
        add g.make_button(name="applecore", unlocked="images/gallery/applecore-city copy.png", xalign=0.5, yalign=0.5)
        add g.make_button(name="bakery", unlocked="images/gallery/bakery copy.png", xalign=0.5, yalign=0.5)
        add g.make_button(name="bathtime-classic", unlocked="images/gallery/bathtime-classic copy.png", xalign=0.5, yalign=0.5)
        add g.make_button(name="bathtime-fruity", unlocked="images/gallery/bathtime-fruity copy.png", xalign=0.5, yalign=0.5)
        add g.make_button(name="bathtime-romantic", unlocked="images/gallery/Bathtime-romantic copy.png", xalign=0.5, yalign=0.5)
        add g.make_button(name="gym", unlocked="images/gallery/gym-inside copy.png", xalign=0.5, yalign=0.5)
        add g.make_button(name="lounge", unlocked="images/gallery/lounge-inside copy.png", xalign=0.5, yalign=0.5)
        add g.make_button(name="office", unlocked="images/gallery/office-inside copy.png", xalign=0.5, yalign=0.5)
        add g.make_button(name="park", unlocked="images/gallery/park-day copy.png", xalign=0.5, yalign=0.5)
        add g.make_button(name="naji-park", unlocked="images/gallery/naji-park-breeze copy.png", xalign=0.5, yalign=0.5)
        add g.make_button(name="devan", unlocked="images/gallery/devan-neutral copy.png", xalign=0.5, yalign=0.5)
        add g.make_button(name="joule", unlocked="images/gallery/joule-neutral copy.png", xalign=0.5, yalign=0.5)
        add g.make_button(name="naji-bar", unlocked="images/gallery/naji-bar-neutral copy.png", xalign=0.5, yalign=0.5)
        add g.make_button(name="naji-neutral", unlocked="images/gallery/naji-neutral copy.png", xalign=0.5, yalign=0.5)

    textbutton "Return" action Return() xalign 0.95 yalign 0.95
