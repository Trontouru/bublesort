from random import randint


def BubbleSort(array):
    for i in reversed(range(len(a) + 1)):
        flag = True
        for j in range(i - 1):
            if a[j] < a[j + 1]:
                tmp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = tmp
                flag = False

        if flag:
            break
    return a


n = int(input())
a = list(map(int, input().split()))
BubbleSort(a)
print(*a)
