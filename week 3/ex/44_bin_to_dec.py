def bin_to_dec(x):

    try:

        decnum = int(x, 2)

        print(f"bin_to_dec({x})")

        return print(decnum)

    except ValueError:

        print("This is not a binary number")


bin_to_dec('110011')
