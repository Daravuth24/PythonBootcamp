def binary_addition(x, y):

    binnum1 = bin(int(x)).replace("0b", "")
    binnum2 = bin(int(y)).replace("0b", "")

    decnum1 = str(x)
    decnum2 = str(y)

    sumbin = []
    carry = "0"

    for i in range(len(binnum1)-1, -1, -1):
        bin1 = binnum1[i]
        bin2 = binnum2[i]
        if bin1 == "0" and bin2 == "0" and carry == "0":
            sumbin.append("0")
            carry = "0"
        elif (bin1 == "0" and bin2 == "0" and carry == "1") or (bin1 == "0" and bin2 == "1" and carry == "0") or (bin1 == "1" and bin2 == "0" and carry == "0"):
            sumbin.append("1")
            carry = "0"
        elif bin1 == "1" and bin2 == "1" and carry == "0":
            sumbin.append("0")
            carry = "1"
        elif bin1 == "1" and bin2 == "1" and carry == "1":
            sumbin.append("1")
            carry = "1"
    if carry == "1":
        sumbin.append("1")

    sumbin = "".join(sumbin[::-1])
    sumdec = int(sumbin, 2)

    print(f"binary_addtion({x},{y})")

    print("Num 1 :", binnum1)

    print("Num 2 :", binnum2)

    print("Sum (Binary) :", sumbin)

    print("Sum (Decimal) :", sumdec)


binary_addition(60, 50)
