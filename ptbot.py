import pyautogui
import keyboard
import time
import win32api, win32con

print('Piano tiles bot...\nPress R to play and Q to stop!')

def click(x,y):

    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while True:

    if keyboard.is_pressed('r'):
        if pyautogui.pixel(838,450)[0] == 0:
            click(838,450)
        if pyautogui.pixel(918,450)[0] == 0:
            click(918,450)
        if pyautogui.pixel(996,450)[0] == 0:
            click(996,450)
        if pyautogui.pixel(1075,450)[0] == 0:
            click(1075,450)
    else:
        time.sleep(0.01)
        if keyboard.is_pressed('q'):
            break