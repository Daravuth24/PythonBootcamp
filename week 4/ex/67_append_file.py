import datetime


def append_file(filename):

    fappend = open(filename, "a")
    choice = ""
    x = datetime.datetime.now()
    y = x.strftime("%d/%m/%y %H:%M:%S")

    while choice != "EXIT":
        choice = input(f"$: ")

        if choice != "EXIT":
            fappend.write(f"[{y}] {choice} ")

        else:
            return 0


append_file("appendtext")
