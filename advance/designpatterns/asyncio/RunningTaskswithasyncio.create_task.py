import asyncio

async def background_task(name, delay):
    print(f"Task {name} is starting...")
    await asyncio.sleep(delay)
    print(f"Task {name} is complete!")

async def main():
    task1 = asyncio.create_task(background_task("One", 2))
    task2 = asyncio.create_task(background_task("Two", 1))
    print("Waiting for tasks to complete...")
    await task1
    await task2

asyncio.run(main())

"""
Waiting for tasks to complete...
Task One is starting...
Task Two is starting...
Task Two is complete!
Task One is complete!
"""