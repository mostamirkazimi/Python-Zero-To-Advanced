# کلاس پایه
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} صدایی دارد.")

# کلاس فرزند
class Dog(Animal):
    def speak(self):
        print(f"{self.name} می‌گوید: هاپ هاپ!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} می‌گوید: میاو!")

# استفاده
dog = Dog("Bobby")
cat = Cat("Kitty")

dog.speak()
cat.speak()
