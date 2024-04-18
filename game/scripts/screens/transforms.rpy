transform laughter:
    xcenter 0.5
    ycenter 0.5
    easein 0.15 yoffset 30
    easeout 0.15 yoffset 0
    easein 0.15 yoffset 30
    easeout 0.15 yoffset 0

transform hop:
    xcenter 0.5
    ycenter 0.5
    easein 0.15 yoffset -50
    easeout 0.08 yoffset 0

transform pushback(duration=0.5):
    xcenter 0.5
    ycenter 0.5
    linear 0.1 xalign 0.55 yalign 0.45
    linear 0.1 xalign 0.5 yalign 0.5

transform shake:
        xcenter 0.5
        ycenter 0.5
        ease .06 yoffset 24
        ease .06 yoffset -24
        ease .05 yoffset 20
        ease .05 yoffset -20
        ease .04 yoffset 16
        ease .04 yoffset -16
        ease .03 yoffset 12
        ease .03 yoffset -12
        ease .02 yoffset 8
        ease .02 yoffset -8
        ease .01 yoffset 4
        ease .01 yoffset -4
        ease .01 yoffset 0

transform squirm:
    xcenter 0.5
    ycenter 0.5
    ease .06 xoffset 24
    ease .06 xoffset -24
    ease .05 xoffset 20
    ease .05 xoffset -20
    ease .04 xoffset 16
    ease .04 xoffset -16
    ease .03 xoffset 12
    ease .03 xoffset -12
    ease .02 xoffset 8
    ease .02 xoffset -8
    ease .01 xoffset 4
    ease .01 xoffset -4
    ease .01 xoffset 0


transform crouch:
    xcenter 0.5
    ycenter 0.5
    ease 3 yoffset 700

transform citynightappear:
    alpha 0.0
    pause 0.5
    linear 0.8 alpha 1.0

transform najiappear:
    alpha 0.0
    pause 1.5
    linear 0.8 alpha 1.0

transform jouleappear:
    alpha 0.0
    pause 2.5
    linear 0.8 alpha 1.0

transform devappear:
    alpha 0.0
    pause 3.5
    linear 0.8 alpha 1.0

transform menmiappear:
    alpha 0.0
    pause 4.5
    linear 1.5 alpha 1.0

transform titleappear:
    alpha 0.0
    pause 6.5
    linear 2.0 alpha 1.0

transform navappear:
    alpha 0.0
    pause 9.5
    linear 1.0 alpha 1.0
