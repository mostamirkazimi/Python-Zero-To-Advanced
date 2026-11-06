class Counter:

    def __init__(self, max_number):

        self.max_number = max_number

        self.current = 0

    def __iter__(self):

        return self

    def __next__(self):

        if self.current < self.max_number:

            self.current += 1

            return self.current

        raise StopIteration


counter = Counter(5)

for number in counter:

    print(number)