# Python Coroutines and Tasks. 
# Coroutines declared with async/await syntax is the preferred way of writing asyncio applications.
#
# To actually run a coroutine, asyncio provides three main mechanisms:
#
# > The asyncio.run() function to run the top-level entry point “main()” function.
# > Awaiting on a coroutine. 
# > The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.
#
# Running Tasks Concurrently:
#
# awaitable asyncio.gather(*aws, loop=None, return_exceptions=False). 
# Run awaitable objects in the aws sequence concurrently.
# If any awaitable in aws is a coroutine, it is automatically scheduled as a Task.
# If all awaitables are completed successfully, the result is an aggregate list of returned values.
# The order of result values corresponds to the order of awaitables in aws.
# If return_exceptions is False (default), the first raised exception is immediately propagated to the task that awaits on gather().
# Other awaitables in the aws sequence won’t be cancelled and will continue to run.
# If return_exceptions is True, exceptions are treated the same as successful results, and aggregated in the result list.
# If gather() is cancelled, all submitted awaitables (that have not completed yet) are also cancelled.
# If any Task or Future from the aws sequence is cancelled, it is treated as if it raised CancelledError – the gather() call is not cancelled in this case.
# This is to prevent the cancellation of one submitted Task/Future to cause other Tasks/Futures to be cancelled.
# 
# Example:
# 

import asyncio

async def factorial(name, number):
    f = 1

    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")

        await asyncio.sleep(1)
        f *= i

    print(f"Task {name}: factorial({number}) = {f}")

async def main():

    # Schedule three calls *concurrently*:

    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

asyncio.run(main())

# Expected output:
#
#     Task A: Compute factorial(2)...
#     Task B: Compute factorial(2)...
#     Task C: Compute factorial(2)...
#     Task A: factorial(2) = 2
#     Task B: Compute factorial(3)...
#     Task C: Compute factorial(3)...
#     Task B: factorial(3) = 6
#     Task C: Compute factorial(4)...
#     Task C: factorial(4) = 24
