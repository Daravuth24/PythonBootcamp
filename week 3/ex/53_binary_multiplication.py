def binary_multiplication(x, y):

    binnumx = bin(x).replace("0b", "")

    binnumy = bin(y).replace("0b", "")

    multibin = bin(x * y).replace("0b", "")

    multidec = x * y

    print(f"binary_addtion({x},{y})")

    print("Num 1 :", binnumx)

    print("Num 2 :", binnumy)

    print("Sum (Binary) :", multibin)

    print("Sum (Decimal) :", multidec)


binary_multiplication(60, 50)
