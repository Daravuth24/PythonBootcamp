def bin_to_hex(x):

    try:

        binnum = x

        decnum = int(binnum, 2)

        hexnum = hex(decnum).replace("0x", "")

        print(f"bin_to_hex({x})")

        return print(hexnum)

    except ValueError:

        print("This is not a binary number")


bin_to_hex('11001101')
