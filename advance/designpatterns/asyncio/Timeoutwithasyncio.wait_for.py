import asyncio

async def long_running_task():
    await asyncio.sleep(5)
    print("Task completed!")

async def main():
    try:
        await asyncio.wait_for(long_running_task(), timeout=2)
    except asyncio.TimeoutError:
        print("The task timed out!")

asyncio.run(main())
