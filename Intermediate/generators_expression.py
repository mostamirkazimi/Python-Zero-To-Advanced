# Generator Expression

numbers = (
    x ** 2
    for x in range(10)
)

for item in numbers:

    print(item)