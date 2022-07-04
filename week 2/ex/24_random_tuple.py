import random
list = []
def random_tuple(num):
    for i in range(num):
        list.append(random.randint(0, 100))
        rannum = tuple(list)
        print(f"Random number {i+1}: {rannum[i]}")
    print(f"\n{rannum}\n")
    return print(sum(rannum))
random_tuple(5)
