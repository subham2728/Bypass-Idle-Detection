#pip install pyautogui
import pyautogui
import time
from datetime import datetime
def random_auto(count_script_call):
    pyautogui.FAILSAFE=False
    i=0
    print("")
    print("Script Started ")
    print("-----------------")
    print("")
    while(i<1):
        # time.sleep(20)
        inside_loop=1
        now=datetime.now()
        current_time=now.strftime("%H:%M:%S")
        for i in range(0,50):
            pyautogui.moveTo(700,i*5)
        if(count_script_call%2==0):
            for i in range(0,3):
                pyautogui.press('shift')
                print("Pressed Shfit Key")   
        else:
            for i in range(0,3):
                pyautogui.press('left')
                print("Pressed Left Arrow Key")
        print("Automated" , count_script_call , "times",end= " ")
        print("at Time = ", current_time)
    