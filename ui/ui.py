from tkinter import *

from entity.gast import gast
from entity.zimmer import zimmer
from entity.reservierung import reservierung




class MenuGaste:
    def __init__(self, gui_master, control):
        self.__window = gui_master
        self.__controler = control
        gui_master.configure(background='Cadet Blue')
        self.__Gast_name_txt = Entry(self.__window, width=20, bg="lightsteelblue")
        self.__Gast_vorname_txt = Entry(self.__window, width=20, bg="lightsteelblue")
        self.__Gast_nameneu_txt = Entry(self.__window, width=20, bg="lightsteelblue")

        # butoane pt add_guest
        btn = Button(self.__window, text='Add guest', command=self.__createGuest, bg="lightsteelblue")
        btn.grid(column=0, row=0)
        nachname = Label(self.__window, text='Last Name', bg="lightsteelblue", font=('arial', 9, 'bold'), relief=RIDGE)
        nachname.grid(column=1, row=1)
        self.__Gast_name_txt.grid(column=2, row=1)
        vorname = Label(self.__window, text='First Name', bg="lightsteelblue", font=('arial', 9, 'bold'), relief=RIDGE)
        vorname.grid(column=1, row=2)
        self.__Gast_vorname_txt.grid(column=2, row=2)

        # butoane pt update_guest
        btn2 = Button(self.__window, text='Update the Last name', command=self.__updateGuestName, bg="lightsteelblue")
        btn2.grid(column=1, row=0)
        nachname_neu = Label(self.__window, text='New Last Name', bg="lightsteelblue", font=('arial', 9, 'bold'),
                             relief=RIDGE)
        nachname_neu.grid(column=1, row=5)
        self.__Gast_nameneu_txt.grid(column=2, row=5)

        # butoane pt delete_guest
        btn3 = Button(self.__window, text='Delete guest from list', command=self.__deleteGuest, bg="lightsteelblue")
        btn3.grid(column=2, row=0)

        # butoane pt print_guests
        btn4 = Button(self.__window, text='Print all the guests', command=self.__Print, bg="lightsteelblue")
        btn4.grid(column=3, row=0)

        # quit button
        aux = Label(self.__window, text="                                     ", bg="cadet blue")
        aux.grid(column=1, row=6)
        btn5 = Button(self.__window, text='Quit', command=self.__QuitWindow, bg="lightsteelblue")
        btn5.grid(column=0, row=7)

        # save/load buttons
        savebtn = Button(self.__window, text='Save data', command=self.__SaveData, bg="lightsteelblue")
        savebtn.grid(column=1, row=6)
        loadbtn = Button(self.__window, text='Load data', command=self.__LoadData, bg="lightsteelblue")
        loadbtn.grid(column=2, row=6)

    def __createGuest(self):
        Gast = gast(self.__Gast_name_txt.get(), self.__Gast_vorname_txt.get())
        self.__controler.add_guest(Gast)

        self.__Gast_name_txt.delete(0, 'end')
        self.__Gast_vorname_txt.delete(0, 'end')

    def __updateGuestName(self):
        Gast = gast(self.__Gast_name_txt.get(), self.__Gast_vorname_txt.get())
        self.__controler.update_guest(Gast, self.__Gast_nameneu_txt.get())

        self.__Gast_name_txt.delete(0, 'end')
        self.__Gast_vorname_txt.delete(0, 'end')
        self.__Gast_nameneu_txt.delete(0, 'end')

    def __deleteGuest(self):
        Gast = gast(self.__Gast_name_txt.get(), self.__Gast_vorname_txt.get())
        self.__controler.delete_guest(Gast)

        self.__Gast_name_txt.delete(0, 'end')
        self.__Gast_vorname_txt.delete(0, 'end')

    def __Print(self):
        resultLabel = Label(self.__window, text=str(self.__controler.print_guests()), bg="lightsteelblue",
                            font=('arial', 9, 'bold'), relief=RIDGE)
        resultLabel.grid(row=8, column=1)

    def __QuitWindow(self):
        self.__controler.save()
        ays_window = Toplevel(self.__window)
        self.new = AreYouSure(ays_window)

        yesbtn = Button(ays_window, text='YES', command=self.__window.destroy, bg='green')
        yesbtn.grid(column=0, row=1)
        nobtn = Button(ays_window, text='NO', command=ays_window.destroy, bg='red')
        nobtn.grid(column=1, row=1)

    def __SaveData(self):
        self.__controler.save()

    def __LoadData(self):
        self.__controler.load()


