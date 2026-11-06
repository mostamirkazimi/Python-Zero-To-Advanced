# وارد کردن کتابخانه asyncio
import asyncio


# تعریف تابع غیرهمزمان
async def main():

    # چاپ پیام شروع
    print("شروع برنامه")

    # توقف غیرهمزمان به مدت 2 ثانیه
    await asyncio.sleep(2)

    # چاپ پیام پایان
    print("پایان برنامه")


# اجرای تابع غیرهمزمان
asyncio.run(main())