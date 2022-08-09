import os


def current_folder():

    fpath = os.path.dirname(os.path.realpath(__file__))
    currentdir = os.listdir(fpath)

    for i in currentdir:
        checkfile = os.path.isfile(i)

        if checkfile:
            check1 = "File"

        else:
            check1 = "Folder"

        print(f"[{i, check1}]", end="")


current_folder()
