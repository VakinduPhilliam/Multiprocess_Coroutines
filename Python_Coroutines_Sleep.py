# Python Coroutines and Tasks. 
# Coroutines declared with async/await syntax is the preferred way of writing asyncio applications.
#
# To actually run a coroutine, asyncio provides three main mechanisms:
#
# > The asyncio.run() function to run the top-level entry point “main()” function.
# > Awaiting on a coroutine. 
# > The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.
# Sleeping:
# coroutine asyncio.sleep(delay, result=None, *, loop=None) 
# Block for delay seconds.
# If result is provided, it is returned to the caller when the coroutine completes.
# sleep() always suspends the current task, allowing other tasks to run.
# The loop argument is deprecated and scheduled for removal in Python 3.10.
# Example of coroutine displaying the current date every second for 5 seconds:
# 

import asyncio
import datetime

async def display_date():
    loop = asyncio.get_running_loop()

    end_time = loop.time() + 5.0

    while True:

        print(datetime.datetime.now())

        if (loop.time() + 1.0) >= end_time:
            break

        await asyncio.sleep(1)

asyncio.run(display_date())