class MenuZimmer:
    def __init__(self, gui_master, control):
        self.__window = gui_master
        self.__controler = control
        gui_master.configure(background='Cadet Blue')

        self.__Zimmer_nummer_txt = Entry(self.__window, width=20, bg="lightsteelblue")
        self.__Zimmer_amg_txt = Entry(self.__window, width=20, bg="lightsteelblue")
        self.__Zimmer_preis_txt = Entry(self.__window, width=20, bg="lightsteelblue")
        self.__Zimmer_farbe_txt = Entry(self.__window, width=20, bg="lightsteelblue")
        self.__Zimmer_meerblick_txt = Entry(self.__window, width=20, bg="lightsteelblue")
        self.__Zimmer_preisneu_txt = Entry(self.__window, width=20, bg="lightsteelblue")
        self.__Price_Option_txt = Entry(self.__window, width=20, bg="lightsteelblue")

        # butoane pt add_room
        btnr = Button(self.__window, text='Add room', command=self.__createRoom, bg="lightsteelblue")
        btnr.grid(column=0, row=0)
        nummer = Label(self.__window, text='Number', bg="lightsteelblue", font=('arial', 9, 'bold'), relief=RIDGE)
        nummer.grid(column=2, row=1)
        self.__Zimmer_nummer_txt.grid(column=3, row=1)
        amg = Label(self.__window, text='Capacity', bg="lightsteelblue", font=('arial', 9, 'bold'), relief=RIDGE)
        amg.grid(column=2, row=2)
        self.__Zimmer_amg_txt.grid(column=3, row=2)
        preis = Label(self.__window, text='Price', bg="lightsteelblue", font=('arial', 9, 'bold'), relief=RIDGE)
        preis.grid(column=2, row=3)
        self.__Zimmer_preis_txt.grid(column=3, row=3)
        farbe = Label(self.__window, text='Color', bg="lightsteelblue", font=('arial', 9, 'bold'), relief=RIDGE)
        farbe.grid(column=2, row=4)
        self.__Zimmer_farbe_txt.grid(column=3, row=4)
        meerblick = Label(self.__window, text='Seaview [yes/no]', bg="lightsteelblue", font=('arial', 9, 'bold'),
                          relief=RIDGE)
        meerblick.grid(column=2, row=5)
        self.__Zimmer_meerblick_txt.grid(column=3, row=5)

        # butoane pt change_preis
        btnr2 = Button(self.__window, text='Change price of a room', command=self.__changeprice, bg="lightsteelblue")
        btnr2.grid(column=0, row=1)
        preisneu = Label(self.__window, text='New Price', bg="lightsteelblue", font=('arial', 9, 'bold'), relief=RIDGE)
        preisneu.grid(column=2, row=6)
        self.__Zimmer_preisneu_txt.grid(column=3, row=6)

        # buton pt delete_room
        btnr3 = Button(self.__window, text='Delete room', command=self.__deleteRoom, bg="lightsteelblue")
        btnr3.grid(column=0, row=2)

        # buton pt print_rooms
        btnr4 = Button(self.__window, text='Print Rooms', command=self.__Print, bg="lightsteelblue")
        btnr4.grid(column=0, row=3)

        # butoane pt filter
        btnr5 = Button(self.__window, text='Filter Rooms', command=self.__Filter, bg="lightsteelblue")
        btnr5.grid(column=0, row=4)
        c = Label(self.__window, text='Filter criteria:', bg="lightsteelblue", font=('arial', 9, 'bold'), relief=RIDGE)
        c.grid(column=2, row=7)
        self.__Price_Option_txt.grid(column=3, row=7)
        aux0 = Label(self.__window, text='''Please type in one of: ''', bg="lightsteelblue", font=('arial', 9, 'bold'),
                     relief=RIDGE)
        aux0.grid(column=2, row=9, padx=10)
        aux1 = Label(self.__window, text='''  • More expensive than x ''', bg="lightsteelblue",
                     font=('arial', 9, 'bold'), relief=RIDGE)
        aux1.grid(column=3, row=8, pady=5)
        aux2 = Label(self.__window, text='''  • Less expensive than x ''', bg="lightsteelblue",
                     font=('arial', 9, 'bold'), relief=RIDGE)
        aux2.grid(column=3, row=9, pady=5)
        aux3 = Label(self.__window, text='''  • Exactly x ''', bg="lightsteelblue", font=('arial', 9, 'bold'),
                     relief=RIDGE)
        aux3.grid(column=3, row=10, pady=5)
        aux3 = Label(self.__window, text=''' Replacing x with the desired price''', bg="lightsteelblue",
                     font=('arial', 9, 'bold'), relief=RIDGE)
        aux3.grid(column=4, row=9, padx=10)
        # buton pt quit
        aux4 = Label(self.__window, text="                            ", bg="cadet blue")
        aux4.grid(column=2, row=15)
        btnr5 = Button(self.__window, text='Quit', command=self.__QuitWindow, bg="lightsteelblue")
        btnr5.grid(column=3, row=16)

        # save/load buttons
        savebtn = Button(self.__window, text='Save data', command=self.__SaveData, bg="lightsteelblue")
        savebtn.grid(column=0, row=5)
        loadbtn = Button(self.__window, text='Load data', command=self.__LoadData, bg="lightsteelblue")
        loadbtn.grid(column=0, row=6)

    def __createRoom(self):
        room = zimmer(self.__Zimmer_nummer_txt.get(), self.__Zimmer_amg_txt.get(), self.__Zimmer_preis_txt.get(),
                      self.__Zimmer_farbe_txt.get(), bool(self.__Zimmer_meerblick_txt.get().lower() == "yes"))
        self.__controler.add_room(room)

        self.__Zimmer_nummer_txt.delete(0, 'end')
        self.__Zimmer_amg_txt.delete(0, 'end')
        self.__Zimmer_preis_txt.delete(0, 'end')
        self.__Zimmer_farbe_txt.delete(0, 'end')
        self.__Zimmer_meerblick_txt.delete(0, 'end')

    def __changeprice(self):
        self.__controler.change_price(self.__Zimmer_nummer_txt.get(), self.__Zimmer_preisneu_txt.get())

        self.__Zimmer_nummer_txt.delete(0, 'end')
        self.__Zimmer_preisneu_txt.delete(0, 'end')

    def __deleteRoom(self):
        room = zimmer(self.__Zimmer_nummer_txt.get(), self.__Zimmer_amg_txt.get(), self.__Zimmer_preis_txt.get(),
                      self.__Zimmer_farbe_txt.get(), self.__Zimmer_meerblick_txt.get())
        self.__controler.delete_room(room.nummer)

        self.__Zimmer_nummer_txt.delete(0, 'end')

    def __Print(self):
        resultLabel = Label(self.__window, text=str(self.__controler.print_rooms()), bg="lightsteelblue",
                            font=('arial', 9, 'bold'), relief=RIDGE)
        resultLabel.grid(row=15, column=2, columnspan=3)

    def __Filter(self):
        aux = self.__Price_Option_txt.get().lower().strip()
        nr = ''
        if not aux[-1].isdigit():
            raise ValueError
        i = len(aux) - 1
        while aux[i].isdigit():
            nr = aux[-1] + nr
            aux = aux[:-1]
            i -= 1
        aux = aux.replace(" ", "")
        print(aux)
        if len(aux) == 0:
            raise ValueError
        resultLabel = Label(self.__window, text=str(
            self.__controler.filter_room(nr, bool(self.__Zimmer_meerblick_txt.get().lower() == "yes"), (
                lambda: ["moreexpensivethan", "lessexpensivethan", "exactly"].index(aux) + 1 if aux in [
                    "moreexpensivethan", "lessexpensivethan", "exactly"] else 4)())), bg="lightsteelblue",
                            font=('arial', 9, 'bold'), relief=RIDGE)
        resultLabel.grid(row=17, column=3)

        self.__Zimmer_preis_txt.delete(0, 'end')
        self.__Zimmer_meerblick_txt.delete(0, 'end')
        self.__Price_Option_txt.delete(0, 'end')

    def __QuitWindow(self):
        self.__controler.save()
        ays_window = Toplevel(self.__window)
        self.new = AreYouSure(ays_window)

        yesbtn = Button(ays_window, text='YES', command=self.__window.destroy, bg='green')
        yesbtn.grid(column=0, row=1)
        nobtn = Button(ays_window, text='NO', command=ays_window.destroy, bg='red')
        nobtn.grid(column=1, row=1)

    def __SaveData(self):
        self.__controler.save()

    def __LoadData(self):
        self.__controler.load()


