def read_file(x):

    try:

        fileread = open(x, 'r')
        filereadstring = "".join(fileread)
        print(f"{filereadstring}")
        fileread.close()

    except FileNotFoundError:

        print("Invalid FILENAME")
        return ""


read_file('hello_world.txt')
