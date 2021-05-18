import keyboard
import time
import pyautogui
import requests
import random
import string

# You want to install these modules first before running, or use the requirements.txt file attached!

def screenshot():
    press = '0'
    amount = '1'
    while True:  # INFITE LOOP TIME!
        if keyboard.is_pressed(']'):  # if key ']' is pressed
            if press == '1':
                pass
            elif press == '0':
                print('File has been saved')
                letters = string.ascii_lowercase
                result_str = ''.join(random.choice(letters) for i in range(6))
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save(r'(INSERTPATHHERE)\Images\SCAMMER{}.png'.format(result_str) ) # Where it saves the file! (Change the (INSERTPATHHERE), with the path leading to the images folder!
                press = '1'
                time.sleep(5)
                press = '0'
                pass
        else:
            pass  # if user pressed a key other than ], then it will pass




screenshot()
