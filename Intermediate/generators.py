# Generator ساده

def counter():

    for i in range(1, 11):

        yield i


gen = counter()

for number in gen:

    print(number)