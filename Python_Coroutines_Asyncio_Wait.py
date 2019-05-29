# Python Coroutines and Tasks. 
# Coroutines declared with async/await syntax is the preferred way of writing asyncio applications.
#
# To actually run a coroutine, asyncio provides three main mechanisms:
#
# > The asyncio.run() function to run the top-level entry point “main()” function.
# > Awaiting on a coroutine. 
# > The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.
#
# Waiting Primitives:
#
# coroutine asyncio.wait(aws, *, loop=None, timeout=None, return_when=ALL_COMPLETED).
# Run awaitable objects in the aws set concurrently and block until the condition specified by return_when.
# If any awaitable in aws is a coroutine, it is automatically scheduled as a Task. Passing coroutines objects to wait() directly is deprecated as it leads
# to confusing behavior.
# 
# Returns two sets of Tasks/Futures: (done, pending).
# 
# Usage:
# 

done, pending = await asyncio.wait(aws)
