def hex_to_oct(x):

    try:

        hexnum = x

        decnum = int(hexnum, 16)

        octnum = oct(decnum).replace("0o", "")

        print(f"hex_to_oct({x})")

        return print(octnum)

    except ValueError:

        print("This is not a hexa-decimal number")


hex_to_oct('2b9')
