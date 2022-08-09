import os

def auto_folder(foldernames):

    fpath = os.path.dirname(os.path.realpath(__file__))

    if len(foldernames) > 0:

        for folders in range(len(foldernames)):

            if os.path.exists(f"{fpath}\{foldernames[folders]}"):

                while True:
                    choice = input(f"Are you sure you want to replace {foldernames[folders]}?[Y/N]")

                    if choice.upper() == "Y":
                        freplace = os.replace(f"{fpath}\{foldernames[folders]}", f"{fpath}\{foldernames[folders]}")
                        break

                    elif choice.upper() == "N":
                        break

                    else:
                        print("Invalid option")

            else:
                fcreate = os.makedirs(f"{fpath}\{foldernames[folders]}")

        return 1

    else:
        return 0

auto_folder(["folder1", "folder2", "folder3", "folder4"])
