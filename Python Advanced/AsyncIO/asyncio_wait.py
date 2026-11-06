import asyncio


async def task(number):

    await asyncio.sleep(number)

    print(f"Task {number}")


async def main():

    tasks = [

        asyncio.create_task(
            task(1)
        ),

        asyncio.create_task(
            task(2)
        ),

        asyncio.create_task(
            task(3)
        )

    ]

    # صبر تا اتمام همه تسک ها
    await asyncio.wait(tasks)


asyncio.run(main())