from runes import *


def create_tile(n=10, pic=heart_bb):
    pic = scale_independent(1, 1/6, heart_bb)
    res = translate(0, 0.5, pic)
    y = 0.32
    for i in range(9):
        res = overlay_frac(3/9, translate(0,y,pic), res)
        y -= 0.1
    return res

def grey_hearts(tile, n=5):
    if n == 1:
        return tile
    else:
        return eighth_turn_left(flip_vert(stack(beside(tile, tile), grey_hearts(stackn(n-1, tile), n-1))))
    
show(grey_hearts(create_tile()))


 
