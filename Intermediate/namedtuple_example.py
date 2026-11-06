from collections import namedtuple

Student = namedtuple(
    "Student",
    ["name", "age", "city"]
)

student = Student(
    "Samiullah",
    25,
    "Kabul"
)

print(student.name)
print(student.age)
print(student.city)