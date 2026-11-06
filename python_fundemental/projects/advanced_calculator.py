class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "❌ تقسیم بر صفر امکان‌پذیر نیست!"

# استفاده از ماشین حساب
calc = Calculator()
print("جمع:", calc.add(10, 5))
print("تفریق:", calc.subtract(10, 5))
print("ضرب:", calc.multiply(10, 5))
print("تقسیم:", calc.divide(10, 0))
