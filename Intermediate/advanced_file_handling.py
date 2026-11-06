with open(
    "data.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "Hello Python"
    )


with open(
    "data.txt",
    "r",
    encoding="utf-8"
) as file:

    print(
        file.read()
    )
