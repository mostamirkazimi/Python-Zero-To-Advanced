# کتابخانه برنامه نویسی غیرهمزمان
import asyncio


# تعریف تابع غیرهمزمان
async def main():

    # پیام شروع
    print("شروع برنامه")

    # توقف غیرهمزمان به مدت 3 ثانیه
    await asyncio.sleep(3)

    # پیام پایان
    print("پایان برنامه")


# اجرای برنامه
asyncio.run(main())