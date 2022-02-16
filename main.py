from pynput.keyboard import Key, Listener
from gokubot import Actions
from gokutranslator import GokuTranslator
from threading import Thread
import time

class Goku(Actions,GokuTranslator):
    def __init__(self,posPath):
        self.posPath=posPath
        self.gokutranslator=GokuTranslator(posPath)
        self.actions=Actions()
        self.instructions=self.gokutranslator.getInstructions()
        self.pause=False
        self.end=False
    def translateInstruction(self,key,value):
        if key.find('CLICK')>=0:
            self.actions.click(value[0],value[1])
        elif key.find('SLEEP')>=0:
            time.sleep(value)
        elif key.find('WAITFOR')>=0:
            self.actions.waitFor(value)
        elif key.find('WAITBATTLE')>=0:
            self.actions.waitBattle()
        elif key.find('SKIP')>=0:
            self.actions.skip()
    def on_press(self,key):
        pass
    def on_release(self,key):
        try:
            if key == Key.esc:
                self.end=True
                return False
            elif key.char == 'p':
                if not self.pause:
                    print("Paused")
                    self.pause=True
                else:
                    print("Not Paused")
                    self.pause=False
        except:
            print('Errore')
    def executeInstructions(self,skipStart=False):
        if not skipStart: # Start
            for i in self.instructions:
                if i != 'loop':
                    for j in self.instructions[i]:
                        while self.pause:
                            pass
                        self.translateInstruction(j,self.instructions[i][j])
        while not self.end: # Loop
            for i in self.instructions['loop']:
                print(i)
                while self.pause:
                    pass
                if self.end:
                    break
                self.translateInstruction(i,self.instructions['loop'][i])
    def start(self):
        print("Started")
        execute=Thread(target=self.executeInstructions,args=(False,))
        execute.start()
        with Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()
if __name__ == "__main__":
    goku = Goku('scripts/dbl.txt')
    goku.start()