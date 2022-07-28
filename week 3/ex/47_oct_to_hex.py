def oct_to_hex(x):

    try:

        octnum = x

        decnum = int(octnum, 8)

        hexnum = hex(decnum).upper().replace("0X", "")

        print(f"oct_to_hex({x})")

        return print(hexnum)

    except ValueError:

        print("This is not a octal number")


oct_to_hex('1271')
