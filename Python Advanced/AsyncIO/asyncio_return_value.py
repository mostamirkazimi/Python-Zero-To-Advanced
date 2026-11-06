import asyncio


async def calculate():

    await asyncio.sleep(2)

    return 100


async def main():

    result = await calculate()

    print(
        "نتیجه:",
        result
    )


asyncio.run(main())
