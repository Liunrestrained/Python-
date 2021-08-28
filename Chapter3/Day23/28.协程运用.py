'''不要让用户手动去切换，而是遇到IO操作时能自动切换。
Python在3.4之后推出了asyncio模块 + Python3.5推出async、async语法 ，内部基于协程并且遇到IO请求自动化切换。'''

import asyncio


async def func1():
    print(1)
    await asyncio.sleep(2)
    print(2)


async def func2():
    print(3)
    await asyncio.sleep(2)
    print(4)


tasks = [asyncio.ensure_future(func1()),
         asyncio.ensure_future(func2())]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
