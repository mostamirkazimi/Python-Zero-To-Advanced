names = [
    "Ali",
    "Sara",
    "Omar"
]

scores = [
    90,
    85,
    95
]

for name, score in zip(
    names,
    scores
):

    print(
        f"{name} : {score}"
    )