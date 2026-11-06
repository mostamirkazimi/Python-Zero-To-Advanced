import asyncio


async def get_student(student_id):

    print(
        f"دریافت اطلاعات دانشجو {student_id}"
    )

    await asyncio.sleep(2)

    return {
        "id": student_id,
        "name": f"Student {student_id}"
    }


async def main():

    students = await asyncio.gather(

        get_student(1),

        get_student(2),

        get_student(3)

    )

    print(students)


asyncio.run(main())