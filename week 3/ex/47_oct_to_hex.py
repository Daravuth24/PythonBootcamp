def oct_to_hex(x):

    octnum = x

    decnum = int(octnum, 8)

    hexnum = hex(decnum).upper().replace("0X", "")

    return print(hexnum)


print("oct_to_hex(1271)")

oct_to_hex('1271')
