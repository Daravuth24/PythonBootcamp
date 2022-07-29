def binary_addition(x, y):

    binnumx = bin(x).replace("0b", "")

    binnumy = bin(y).replace("0b", "")

    sumbin = bin(x + y).replace("0b", "")

    sumdec = x + y

    print(f"binary_addtion({x},{y})")

    print("Num 1 :", binnumx)

    print("Num 2 :", binnumy)

    print("Sum (Binary) :", sumbin)

    print("Sum (Decimal) :", sumdec)


binary_addition(60, 50)
