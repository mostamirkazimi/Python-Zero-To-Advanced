list = [2,6,4,3,8,6]
seek = 4
for i in list:
    if i == seek:
        print("Found")
        break
else:
    print("not found")