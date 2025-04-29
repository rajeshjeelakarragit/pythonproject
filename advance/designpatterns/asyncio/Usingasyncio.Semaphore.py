import asyncio

"""
Control the number of concurrent coroutines.
"""
semaphore = asyncio.Semaphore(2)

async def limited_task(name):
    async with semaphore:
        print(f"{name} is starting...")
        await asyncio.sleep(2)
        print(f"{name} is done!")

async def main():
    tasks = [limited_task(f"Task {i}") for i in range(5)]
    await asyncio.gather(*tasks)

asyncio.run(main())