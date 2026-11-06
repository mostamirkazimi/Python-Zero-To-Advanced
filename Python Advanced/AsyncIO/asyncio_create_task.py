import asyncio


async def task1():

    await asyncio.sleep(2)

    print("Task 1")


async def task2():

    await asyncio.sleep(1)

    print("Task 2")


async def main():

    # ساخت Task ها
    t1 = asyncio.create_task(
        task1()
    )

    t2 = asyncio.create_task(
        task2()
    )

    # انتظار برای اتمام
    await t1
    await t2


asyncio.run(
    main()
)