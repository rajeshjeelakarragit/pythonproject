import asyncio

async def say_hello():
    print("Hello!")
    await asyncio.sleep(1)  # Simulate I/O or delay
    print("World!")

asyncio.run(say_hello())
