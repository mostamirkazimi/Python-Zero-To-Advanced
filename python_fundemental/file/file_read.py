# خواندن محتوای یک فایل متنی
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("محتوای فایل:")
    print(content)
