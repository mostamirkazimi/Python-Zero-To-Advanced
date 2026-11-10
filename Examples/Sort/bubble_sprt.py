from random import randint as rnd
import matplotlib.pyplot as plt

lenght = 10
list = [rnd(0, lenght) for i in range(lenght)]

for i in range(lenght-1):
    for j in range(0, lenght - i - 1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
    plt.bar(range(lenght), list)
    plt.pause(0.5)
    plt.clf()

plt.bar(range(lenght), list)
plt.show()
print(list)