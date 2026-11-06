# پیاده سازی الگوی Singleton

class Singleton:

    # نگهداری نمونه ساخته شده
    _instance = None

    def __new__(cls):

        # اگر هنوز نمونه‌ای ساخته نشده بود
        if cls._instance is None:

            cls._instance = super().__new__(
                cls
            )

        return cls._instance


# ساخت دو شیء
obj1 = Singleton()
obj2 = Singleton()

# بررسی یکی بودن اشیاء
print(
    obj1 is obj2
)