#################################################
# Libraries
#################################################

# Own Libraries
from flows import farmer_flow, herbalist_flow
from flows import mining_flow 
from utils import utils

# Third-party Libraries
import numpy as np 
import cv2
import pyautogui as pg
import pydirectinput as pdi

#################################################
# Variables for template Matching
#################################################
# Variables
th = 0.7

# Button for Actions
button = cv2.imread("resources/miner/mine_icon.png")
template_gray = cv2.cvtColor(button, cv2.COLOR_BGR2GRAY)

# Detect element for interaction
resource_reads = []
resorce_templates = []

print("Iniciando creación Recursos")

for path in utils.search_files_from_text(path="resources/miner/", text="shadowy_cobalt"):
    resource_reads.append(cv2.imread(path))

for read in resource_reads:
    resorce_templates.append(cv2.cvtColor(read, cv2.COLOR_BGR2GRAY))

print("Creación tempaltes terminados")


print("Iniciando ciclos")
while(True):
    var = 0

    screenshot = cv2.cvtColor(np.array(pg.screenshot()), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    for template in resorce_templates:
        res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)

        loc = np.where(res >= th)

        for i in zip(*loc[::-1]):
            var += 1

    if(var!= 0):
        pdi.keyDown('j')
        pdi.keyUp('j')