class MenuReservierung:
    def __init__(self, gui_master, control):
        self.__window = gui_master
        self.__controler = control
        gui_master.configure(background='Cadet Blue')

        self.__Reserv_Vorname_txt = Entry(self.__window, width=20)
        self.__Reserv_Nachname_txt = Entry(self.__window, width=20)
        self.__Reserv_zimmerNummer_txt = Entry(self.__window, width=20)
        self.__Reserv_anfang_data_txt = Entry(self.__window, width=20)
        self.__Reserv_ende_data_txt = Entry(self.__window, width=20)

        # butoane pt make_reservation
        btnR = Button(self.__window, text='Make Reservation', command=self.__makeReservation, bg="lightsteelblue")
        btnR.grid(column=0, row=0)
        vorname = Label(self.__window, text='First Name', bg="lightsteelblue", font=('arial', 9, 'bold'), relief=RIDGE)
        vorname.grid(column=1, row=2)
        self.__Reserv_Vorname_txt.grid(column=2, row=2)
        nachname = Label(self.__window, text='Last Name', bg="lightsteelblue", font=('arial', 9, 'bold'), relief=RIDGE)
        nachname.grid(column=1, row=3)
        self.__Reserv_Nachname_txt.grid(column=2, row=3)
        zimmerNummer = Label(self.__window, text='Room Number', bg="lightsteelblue", font=('arial', 9, 'bold'),
                             relief=RIDGE)
        zimmerNummer.grid(column=1, row=4)
        self.__Reserv_zimmerNummer_txt.grid(column=2, row=4)
        anfang = Label(self.__window, text='First Day (dd/mm/yy)', bg="lightsteelblue", font=('arial', 9, 'bold'),
                       relief=RIDGE)
        anfang.grid(column=1, row=5)
        self.__Reserv_anfang_data_txt.grid(column=2, row=5)
        ende = Label(self.__window, text='Last Day (dd/mm/yy)', bg="lightsteelblue", font=('arial', 9, 'bold'),
                     relief=RIDGE)
        ende.grid(column=1, row=6)
        self.__Reserv_ende_data_txt.grid(column=2, row=6)

        # butoane pentru no_reserv_guest
        btnR2 = Button(self.__window, text='Print Guests without Reservation', command=self.__PrintNoReserv,
                       bg="lightsteelblue")
        btnR2.grid(column=1, row=0)

        # buton pentru available_today
        btnR3 = Button(self.__window, text='Show rooms available today', command=self.__AvToday, bg="lightsteelblue")
        btnR3.grid(column=2, row=0)

        # buton pentru calcel
        btnR4 = Button(self.__window, text='Cancel Reservation', command=self.__Cancel, bg="lightsteelblue")
        btnR4.grid(column=3, row=0)

        # buton pt quit
        btnR5 = Button(self.__window, text='Quit', command=self.__QuitWindow, bg="lightsteelblue")
        btnR5.grid(column=3, row=9)

        # save/load buttons
        savebtn = Button(self.__window, text='Save data', command=self.__SaveData, bg="lightsteelblue")
        savebtn.grid(column=1, row=8)
        loadbtn = Button(self.__window, text='Load data', command=self.__LoadData, bg="lightsteelblue")
        loadbtn.grid(column=2, row=8)

    def __makeReservation(self):
        start = self.__controler.transform(self.__Reserv_anfang_data_txt.get())
        end = self.__controler.transform(self.__Reserv_ende_data_txt.get())
        rezerv = reservierung(self.__Reserv_zimmerNummer_txt.get(), start, end)
        txt = self.__controler.make_reservation(rezerv,
                                                gast(self.__Reserv_Vorname_txt.get(), self.__Reserv_Nachname_txt.get()))
        resultLabel20 = Label(self.__window, text=txt, font=('arial', 9, 'bold'), relief=RIDGE, bg="lightsteelblue")
        resultLabel20.grid(row=10, column=1)
        self.__Reserv_Vorname_txt.delete(0, 'end')
        self.__Reserv_Nachname_txt.delete(0, 'end')
        self.__Reserv_zimmerNummer_txt.delete(0, 'end')
        self.__Reserv_anfang_data_txt.delete(0, 'end')
        self.__Reserv_ende_data_txt.delete(0, 'end')

    def __PrintNoReserv(self):
        resultLabel2 = Label(self.__window, text=str(self.__controler.no_reserv_guest()), font=('arial', 9, 'bold'),
                             relief=RIDGE, bg="lightsteelblue")
        resultLabel2.grid(row=11, column=1)

    def __AvToday(self):
        resultLabel3 = Label(self.__window, text=str(self.__controler.available_today()), bg="lightsteelblue",
                             font=('arial', 9, 'bold'), relief=RIDGE)
        resultLabel3.grid(row=12, column=1)

    def __Cancel(self):
        aux = gast(self.__Reserv_Vorname_txt.get(), self.__Reserv_Nachname_txt.get())
        if aux in self.__controler.repo.listg:
            indx = self.__controler.repo.listg.index(aux)
            deprintat = self.__controler.print_reserv(indx)
            if deprintat == '':
                resultLabel4 = Label(self.__window, text='No reservations', bg="lightsteelblue",
                                     font=('arial', 9, 'bold'), relief=RIDGE)
                resultLabel4.grid(row=13, column=1)
            else:
                resultLabel4 = Label(self.__window, text=deprintat, bg="lightsteelblue", font=('arial', 9, 'bold'),
                                     relief=RIDGE)
                resultLabel4.grid(row=13, column=1, columnspan=3)
                # 7 e gol
                opt = Label(self.__window, text='Nr of reservation to cancel', bg="lightsteelblue",
                            font=('arial', 9, 'bold'), relief=RIDGE)
                opt.grid(column=1, row=7)
                option = Entry(self.__window, width=20)
                option.grid(column=2, row=7)
                # de fct buton
                btnR6 = Button(self.__window, text='Cancel', bg="lightsteelblue")
                btnR6.grid(column=3, row=7)
                btnR6.configure(command=lambda: self.__cancel_aux(indx, option, opt, btnR6))
                # command=self.__cancel_aux(indx)
        else:
            resultLabel4 = Label(self.__window, text='No such guest. Try again!', bg="lightsteelblue",
                                 font=('arial', 9, 'bold'), relief=RIDGE)
            resultLabel4.grid(row=12, column=1)
        self.__Reserv_Vorname_txt.delete(0, 'end')
        self.__Reserv_Nachname_txt.delete(0, 'end')

    def __cancel_aux(self, indx, option, opt, btn):
        try:
            nr_ord = int(option.get()) - 1
            if nr_ord < len(self.__controler.repo.listg[indx].reserv):
                self.__controler.repo.listg[indx].reserv.pop(nr_ord)
            else:
                raise ValueError
            option.destroy()
            opt.destroy()
            btn.destroy()
        except:
            pass

    def __QuitWindow(self):
        self.__controler.save()
        ays_window = Toplevel(self.__window)
        self.new = AreYouSure(ays_window)

        yesbtn = Button(ays_window, text='YES', command=self.__window.destroy, bg='green')
        yesbtn.grid(column=0, row=1)
        nobtn = Button(ays_window, text='NO', command=ays_window.destroy, bg='red')
        nobtn.grid(column=1, row=1)

    def __SaveData(self):
        self.__controler.save()

    def __LoadData(self):
        self.__controler.load()


