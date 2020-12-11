from entity.gast import gast
from entity.reservierung import reservierung
from entity.data import data
from entity.zimmer import zimmer
from manage.repository import repo
from manage.controler import controler

ui = """
        1- Load data
        2- Save data

        3- Add guest
        4- Change surname of guest
        5- Delete guest
        6- Show list of guests

        7- Add room
        8- Change price of room
        9- Delete room
        10- Show list of rooms

        11- Make a reservation
        12- Show guests with no reservation
        13- Filter rooms
        14- Show the rooms available today
        15- Cancel reservation

        16- Exit
"""
control = controler(repo())


def test_string(aux):
    for i in range(0, len(aux)):
        if not (aux[i].isalpha() or aux[i] == '-'):
            raise Exception("invalid string")
    return None


def test_room(nr):

    for i in control.repo.listz:
        if i.nummer == nr:
            return None
    raise Exception("invalid room")


def convert_date(s):
    if not (s[2] == '/' and s[5] == '/'):
        raise Exception("invalid date")
    if not (s[:2].isdigit() and s[3:5].isdigit() and s[6:].isdigit()):
        raise Exception("invalid date")
    Monat = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = int(s[:2])
    m = int(s[3:5])
    y = int(s[6:])
    if y % 4 == 0 and y % 100 != 0:
        Monat[1] = 29
    if y % 400 == 0:
        Monat[1] = 29
    if d > Monat[m - 1]:
        raise Exception("invalid date")
    return data(d, m, y)


def main():
    while True:
        control.today_valid()
        print(ui)
        opt = input('option-')
        if opt == "1":
            control.load()
        elif opt == "2":
            control.save()
        elif opt == "3":
            name = input('surname:')
            test_string(name)
            vorname = input('name: ')
            test_string(vorname)
            control.add_guest(gast(vorname, name))
        elif opt == "4":
            name = input('surname: ')
            test_string(name)
            vorname = input('name: ')
            test_string(vorname)
            nachname = input('neu surname: ')
            test_string(nachname)
            control.update_guest(gast(vorname, name), nachname)
            print('Done👌')
        elif opt == "5":
            name = input('surname: ')
            test_string(name)
            vorname = input('name: ')
            test_string(vorname)
            control.delete_guest(gast(vorname, name))
        elif opt == "6":
            print("The guests are: ")
            print(control.print_guest())
        elif opt == "7":
            nr = int(input("New room's number: "))
            pers = int(input("Capacity: "))
            preis = int(input("Price/night: "))
            farbe = input("The color of room's walls: ")
            test_string(farbe)
            meerblick = input("Does it have seaview?[yes / no] ")
            test_string(meerblick)
            meerblick = bool(meerblick == "ja")
            aux = zimmer(nr, pers, preis, farbe, meerblick)
            control.add_room(aux)
        elif opt == "8":
            nr = int(input("Number of room you'd wish the change the price to: "))
            preis = int(input("New Price: "))
            control.change_price(nr, preis)
        elif opt == "9":
            nr = int(input("Number of room you'd wish to delete: "))
            control.delete_room(nr)
        elif opt == "10":
            print(control.print_rooms())
        elif opt == "11":
            name = input('surname:')
            test_string(name)
            vorname = input('name: ')
            test_string(vorname)
            nr = int(input("Which room would you like to rent? "))
            test_room(nr)
            start = input("von [dd/mm/yyyy]: ")
            start = convert_date(start)
            end = input("bis [dd/mm/yyyy]: ")
            end = convert_date(end)
            control.make_reservation(gast(vorname, name), reservierung(nr, start, end))
        elif opt == "12":
            control.no_reserv_guest()
        elif opt == "13":
            p = input("Price per night: [more expensive than x / cheaper than x / exactly x] ")
            m = input("Do you want seaview? [yes / no] ")
            m = bool(m == "ja")
            c = 0
            aux = len(p) - 1
            while aux >= 0:
                if not (p[aux].isnumeric()):
                    break
                aux -= 1
            preis = int(p[aux + 1:])
            if "more expensive" in p:
                c = 1
            elif "cheaper" in p:
                c = 2
            elif "exactly" in p:
                c = 3
            else:
                print("Invalid syntax")
            print("Your options are the rooms",end=" ")
            print(control.filter_room(preis, m, c))
        elif opt == "14":
            aux = control.available_today()
            print("The rooms available today are:")
            for i in aux:
                print(i)
        elif opt == "15":
            name = input('surname:')
            test_string(name)
            vorname = input('name: ')
            test_string(vorname)
            aux = gast(vorname, name)
            if aux not in control.repo.listg:
                print("No such guest")
                continue
            for i in range(0, len(control.repo.listg)):
                if control.repo.listg[i] == aux:
                    print("You have the following reservations: ")
                    nr = 1
                    for j in control.repo.listg[i].reserv:
                        print(str(nr) + ". " + str(j))
                        nr += 1
                    pick = input(f"Which one would you like to delete[1-{nr - 1}]")
                    if not pick.isdigit():
                        print("Invalid input")
                        continue
                    else:
                        pick = int(pick)-1
                        if pick < len(control.repo.listg[i].reserv):
                            control.cancel(aux, pick)
                        else:
                            print("Invalid input")
            print("Done")
        elif opt == "16":
            print('Exiting')
            break
        else:
            print("Invalid option\nPick a number from [1,16]")

        print("\n\n")

    control.print_guest()


main()
