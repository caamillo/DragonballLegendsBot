import win32api, win32con
import random as rnd
import pyautogui as pag
import time

class Actions:
    def __init__(self):
        pass
    def click(self,x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.5)
    def waitFor(self,who):
        while True:
            if pag.locateOnScreen(f'src/{who}.png',grayscale=True,confidence=0.8) != None:
                break
            self.click(934,996)
            time.sleep(1)
    def getRandomAttack(self):
        return rnd.choice(['g','h','j','k'])
    def keyDown(self,key):
        pag.keyDown(key)
        time.sleep(0.1)
        pag.keyUp(key)
        time.sleep(0.2)
    def waitBattle(self):
        while True:
            while pag.locateOnScreen('src/goku.png',grayscale=True,confidence=0.8) != None:
                self.keyDown(self.getRandomAttack())
            if pag.locateOnScreen('src/ok.png',grayscale=True,confidence=0.8) != None:
                time.sleep(0.5)
                break
            else:
                self.click(941,804)
                time.sleep(0.5)
    def skip(self):
        while pag.locateOnScreen('src/startbattle.png',grayscale=True,confidence=0.8) == None:
            if pag.locateOnScreen('src/skip.png',grayscale=True,confidence=0.8) != None:
                self.click(1123,64) # Skip
                time.sleep(1)
                self.click(1063,685) # Yes
                time.sleep(4)
            time.sleep(1)