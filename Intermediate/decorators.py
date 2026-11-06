# Decorator ساده

def logger(func):

    def wrapper():

        print("شروع تابع")

        func()

        print("پایان تابع")

    return wrapper


@logger
def hello():

    print("سلام سید جان")


hello()