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
    easein 0.2 yoffset -50
    easeout 0.2 yoffset 0
    easein 0.2

transform pushback(duration=0.5):
    xcenter 0.5
    ycenter 0.5
    linear 0.1 xalign 0.55 yalign 0.45
    linear 0.1 xalign 0.5 yalign 0.5

transform squirm:
    xcenter 0.5
    ycenter 0.5
    linear 0.3 xalign 0.52
    linear 0.3 xalign 0.5
    linear 0.3 xalign 0.42
    linear 0.3 xalign 0.5
    linear 0.3 xalign 0.52
    linear 0.3 xalign 0.5



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
