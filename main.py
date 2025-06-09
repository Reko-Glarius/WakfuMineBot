import numpy as np 
import cv2
import pyautogui as pg
import pydirectinput as pdi

template = cv2.imread("tem2.png")
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)


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
        pdi.keyDown('b')
        pdi.keyUp('b')