# Python Coroutines and Tasks. 
# Coroutines declared with async/await syntax is the preferred way of writing asyncio applications.
#
# To actually run a coroutine, asyncio provides three main mechanisms:
#
# > The asyncio.run() function to run the top-level entry point “main()” function.
# > Awaiting on a coroutine. 
# > The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.
# asyncio.as_completed(aws, *, loop=None, timeout=None): 
# Run awaitable objects in the aws set concurrently. Return an iterator of Future objects. Each Future object returned represents the earliest result from the
# set of the remaining awaitables.
# 
# Raises asyncio.TimeoutError if the timeout occurs before all Futures are done.
# 
# Example:
# 

for f in as_completed(aws):
    earliest_result = await f

    # ...
