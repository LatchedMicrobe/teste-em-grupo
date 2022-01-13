#pokemon daycare grinder emerald, but you can use for whatever you want (educational purposes)
#made by two handsome devs named micr0be and LucasPP5 of the Platina Studios

import time
import pyautogui

#first we made an infinite loop to make the grinder more efficient
while True:
    #we are using visualboy advance, which has the space to speed up function, so the space here is optional
    pyautogui.keyDown('space')
    start = time.time()
    hold_time = 2
    while time.time() - start < hold_time:
        pyautogui.keyDown('a')
    pyautogui.keyUp('a')
    start = time.time()
    while time.time() - start < hold_time:
        pyautogui.keyDown('d')
    pyautogui.keyUp('d')


