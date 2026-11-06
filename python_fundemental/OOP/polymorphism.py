class Bird:
    def speak(self):
        print("پرنده می‌گوید: جیک جیک")

class Fish:
    def speak(self):
        print("ماهی می‌گوید: ... (ساکت است)")

class Human:
    def speak(self):
        print("انسان می‌گوید: سلام دنیا!")

# استفاده از چندریختی
creatures = [Bird(), Fish(), Human()]

for creature in creatures:
    creature.speak()
