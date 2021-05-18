import keyboard
import time
import pyautogui
import requests
import random
import string

# You don't need to install any modules when running it as an exe!

def screenshot():
    press = '0'
    amount = '1'
    theprefix = ']'
    while True:  # INFITE LOOP TIME!
        if keyboard.is_pressed("SHIFT"):
            if keyboard.is_pressed("Z"):
                theprefix = input("Please enter a new prefix!\n")
                print("Saved, you can now press", theprefix, "to screenshot your game!")
        if keyboard.is_pressed(theprefix):  # if the assaigned key is pressed
            if press == '1':
                pass
            elif press == '0':
                print('File has been saved')
                letters = string.ascii_lowercase
                result_str = ''.join(random.choice(letters) for i in range(6))
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save(r(pathh, '\Images\SCAMMER{}.png'.format(result_str) ) # Where it saves the file! (Change the (INSERTPATHHERE), with the path leading to the images folder!
                press = '1'
                time.sleep(5)
                press = '0'
                pass
        else:
            pass  # if user pressed a key other than the assigned key, then it will pass


global pathh


pathh = input("Please enter the path that you'd like me to save the images in.\n")
print("Stored, I will automatically re-route your photos to this area! (If you want to change it, restart the program!
screenshot()
