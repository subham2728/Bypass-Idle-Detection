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
        print("Running in : ")
        for x in range(5,-1,-1):
            print(x)
            time.sleep(1) 
        inside_loop=1
        now=datetime.now()
        current_time=now.strftime("%H:%M:%S")
        for i in range(0,50):
            pyautogui.moveTo(700,i*5)
        if(count_script_call%2==0):
            for i in range(0,3):
                pyautogui.press('shift')
                time.sleep(1) 
                print("Pressed Shfit Key") 
            print("")  
        else:
            for i in range(0,3):
                pyautogui.press('left')
                time.sleep(1) 
                print("Pressed Left Arrow Key")
            print("")
        print("Automated" , count_script_call , "times",end= " ")
        print("at Time = ", current_time)
        print("")
    
