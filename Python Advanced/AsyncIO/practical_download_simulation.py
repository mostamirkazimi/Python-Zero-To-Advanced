import asyncio


async def download_file(file_name):

    print(
        f"{file_name} در حال دانلود..."
    )

    await asyncio.sleep(3)

    print(
        f"{file_name} دانلود شد."
    )


async def main():

    await asyncio.gather(

        download_file("file1"),

        download_file("file2"),

        download_file("file3")

    )


asyncio.run(main())