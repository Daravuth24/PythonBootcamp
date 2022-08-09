import os

def current_path():

    fpath = os.getcwd()
    fpathstring = "".join(fpath)
    print(f"Current path of program folder:\n{fpathstring}")


current_path()
