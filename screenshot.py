import time
import pyautogui

def screenshots():
    name= int(round(time.time()*1000))
    name= f"C:/Users/LENOVO/Desktop/python projects/screenshots/{name}.png"
    times= time.sleep(2)
    img= pyautogui.screenshot(name)
    img.show()

screenshots()