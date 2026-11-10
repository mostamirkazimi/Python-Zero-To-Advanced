list = [2,4,5,6,8,9,11,14]

def binary_sort(list,seek):
    if len(list) < 2:
        if list[0] == seek:
            return "Found"
        else:
            return "Not Found"

    else:
        mid = len(list)//2
        if list[mid] == seek:
            return "Found"
        elif list[mid] > seek:
            return binary_sort(list[:mid],seek)
        else:
            return binary_sort(list[mid:],seek)
sort = binary_sort(list,3)
print(sort)

