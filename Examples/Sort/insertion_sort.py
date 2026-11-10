from random import shuffle
import matplotlib.pyplot as plt
length = 10
list = [i for i in range(length)]
shuffle(list)
list1 = []
for i in list:
    for j in range(len(list1)):
        if i < list1[j]:
            list1.insert(j, i)
            break
    else:
        list1.append(i)
    plt.bar(range(len(list1)), list1)
    plt.pause(0.5)
    plt.clf()
plt.bar(range(len(list1)), list1)
plt.show()

print(list1)
