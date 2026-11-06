# تعریف یک کلاس ساده
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"سلام، من {self.name} هستم و {self.age} سال دارم.")

# ساخت آبجکت
p1 = Person("Samiullah", 25)
p1.greet()

p2 = Person("Asma", 22)
p2.greet()
