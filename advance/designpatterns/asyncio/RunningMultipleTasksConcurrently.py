import asyncio

async def task1():
    print("Task 1 is starting...")
    await asyncio.sleep(2)
    print("Task 1 is complete!")

async def task2():
    print("Task 2 is starting...")
    await asyncio.sleep(1)
    print("Task 2 is complete!")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
