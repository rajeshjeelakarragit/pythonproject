import asyncio

class AsyncIterator:
    def __init__(self, count):
        self.count = count

    async def __aiter__(self):
        self.current = 0
        return self

    async def __anext__(self):
        if self.current < self.count:
            await asyncio.sleep(0.5)  # Simulate async operation
            self.current += 1
            return self.current
        else:
            raise StopAsyncIteration

async def main():
    async for number in AsyncIterator(5):
        print(f"Number: {number}")

asyncio.run(main())
