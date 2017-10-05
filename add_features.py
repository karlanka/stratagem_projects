import math
import numpy as np

def calc_angle(x,y):
    lp = 30.34
    rp = 37.66
    gw = 7.32

    if y > lp:
        y_lp = y - lp
    else:
        y_lp = lp - y

    if y > rp:
        y_rp = y - rp
    else:
        y_rp = rp - y

    dist_lp = math.sqrt(y_lp**2 + x**2)
    dist_rp = math.sqrt(y_rp**2 + x**2)

    cos_angle = (dist_lp**2 + dist_rp**2 - gw**2) / (2 * dist_lp * dist_rp)
    angle = math.acos(round(cos_angle,5))

    return round(math.degrees(angle),2)


def calc_distance_to_goal(x, y):

    lp = 30.34
    rp = 37.66

    if y >= rp:
        dist = math.sqrt(x ** 2 + (y - rp) ** 2)

    elif y <= lp:
        dist = math.sqrt(x ** 2 + (lp - y) ** 2)

    else:
        if lp < y <rp:
            dist = x

    # pitch_width = 68.0
    # dist = math.sqrt(x ** 2 + (pitch_width/2 - y) ** 2)

    return np.log(dist + 1)


def assist_distance(x1, x2, y1, y2):

    x = (x1 - x2) ** 2
    y = (y1 - y2) ** 2

    return math.sqrt(x+y)
