import os

def current_path():

    fpath = os.path.dirname(os.path.realpath(__file__))
    a = os.path.isfile(fpath)
    b = os.path.isdir(fpath)
    print(f"Current path of program folder:\n{fpath, a, b}")

current_path()
