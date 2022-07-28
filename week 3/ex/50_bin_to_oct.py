def bin_to_oct(x):

    try:

        binnum = x

        decnum = int(binnum, 2)

        octnum = oct(decnum).replace("0o", "")

        print(f"bin_to_oct({x})")

        return print(octnum)

    except ValueError:

        print("This is not a binary number")


bin_to_oct('11001101')
