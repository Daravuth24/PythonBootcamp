def binary_subtraction(x, y):

    dec1 = x
    dec2 = y

    bin1 = bin(int(x)).replace("0b", "")
    bin2 = bin(int(y)).replace("0b", "")

    maxlen = max(len(bin1), len(bin2))
    result = ''
    carry = 0

    i = maxlen - 1
    while i >= 0:

        s = int(bin1[i]) - int(bin2[i])

        if s == -1:
            if carry == 0:
                carry = 1
                result = result + "1"

        if s == 0:
            if carry == 0:
                result = result + "0"

        if s == 1:
            if carry == 1:
                result = result + "0"
                carry = 0
            else:
                result = result + "1"

        i = i - 1

    if carry > 0:
        result = result + "1"

    difbin = int(result[::-1])
    difdec = int(dec1) - int(dec2)

    print(f"binary_addtion({x},{y})")
    print("Num 1 :", bin1)
    print("Num 2 :", bin2)
    print("Difference (Binary) :", difbin)
    print("Difference (Decimal) :", difdec)


binary_subtraction('60', '50')
