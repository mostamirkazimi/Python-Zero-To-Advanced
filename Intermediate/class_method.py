class Student:

    school = "Kabul School"

    @classmethod
    def get_school(cls):

        return cls.school


print(
    Student.get_school()
)