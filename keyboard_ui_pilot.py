import pyautogui as pag

class Keyboard:
    def __init__(self):
        pass
    
    def press(self, text: list, delay: float):
        
        print_text = []
        hk = []
        for char in text:
            if len(char) == 1 or (len(char) != 1 and "+" not in char):
                print_text.append(char)
            else:
                pag.typewrite(print_text, delay)
                # print_text.clear()
                print_text = []
                for _char in char.split("+"):
                    hk.append(_char.strip())
                pag.hotkey(*hk)
                # hk.clear()
                hk = []
                
        else:
            pag.typewrite(print_text, delay)
            
    def screenshot(self, name):
        pag.screenshot(name)
                
                
            
        