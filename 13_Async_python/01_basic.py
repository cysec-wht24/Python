# async def: declare a coroutine (special function that can be paused)
# await: Pauses execution until the result is ready
# asyncio: Build in pyhon library
# Event loop: The engine that runs and schedule co-routines in python



import asyncio

async def brew_chai():
    print("Brewing")
    await asyncio.sleep(2)
    print("Chai is ready")

asyncio.run(brew_chai())