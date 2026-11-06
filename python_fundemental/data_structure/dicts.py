# تعریف دیکشنری
student = {
    "name": "Asma",
    "age": 22,
    "major": "Computer Science"
}

# دسترسی به مقدار
print("نام:", student["name"])
print("رشته:", student["major"])

# اضافه کردن کلید جدید
student["grade"] = "A"
print("اطلاعات کامل:", student)

# پیمایش دیکشنری
for key, value in student.items():
    print(key, ":", value)
