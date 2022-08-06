import os

def current_path():

    fpath = os.path.dirname(os.path.realpath(__file__))
    print(f"Current path of program folder:\n{fpath}")

current_path()
