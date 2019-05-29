# Python Coroutines and Tasks. 
# Coroutines declared with async/await syntax is the preferred way of writing asyncio applications.
#
# To actually run a coroutine, asyncio provides three main mechanisms:
#
# > The asyncio.run() function to run the top-level entry point “main()” function.
# > Awaiting on a coroutine. 
# > The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.
# wait() schedules coroutines as Tasks automatically and later returns those implicitly created Task objects in (done, pending) sets.
#
# Passing coroutine objects to wait() directly is deprecated.
#
# Therefore the following code won’t work as expected:
# 

async def foo():
    return 42

coro = foo()

done, pending = await asyncio.wait({coro})

if coro in done:

    # This branch will never be run!

# 
# Here is how the above snippet can be fixed:
# 

async def foo():
    return 42

task = asyncio.create_task(foo())
done, pending = await asyncio.wait({task})

if task in done:

    # Everything will work as expected now.
