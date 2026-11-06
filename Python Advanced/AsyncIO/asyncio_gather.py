import asyncio


async def worker(name):

    print(f"{name} شروع شد")

    await asyncio.sleep(2)

    print(f"{name} پایان یافت")


async def main():

    await asyncio.gather(

        worker("کارگر اول"),

        worker("کارگر دوم"),

        worker("کارگر سوم")

    )


asyncio.run(
    main()
)