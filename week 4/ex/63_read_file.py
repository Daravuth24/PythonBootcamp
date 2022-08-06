def read_file(x):

    try:

        fileread = open(x, 'r')
        print(fileread.read())
        return fileread.read()

    except FileNotFoundError:

        print("Invalid FILENAME")
        return ""


read_file('hello_world.txt')
