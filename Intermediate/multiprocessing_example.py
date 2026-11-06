from multiprocessing import Process


def task():

    print(
        "Running Process"
    )


p = Process(
    target=task
)

p.start()

p.join()