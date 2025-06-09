import numpy as np 
import cv2
import pyautogui as pg
import pydirectinput as pdi

def get_mine_starting_data():
    return "miner", "",{
        1: "primitive_iron",
        2: "finest_sea_salt",
        3: "classic_coal",
        4: "bright_copper",
        5: "shadowy_cobalt",
        6: "",
        7: "",
    }

def mining_action(screenshot_gray, button_template):
    # Captura de pantalla actual
    # Template match para el botón
    res = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.7)  # Puedes ajustar el threshold si hace falta

    for pt in zip(*loc[::-1]):
        h, w = button_template.shape
        center_x = pt[0] + w // 2
        center_y = pt[1] + h // 2

        # Mueve y hace clic izquierdo en el botón
        pg.moveTo(center_x, center_y, duration=0.1)
        pg.click(button='left')
        print("Recurso recolectado.")
        return True  # Botón encontrado y acción realizada

    return False  # Botón no detectado