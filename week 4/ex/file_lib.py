class FileLib:

    def inspect(self):

        import os
        fpath = os.getcwd()
        if os.path.isfile(fpath):
            print("The type is file.")
        elif os.path.isdir(fpath):
            print("The type is folder.")

    def current_path(self):

        import os
        fpath = os.getcwd()
        fpathstring = "".join(fpath)
        print(f"Current path of program folder:\n{fpathstring}")

    def read(self, filename):

        try:

            fileread = open(filename, 'r')
            filereadstring = "".join(fileread)
            print(f"{filereadstring}")
            fileread.close()

        except FileNotFoundError:

            print("Invalid FILENAME")
            return ""

    def write(self, filename, content):

        while True:
            choice1 = input(f"Are you sure you want to replace {filename}?[Y/N]")
            try:
                while True:

                    if choice1.upper() == "Y":
                        filecreate = open(filename, "w")
                        filecreate.write(content)
                        return 1

                    elif choice1.upper() == "N":
                        return 0

                    else:
                        print("Invalid Option")
                        break

            except FileExistsError:
                continue

    def append(self, filename, content):

        import datetime
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

    def remove(self, filename):

        import os
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

    def create_folder(self, folder_list):

        import os
        fpath = os.path.dirname(os.path.realpath(__file__))

        if len(folder_list) > 0:

            for folders in range(len(folder_list)):

                if os.path.exists(f"{fpath}\{folder_list[folders]}"):

                    while True:
                        choice = input(f"Are you sure you want to replace {folder_list[folders]}?[Y/N]")

                        if choice.upper() == "Y":
                            freplace = os.replace(f"{fpath}\{folder_list[folders]}", f"{fpath}\{folder_list[folders]}")
                            break

                        elif choice.upper() == "N":
                            break

                        else:
                            print("Invalid option")

                else:
                    fcreate = os.makedirs(f"{fpath}\{folder_list[folders]}")

            return 1

        else:
            return 0