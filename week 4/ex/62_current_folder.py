import os


def current_folder():

    fpath = os.path.dirname(os.path.realpath(__file__))
    currentdir = os.listdir(fpath)

    for i in currentdir:
        checkfile2 = os.path.isfile(i)

        if checkfile2:
            check1 = "File"

        else:
            check1 = "Folder"

        print(f"[{i, check1}]", end="")


current_folder()
