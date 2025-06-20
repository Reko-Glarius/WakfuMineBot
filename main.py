#################################################
# Libraries
#################################################

# Native libraries
import time

# Own Libraries
from flows import farmer_flow, herbalist_flow
from flows import mining_flow 
from utils import utils

# Third-party Libraries
import numpy as np 
import cv2
import pyautogui as pg
import pydirectinput as pdi
import keyboard

#################################################
# Variables for template Matching
#################################################
# Variables
th = 0.75
detected = None
filtered_pts_templates = []

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
    if keyboard.is_pressed('q'):
        print("Tecla 'q' presionada. Deteniendo el script.")
        break

    var = 0
    filtered_pts_templates = []

    screenshot = cv2.cvtColor(np.array(pg.screenshot()), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    if(detected):
        print("Comenzando minado")
        time.sleep(11)
        detected = False
        print("minado terminado, reiniciando proceso")

    else:
        print("comenzando busqueda")
        for template in resorce_templates:
            res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)

            loc = np.where(res >= th)

            for pt in zip(*loc[::-1]):
                h, w = template.shape  # Tamaño del template
                center_x = pt[0] + w // 2
                center_y = pt[1] + h // 2

                if not utils.is_nearby(filtered_pts_templates, (center_x, center_y), min_distance=40):
                    filtered_pts_templates.append((center_x, center_y))

            for center_x, center_y in filtered_pts_templates:
                print(center_x, center_y)
                pg.moveTo(center_x, center_y, duration=0.2)
                pg.click(button='right')

                time.sleep(0.4)

                screenshot = cv2.cvtColor(np.array(pg.screenshot()), cv2.COLOR_RGB2BGR)
                gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
                action = mining_flow.mining_action(screenshot_gray=gray, button_template=template_gray)

                if action:
                    print("Action Button Detected")
                    detected = True
                    break

                """ # Mueve el mouse al centro del match
                pg.moveTo(center_x, center_y, duration=0.2)

                # Clic derecho
                pg.click(button='right')

                screenshot = cv2.cvtColor(np.array(pg.screenshot()), cv2.COLOR_RGB2BGR)
                gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
                action = mining_flow.mining_action(screenshot_gray=gray, button_template=template_gray)
                
                # Ejecuta la acción de minería
                if(action):
                    print("Action Button Detected")
                    detected = True
                    break
                else:
                    continue """
                    
            if(detected):
                print("Breaking for of mining templates")
                break


    if(var!= 0):
        pdi.keyDown('j')
        pdi.keyUp('j')