import asyncio


# تابع غیرهمزمان
async def download():

    print("شروع دانلود")

    await asyncio.sleep(2)

    print("دانلود تکمیل شد")


asyncio.run(
    download()
)