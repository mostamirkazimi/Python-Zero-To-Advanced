# اضافه کردن متن جدید به فایل موجود
with open("example.txt", "a", encoding="utf-8") as file:
    file.write("این یک خط جدید است که اضافه شد.\n")

print("متن جدید به فایل اضافه شد.")
