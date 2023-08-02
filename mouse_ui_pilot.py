import pyautogui
# import time

class Mouse:
    def __init__(self):
        self.size = pyautogui.size()
        print(self.size.height)
        print(self.size.width)
        pass
        
    def pos(self, x:int, y:int, time:float):
        print(f"mouse move to: {x}, {y}")
        pyautogui.moveTo(x, y, time)


    def click(self, x:int, y:int, clicks:int = 2, interval:float = 0.2, button:str = "left"):
        pyautogui.click(x, y, clicks, interval, button)
    
    def scroll(self, then:int, x:int, y:int):
        pyautogui.scroll(then, x, y)