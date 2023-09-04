import pyautogui as auto 
import time 

i=0
while i<=100:
    auto.write("hii")
    auto.press('enter')
    time.sleep(0.1)
    i=i+1