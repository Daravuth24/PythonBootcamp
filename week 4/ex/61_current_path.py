import os

def current_path():

    fpath = os.path.dirname(os.path.realpath(__file__))
    fpathstring = "".join(fpath)
    print(f"Current path of program folder:\n{fpathstring}")


current_path()
