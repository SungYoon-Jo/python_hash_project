import numpy as np
from PIL import Image
import colorsys

def revised_rgb_to_hsv(r, g, b):
    (h, s, v) = colorsys.rgb_to_hsv(r/255, g/255, b/255)
    h *= 360
    s *= 100
    v *= 100
    return h, s, v

print(revised_rgb_to_hsv(211, 193, 231))

