from dataclasses import dataclass

@dataclass
class Student:

    name: str
    age: int
    city: str


student = Student(
    "Samiullah",
    25,
    "Kabul"
)

print(student)