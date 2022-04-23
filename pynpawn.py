import time

version = '1.0'


class Mouse():
    import pynput
    mouse = pynput.mouse()
    


    


    
    
    class autoclick():
        def __init__(self, running):
            self.running = False
        super().__init__()


        def clicks(button='left', delay='1'):
        
            import pyautogui

            running = True
        
            if button == 'left':

                while running == True:
                    pyautogui.leftClick()
                    time.sleep(delay)
            else:
                while running == True:
                    pyautogui.rightClick()
                    time.sleep(delay)

        def stop():
            running = False




class gui():
   


    def UI(t='UI'):
        import tkinter as tk
        tk.Tk().title(t)
        


    def textbutton(ui, Text, bcg):
        import tkinter as tk

        tk.Button(ui, text=Text, bg=bcg)
    def imagebutton(ui, Ima, bcg):
        import tkinter as tk
        Im = tk.PhotoImage(file=Ima)
        tk.Button(tk.Tk(), image=Im, bg=bcg)
    def textlabel(ui, Text, bcg):
        import tkinter as tk
        tk.Label(ui, text=Text, bcg=bcg)
    def mainloop():
        import tkinter as tk
        tk.Tk().title('pynpawn UI')
gui.mainloop()

    







        