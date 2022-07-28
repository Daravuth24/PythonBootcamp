def hex_to_oct(x):

    hexnum = x

    decnum = int(hexnum, 16)

    octnum = oct(decnum).replace("0o", "")

    return print(octnum)


print("oct_to_hex(2b9)")

hex_to_oct('2b9')
