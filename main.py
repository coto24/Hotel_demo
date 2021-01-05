from tkinter import *
from ui.mainUI import MainMenu
#from mainUI import MainMenu
#from ui import Test

def main():

    root = Tk()

    '''
    g = MenuGaste(root)
    g.draw_window()
    mainloop()

    root2 = Tk()
    g2 = MenuZimmer(root2)
    g2.draw_window2()
    mainloop()

    root3 = Tk()
    g3 = MenuReservierung(root3)
    g3.draw_window3()
    mainloop()
    '''


    MainMenu(root)
    mainloop()

main()

"""
class Controler:
    def __init__(self):
        self.__repo = []
        self.i = 0


def __Print(self):
# resultLabel = Label(self.__window, text=str(control.print_guests()))


def print_guests(self):
    self.i+=1
    return "Ai apelat print_guests"+str(self.i)
"""
