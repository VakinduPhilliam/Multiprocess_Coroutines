# Python Coroutines and Tasks. 
# Coroutines declared with async/await syntax is the preferred way of writing asyncio applications.
#
# To actually run a coroutine, asyncio provides three main mechanisms:
#
# > The asyncio.run() function to run the top-level entry point “main()” function.
# > Awaiting on a coroutine. 
# > The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.
#
# For example, the following snippet of code (requires Python 3.7+) prints “hello”, waits 1 second, and then prints “world”:
# 
# Note that simply calling a coroutine will not schedule it to be executed:
#


import asyncio

async def main():
        print('hello')

        await asyncio.sleep(1)

        print('world')

asyncio.run(main())

#
# OUTPUT:
#
# hello
# world

