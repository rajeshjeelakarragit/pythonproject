import asyncio

async def periodic_task(interval):
    while True:
        print("Running periodic task...")
        await asyncio.sleep(interval)

async def main():
    task = asyncio.create_task(periodic_task(2))
    await asyncio.sleep(10)  # Run for 10 seconds
    task.cancel()

asyncio.run(main())
