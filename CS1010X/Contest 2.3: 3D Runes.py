from runes import *

def get_peak(n=25, pic=circle_bb):
    res = pic
    for i in range(2, n+1):
        layer = scale((n+1-i)/n, pic)
        res = overlay_frac(1/i, layer, res)
    return hollusion(res)



show(get_peak())
