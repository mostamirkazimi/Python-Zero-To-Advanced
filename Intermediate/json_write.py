import json

student = {
    "name": "Samiullah",
    "age": 25,
    "city": "Kabul"
}

with open(
    "student.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        student,
        file,
        indent=4
    )

print("فایل ذخیره شد")
