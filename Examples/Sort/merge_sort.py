from random import randint as rnd
import matplotlib.pyplot as plt

length = 10
arr = [rnd(0, length) for _ in range(length)]

plt.ion()


def draw(arr):
    plt.clf()
    plt.bar(range(len(arr)), arr)
    plt.pause(0.5)


def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1

        k += 1
        draw(arr)

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
        draw(arr)

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1
        draw(arr)


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)


merge_sort(arr, 0, len(arr) - 1)

plt.ioff()
plt.bar(range(length), arr)
plt.show()

print(arr)