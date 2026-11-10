from random import shuffle
import matplotlib.pyplot as plt

length = 10
arr = [i for i in range(length)]
shuffle(arr)

plt.ion()


def draw(arr, pivot=None):
    plt.clf()

    colors = ["skyblue"] * len(arr)

    if pivot is not None:
        colors[pivot] = "red"

    plt.bar(range(len(arr)), arr, color=colors)
    plt.title("Quick Sort")
    plt.pause(0.5)


def quick_sort(arr, low, high):
    if low < high:

        pivot = low
        i = low
        j = high

        draw(arr, pivot)

        while i < j:

            while i < high and arr[i] <= arr[pivot]:
                i += 1

            while arr[j] > arr[pivot]:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
                draw(arr, pivot)

        arr[pivot], arr[j] = arr[j], arr[pivot]
        draw(arr, j)

        quick_sort(arr, low, j - 1)
        quick_sort(arr, j + 1, high)


quick_sort(arr, 0, len(arr) - 1)

plt.ioff()
plt.show()

print(arr)