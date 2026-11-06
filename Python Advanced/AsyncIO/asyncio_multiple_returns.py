import asyncio


async def square(num):

    return num ** 2


async def main():

    results = await asyncio.gather(

        square(2),

        square(3),

        square(4)

    )

    print(results)


asyncio.run(main())