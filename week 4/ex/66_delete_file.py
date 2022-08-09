import os


def delete_file(filename):

    fpath = os.path.dirname(os.path.realpath(__file__))

    while len(filename) > 0:

        choice = input(f"Are you sure you want to delete {filename}? [Y/N]")

        if choice.upper() == "Y":

            if os.path.isdir(f"{fpath}\{filename}"):
                os.rmdir(f"{fpath}\{filename}")
                return 1

            if os.path.isfile(f"{fpath}\{filename}"):
                os.remove(f"{fpath}\{filename}")
                return 1

        elif choice.upper() == "N":
            return 0

        else:
            print("Invalid Option")

    else:
        return 0


delete_file("folder1")

