import threading


def task():

    for i in range(5):

        print(
            f"Task {i}"
        )


thread = threading.Thread(
    target=task
)

thread.start()

thread.join()

print("Finished")
