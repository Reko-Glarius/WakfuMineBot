#################################################
# Libraries
#################################################

# Own Libraries
from flows import farmer_flow, herbalist_flow
from flows import mining_flow 

# Third-party Libraries
import numpy as np 
import cv2
import pyautogui as pg
import pydirectinput as pdi

#################################################
# Variables for template Matching
#################################################

# Button for Actions
button = cv2.imread("resources/miner/mine_icon.png")
template_gray = cv2.cvtColor(button, cv2.COLOR_BGR2GRAY)

# Detect element for interaction
resource_reads = []
resorce_templates = []




th = 0.7

while(True):
    var = 0

    screenshot = cv2.cvtColor(np.array(pg.screenshot()), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gray, template_gray, cv2.TM_CCOEFF_NORMED)

    loc = np.where(res >= th)

    for i in zip(*loc[::-1]):
        var += 1

    if(var!= 0):
        pdi.keyDown('j')
        pdi.keyUp('j')