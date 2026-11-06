# Generator بی‌نهایت

def infinite_counter():

    num = 1

    while True:

        yield num

        num += 1


gen = infinite_counter()

for _ in range(10):

    print(next(gen))