def and_operation(x, y):

    try:

        print(f"and_operation({x, y})")

        hexnum1 = x

        hexnum2 = y

        decnum1 = int(hexnum1, 16)

        decnum2 = int(hexnum2, 16)

        binnum1 = bin(decnum1).replace("0b", "")

        binnum2 = bin(decnum2).replace("0b", "")

        return print(f"{decnum1} \n{decnum2} \n\n{bin(51 & 61)}")

    except ValueError:

        print("This is not a hexa-decimal number")


and_operation("33", "3D")
