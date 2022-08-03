def message_converter(mes):

    if mes == "":
        print("The string is empty.")
    else:
        for i in mes:
            ascii = ord(i)
            decnum = int(ascii)
            hexnum = hex(decnum).replace("0x", "")
            print(hexnum)
        hexnum = hexnum.join("")
        print(hexnum)
    hexnum = "".join(hexnum)
    print(hexnum)
message_converter("Hello")