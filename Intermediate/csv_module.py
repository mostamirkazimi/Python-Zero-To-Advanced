import csv

with open(
    "students.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow(
        ["Name", "Age"]
    )

    writer.writerow(
        ["Samiullah", 25]
    )

print("CSV Saved")