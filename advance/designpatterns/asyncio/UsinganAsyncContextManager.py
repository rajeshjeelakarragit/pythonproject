import asyncio


class AsyncContext:
    async def __aenter__(self):
        print("Entering context...")
        await asyncio.sleep(1)
        print("Entered!")

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context...")
        await asyncio.sleep(1)
        print("Exited!")


async def main():
    async with AsyncContext():
        print("Inside the context!")


asyncio.run(main())

"""
Entering context...
Entered!
Inside the context!
Exiting context...
Exited!
"""