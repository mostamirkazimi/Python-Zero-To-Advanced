import threading


def worker(name):

    for i in range(3):

        print(
            name,
            i
        )


t1 = threading.Thread(
    target=worker,
    args=("Thread1",)
)

t2 = threading.Thread(
    target=worker,
    args=("Thread2",)
)

t1.start()
t2.start()

t1.join()
t2.join()
