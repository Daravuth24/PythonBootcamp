def oct_to_dec(x):

    try:

        print(f"oct_to_dec({x})")

        return print(int(x, 8))

    except ValueError:

        print("This is not octal number")


oct_to_dec('750')
