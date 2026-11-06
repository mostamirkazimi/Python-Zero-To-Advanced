class MyFile:

    def __enter__(self):

        print("File Opened")

        return self

    def __exit__(
        self,
        exc_type,
        exc_val,
        exc_tb
    ):

        print("File Closed")


with MyFile():

    print("Working...")