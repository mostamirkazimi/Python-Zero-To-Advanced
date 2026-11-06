import os

# مسیر فعلی
print("مسیر فعلی:", os.getcwd())

# ساخت پوشه جدید
os.mkdir("test_folder")
print("پوشه ساخته شد.")

# لیست فایل‌ها و پوشه‌ها
print("لیست فایل‌ها:", os.listdir())

# حذف پوشه
os.rmdir("test_folder")
print("پوشه حذف شد.")