'''
class Test():
    def __init__(self,root):
        self.root = root
        self.text = StringVar()
        self.text.set(control.add_guest)
        self.label = Label(self.root, textvariable=self.text)

        self.button = Button(self.root, text="Click to change text below", command=self.changeText)
        self.button.pack()
        self.label.pack()
        self.root.mainloop()

    def changeText(self):
        self.text.set("Text updated")
'''


class MenuHELP:
    def __init__(self, gui_master, control):
        self.__window = gui_master
        self.__controler = control
        gui_master.configure(background='Cadet Blue')

        about = Button(self.__window, text="About Hotel Arcasu'&CO", command=self.new_windowA, bg="lightsteelblue")
        about.pack()

        HTUG = Button(self.__window, text="How to use Guest Menu?", command=self.new_windowHTUG, bg="lightsteelblue")
        HTUG.pack()

        HTUZ = Button(self.__window, text="How to use Room Menu?", command=self.new_windowHTUZ, bg="lightsteelblue")
        HTUZ.pack()

        HTUR = Button(self.__window, text="How to use Reservation Menu?", command=self.new_windowHTUR,
                      bg="lightsteelblue")
        HTUR.pack()

        quitbutton = Button(self.__window, text="Quit", command=self.__Destroy, bg="lightsteelblue")
        quitbutton.pack()

    def __Destroy(self):
        self.__window.destroy()

    def new_windowA(self):
        about_window = Toplevel(self.__window)
        about_window.title("About")
        about_window.geometry('1000x750')
        about_window.config(bg="cadet blue")
        outputLabel = Label(about_window, text="About Hotel Arcasu'&CO :", relief=RIDGE, bg="lightsteelblue")
        outputLabel.place(x=450, y=50)
        label = Label(about_window, text="🏙 Built in 2001 🏢", relief=RIDGE, bg="lightsteelblue")
        label.place(x=475, y=100)
        lab = Label(about_window, text="7 stars with ultra all-inclusive", relief=RIDGE, bg="lightsteelblue")
        lab.place(x=440, y=150)
        lab1 = Label(about_window, text="25 Single rooms, 20 Duet rooms and 15 penthouses with seaview", relief=RIDGE,
                     bg="lightsteelblue")
        lab1.place(x=350, y=200)
        lab2 = Label(about_window, text="Pool parties on the rooftop of the hotel", relief=RIDGE, bg="lightsteelblue")
        lab2.place(x=420, y=250)
        lab3 = Label(about_window, text="About our hotel software :", relief=RIDGE, bg="lightsteelblue")
        lab3.place(x=450, y=450)
        lab4 = Label(about_window, text="Name : Arcasu's software", relief=RIDGE, bg="lightsteelblue")
        lab4.place(x=453, y=500)
        lab5 = Label(about_window, text="Version 2021.1", relief=RIDGE, bg="lightsteelblue")
        lab5.place(x=485, y=550)
        lab6 = Label(about_window, text="Copyright © 2016-2020 Arcasu' S.R.L", relief=RIDGE, bg="lightsteelblue")
        lab6.place(x=425, y=600)

    def new_windowHTUG(self):
        HTUG_window = Toplevel(self.__window)
        HTUG_window.title("How to use Guest Menu?")
        HTUG_window.geometry('1100x450')
        HTUG_window.config(bg="cadet blue")
        oL1 = Label(HTUG_window,
                    text=" In order to use the Guest Menu you have to know a few things about how it is organized and the meaning of each button",
                    relief=RIDGE, bg="lightsteelblue")
        oL1.place(x=100, y=100)
        oL2 = Label(HTUG_window, text="1. 'Add Guest' Button:", relief=RIDGE, bg="lightsteelblue")
        oL2.place(x=100, y=140)
        oL3 = Label(HTUG_window,
                    text="By pressing this button you will start the process of adding a guest in the database of the hotel. But what you must now is that you have to fill the First Name and Last Name gaps firstly",
                    relief=RIDGE, bg="lightsteelblue")
        oL3.place(x=120, y=160)
        oL4 = Label(HTUG_window, text="2. 'Update the lastname' Button:", relief=RIDGE, bg="lightsteelblue")
        oL4.place(x=100, y=180)
        oL5 = Label(HTUG_window,
                    text="In order to change the last name of a guest you will have to reintroduce his first and last name and also to fill in the specified area the new family name of the guest",
                    relief=RIDGE, bg="lightsteelblue")
        oL5.place(x=120, y=200)
        oL6 = Label(HTUG_window,
                    text="3. 'Delete Guest' Button:", relief=RIDGE, bg="lightsteelblue")
        oL6.place(x=100, y=220)
        oL7 = Label(HTUG_window,
                    text="In order to delete a guest from the database you will only have to enter again his first and last name in the specified areas and then press the button",
                    relief=RIDGE, bg="lightsteelblue")
        oL7.place(x=120, y=240)
        oL8 = Label(HTUG_window, text="4. 'Print Guests' Button:", relief=RIDGE, bg="lightsteelblue")
        oL8.place(x=100, y=260)
        oL9 = Label(HTUG_window,
                    text="This button was created for printing the list of guests that are curently renting a room",
                    relief=RIDGE, bg="lightsteelblue")
        oL9.place(x=120, y=280)
        oL10 = Label(HTUG_window,
                     text="When you quit the menu your data are automatically saved, but for more certainty you should use the Save button",
                     relief=RIDGE, bg="lightsteelblue")
        oL10.place(x=100, y=320)

        quit = Button(HTUG_window, text='Quit', command=HTUG_window.destroy, bg="lightsteelblue")
        quit.place(x=100, y=350)

    def new_windowHTUZ(self):
        HTUZ_window = Toplevel(self.__window)
        HTUZ_window.title("How to use Room Menu?")
        HTUZ_window.geometry('1200x550')
        HTUZ_window.config(bg="cadet blue")
        oL1 = Label(HTUZ_window,
                    text=" In order to use the Room Menu you have to know a few things about how it is organized and the meaning of each button:",
                    relief=RIDGE, bg="lightsteelblue")
        oL1.place(x=100, y=100)
        oL2 = Label(HTUZ_window, text="1. Add Room Button:", relief=RIDGE, bg="lightsteelblue")
        oL2.place(x=100, y=140)
        oL3 = Label(HTUZ_window,
                    text="By pressing this button you will start the process of adding a room in the database of the hotel. But what you must now is that you have to fill the Number, Capacity, Price, Colour and Seaview gaps firstly",
                    relief=RIDGE, bg="lightsteelblue")
        oL3.place(x=120, y=160)
        oL4 = Label(HTUZ_window, text="Capacity refers to the 'number of people that can stay in that room'.",
                    relief=RIDGE, bg="lightsteelblue")
        oL4.place(x=120, y=180)
        oL5 = Label(HTUZ_window, text="2. Change price:", relief=RIDGE, bg="lightsteelblue")
        oL5.place(x=100, y=200)
        oL6 = Label(HTUZ_window,
                    text="By pressing this button you will start the process of changing the price of a room that already is in the database of the hotel.",
                    relief=RIDGE, bg="lightsteelblue")
        oL6.place(x=120, y=220)
        oL7 = Label(HTUZ_window,
                    text="In order to do so you have to introduce the number of the room and the new price in the specified gaps firstly ",
                    relief=RIDGE, bg="lightsteelblue")
        oL7.place(x=120, y=240)
        oL8 = Label(HTUZ_window, text="3. Delete room:", relief=RIDGE, bg="lightsteelblue")
        oL8.place(x=100, y=260)
        oL9 = Label(HTUZ_window,
                    text="In order to delete a room from the database you will only have to enter the number of the room in the specified area ",
                    relief=RIDGE, bg="lightsteelblue")
        oL9.place(x=120, y=280)
        oL10 = Label(HTUZ_window, text="4. Print rooms:", relief=RIDGE, bg="lightsteelblue")
        oL10.place(x=100, y=300)
        oL11 = Label(HTUZ_window,
                     text="This button was created for printing the list of rooms that are available for renting or that are already rented",
                     relief=RIDGE, bg="lightsteelblue")
        oL11.place(x=120, y=320)
        oL12 = Label(HTUZ_window, text="5. Filter: ", relief=RIDGE, bg="lightsteelblue")
        oL12.place(x=100, y=340)
        oL13 = Label(HTUZ_window,
                     text="In order to filter the list of rooms depending on multiple options you will have to introduce exactly what you are looking for.",
                     relief=RIDGE, bg="lightsteelblue")
        oL13.place(x=120, y=360)
        oL14 = Label(HTUZ_window,
                     text="More exactly you will have to introduce a price in the specified gap, the price option which is specified in the menu, and if the room has or not a seaview.",
                     relief=RIDGE, bg="lightsteelblue")
        oL14.place(x=120, y=380)
        oL15 = Label(HTUZ_window,
                     text="When you quit the menu your data are automatically saved, but for more certainty you should use the Save button",
                     relief=RIDGE, bg="lightsteelblue")
        oL15.place(x=100, y=420)

        quit = Button(HTUZ_window, text='Quit', command=HTUZ_window.destroy, bg="lightsteelblue")
        quit.place(x=100, y=470)

    def new_windowHTUR(self):
        HTUR_window = Toplevel(self.__window)
        HTUR_window.title("How to use Reservation Menu?")
        HTUR_window.geometry('1100x450')
        HTUR_window.config(bg="cadet blue")

        oL1 = Label(HTUR_window,
                    text=" In order to use the Reservation Menu you have to know a few things about how it is organized and the meaning of each button:",
                    relief=RIDGE, bg="lightsteelblue")
        oL1.place(x=100, y=100)
        oL2 = Label(HTUR_window, text="1. 'Make Reservation' Button:", relief=RIDGE, bg="lightsteelblue")
        oL2.place(x=100, y=140)
        oL3 = Label(HTUR_window,
                    text="By pressing this button you will start the process of making a reservation in the database of the hotel.",
                    relief=RIDGE, bg="lightsteelblue")
        oL3.place(x=120, y=160)
        oL4 = Label(HTUR_window,
                    text=" But what you must now is that you have to fill First Name, Last Name, Room Number, First Day and Last Day gaps firstly",
                    relief=RIDGE, bg="lightsteelblue")
        oL4.place(x=120, y=180)
        oL5 = Label(HTUR_window, text="2. 'Print Guests without Reservation ' Button:", relief=RIDGE,
                    bg="lightsteelblue")
        oL5.place(x=100, y=200)
        oL6 = Label(HTUR_window,
                    text="This button was created for printing the list of guests that have no reservation in the database of the hotel, but they are interested in renting a room.",
                    relief=RIDGE, bg="lightsteelblue")
        oL6.place(x=120, y=220)
        oL7 = Label(HTUR_window,
                    text="3. 'Show rooms available today' Button: ",
                    relief=RIDGE, bg="lightsteelblue")
        oL7.place(x=100, y=240)
        oL8 = Label(HTUR_window,
                    text="This button was created for printing the list of rooms that are available for renting today",
                    relief=RIDGE, bg="lightsteelblue")
        oL8.place(x=120, y=260)
        oL9 = Label(HTUR_window, text="4. 'Cancel Reservation' Button:", relief=RIDGE, bg="lightsteelblue")
        oL9.place(x=100, y=280)
        oL10 = Label(HTUR_window,
                     text="In order to cancel a reservation you will have to introduce the Room Number, and the dates of the First and Last Day in the specified area",
                     relief=RIDGE, bg="lightsteelblue")
        oL10.place(x=120, y=300)
        oL11 = Label(HTUR_window,
                     text="When you quit the menu your data are automatically saved, but for more certainty you should use the Save button",
                     relief=RIDGE, bg="lightsteelblue")
        oL11.place(x=100, y=350)

        quit = Button(HTUR_window, text='Quit', command=HTUR_window.destroy, bg="lightsteelblue")
        quit.place(x=100, y=400)


class AreYouSure():
    def __init__(self, gui_master):
        self.__window = gui_master

        label = Label(self.__window, text='Are you sure you want to quit this window?')
        label.grid(column=0, row=0)

    def __QuitBothWindows(self):
        self.__window.destroy()

    def __QuitWindow(self):
        self.__window.destroy()
