# Decorator همراه با آرگومان

def logger(func):

    def wrapper(*args, **kwargs):

        print("قبل از اجرا")

        result = func(*args, **kwargs)

        print("بعد از اجرا")

        return result

    return wrapper


@logger
def add(a, b):

    return a + b


print(add(10, 20))