import random

n = int(input("Input Number:"))
ranSum = []
evenSum = []
def random1():
    for i in range(n):
        ranSum.append(random.randint(2000, 3000))
    print(ranSum)
def sumevenran():
    for j in ranSum:
        if j % 2 == 0:
            evenSum.append(j)
    print(sum(evenSum))

random1()
sumevenran()