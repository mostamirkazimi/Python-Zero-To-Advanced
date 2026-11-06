# ذخیره داده در CSV

import csv


with open(
    "students.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(
        file
    )

    writer.writerow(
        ["Name", "Age"]
    )

    writer.writerow(
        ["Samiullah", 25]
    )

print("CSV Saved")