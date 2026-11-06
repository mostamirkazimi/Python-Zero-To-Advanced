# وارد کردن کش آماده پایتون
from functools import lru_cache


# فعال کردن کش
@lru_cache(maxsize=100)
def fibonacci(n):

    # شرط توقف
    if n < 2:
        return n

    # محاسبه فیبوناچی
    return (
        fibonacci(n - 1)
        +
        fibonacci(n - 2)
    )


# نمایش نتیجه
print(
    fibonacci(100)
)