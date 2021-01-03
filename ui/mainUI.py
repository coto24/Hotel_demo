from tkinter import *
from ui.ui import MenuGaste, MenuZimmer, MenuReservierung, MenuHELP
import random
import tkinter.messagebox


class MainMenu:

    def __init__(self, root):
        self.__window = root
        self.__window.title('Main Menu')
        self.__window.geometry('560x300')
        self.top = Frame(self.__window)
        root.configure(background='Cadet Blue')
        """
        aux = Label(self.__window, text="                                                        ", background='Cadet Blue')
        aux.grid(column=0, row=0)
        aux2 = Label(self.__window, text="                                                        ",background='Cadet Blue')
        aux2.grid(column=0, row=2)
        """

        Tops = Frame(root,bg='Cadet Blue', bd=8, pady = 3, relief=RIDGE)
        Tops.grid(row=0,column=2)

        mesaj= Label(Tops,
                     font=('arial',15,'bold'),text="Hotel Arcasu' & CO", bd=6,bg='Cadet Blue',
                     fg='Cornsilk',justify=CENTER)
        mesaj.grid()
        mesaj2 = Label(self.__window, text="✯✯✯✯✯✯✯", fg='yellow', background='Cadet Blue')
        mesaj2.grid(column=2, row=1)


        self.button_gaste = Button(self.__window, text='Open Menu Guests', command=self.__draw_windowG, bg="lightsteelblue")
        self.button_gaste.grid(column=2, row=13,pady=2.5)

        self.button_zimmer = Button(self.__window, text='Open Menu Room', command=self.__draw_windowZ, bg="lightsteelblue")
        self.button_zimmer.grid(column=2, row=14,pady=2.5)

        self.button_reserv = Button(self.__window, text='Open Menu Reservation', command=self.__draw_windowR, bg="lightsteelblue")
        self.button_reserv.grid(column=2, row=15,pady=2.5)

        aux3 = Label(self.__window, text="                                                        ",background='Cadet Blue' )
        aux3.grid(column=0, row=16,pady=2.5)

        self.quit_button = Button(self.__window, text='Quit', command=self.__QuitWindow, bg="lightsteelblue")
        self.quit_button.grid(column=2, row=20,pady=2.5)

        self.help_button = Button(self.__window, text="HELP", command=self.__draw_windowH, bg="lightsteelblue")
        self.help_button.grid(column=2,row=16,pady=2.5)

    def __draw_windowH(self):
        help_window = Toplevel(self.__window)
        self.new = MenuHELP(help_window)
        help_window.title("HELP")
        help_window.geometry('300x300')

    def __draw_windowG(self):
        guest_window = Toplevel(self.__window)
        self.new = MenuGaste(guest_window)
        guest_window.title("Menu Guests")
        guest_window.geometry('500x400')

    def __draw_windowZ(self):
        room_window = Toplevel(self.__window)
        self.new = MenuZimmer(room_window)
        room_window.title("Menu Rooms")
        room_window.geometry('700x370')

    def __draw_windowR(self):
        rezerv_window = Toplevel(self.__window)
        self.new = MenuReservierung(rezerv_window)
        rezerv_window.title("Menu Reservations")
        rezerv_window.geometry('560x390')

    def __QuitWindow(self):
        self.__window.destroy()

