import os

def current_folder():

    path = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(path)
    print(files)


current_folder()
