from random import randint as rnd
import matplotlib.pyplot as plt
lenght = 100
list = [rnd(0,lenght) for i in range(lenght)]
for i in range(lenght-1):
    min = i
    for j in range(i+1,lenght):
        if list[min] > list[j]:
            min = j
    list[i],list[min] =  list[min],list[i]
    plt.bar(range(lenght),list)
    plt.pause(0.5)
    plt.clf()
plt.bar(range(lenght),list)
plt.show()
print(list)