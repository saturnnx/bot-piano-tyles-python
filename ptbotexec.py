import pygame
import pyautogui
import keyboard
import time
import win32api, win32con


pygame.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Piano Tiles Bot")
clock = pygame.time.Clock()
running = True
font = pygame.font.Font(None, 26)

def click(x, y):

        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill("black")

    
    text = font.render("Piano tiles bot...Press R to play and Q to stop!", True, "white")
    screen.blit(text, (70, 120))


    if keyboard.is_pressed('r'):
            if pyautogui.pixel(838,450)[0] == 0:
                click(838,450)
            if pyautogui.pixel(918,450)[0] == 0:
                click(918,450)
            if pyautogui.pixel(996,450)[0] == 0:
                click(996,450)
            if pyautogui.pixel(1075,450)[0] == 0:
                click(1075,450)    
        
    if keyboard.is_pressed('q'):
            running = False    
    
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()