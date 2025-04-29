import asyncio

async def run_command():
    proc = await asyncio.create_subprocess_exec(
        'echo', 'Hello, subprocess!',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await proc.communicate()
    print(f"[stdout]: {stdout.decode().strip()}")
    if stderr:
        print(f"[stderr]: {stderr.decode().strip()}")

asyncio.run(run_command())
