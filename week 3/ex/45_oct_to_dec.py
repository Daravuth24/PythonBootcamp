def oct_to_dec(x):

    try:

        return print(int(x, 8))

    except ValueError:
        print("This is not octal number")


print("oct_to_dec(750)")

oct_to_dec('750')
