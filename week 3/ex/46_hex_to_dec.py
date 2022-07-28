def hex_to_dec(x):

    try:

        print(f"hex_to_dec({x})")

        return print(int(x, 16))

    except ValueError:

        print("This is not a hexa-decimal number")


hex_to_dec('BA1')
