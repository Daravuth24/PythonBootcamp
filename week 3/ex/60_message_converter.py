def message_converter(mes):
    secret = []
    if mes == "":
        print("The string is empty.")
    else:
        for i in mes:
            ascii = ord(i)
            decnum = int(ascii)
            secret = hex(decnum).upper().replace("0X", "")
            print(secret, end="")
message_converter("Hello")