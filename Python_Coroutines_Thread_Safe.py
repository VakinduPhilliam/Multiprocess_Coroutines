# Python Coroutines and Tasks. 
# Coroutines declared with async/await syntax is the preferred way of writing asyncio applications.
#
# To actually run a coroutine, asyncio provides three main mechanisms:
#
# > The asyncio.run() function to run the top-level entry point “main()” function.
# > Awaiting on a coroutine. 
# > The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.
#
# asyncio.run_coroutine_threadsafe(coro, loop): 
# Submit a coroutine to the given event loop. Thread-safe.
# 
# Return a concurrent.futures.Future to wait for the result from another OS thread.
# This function is meant to be called from a different OS thread than the one where the event loop is running.
#
# Example:
# 

# Create a coroutine

coro = asyncio.sleep(1, result=3)

# Submit the coroutine to a given loop

future = asyncio.run_coroutine_threadsafe(coro, loop)

# Wait for the result with an optional timeout argument

assert future.result(timeout) == 3
