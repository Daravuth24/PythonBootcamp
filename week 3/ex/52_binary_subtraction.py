def binary_substraction(x, y):

    binnumx = bin(x).replace("0b", "")

    binnumy = bin(y).replace("0b", "")

    substractbin = bin(x - y).replace("0b", "")

    substractdec = x - y

    print(f"binary_addtion({x},{y})")

    print("Num 1 :", binnumx)

    print("Num 2 :", binnumy)

    print("Sum (Binary) :", substractbin)

    print("Sum (Decimal) :", substractdec)


binary_substraction(60, 50)
