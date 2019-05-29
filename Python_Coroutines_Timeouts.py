# Python Coroutines and Tasks. 
# Coroutines declared with async/await syntax is the preferred way of writing asyncio applications.
#
# To actually run a coroutine, asyncio provides three main mechanisms:
#
# > The asyncio.run() function to run the top-level entry point “main()” function.
# > Awaiting on a coroutine. 
# > The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.
#
# Timeouts:
# coroutine asyncio.wait_for(aw, timeout, *, loop=None) 
# Wait for the aw awaitable to complete with a timeout.
# 
# If 'aw' is a coroutine it is automatically scheduled as a Task.
# 'timeout' can either be None or a float or int number of seconds to wait for. If timeout is None, block until the future completes.
# If a timeout occurs, it cancels the task and raises asyncio.TimeoutError.
# To avoid the task cancellation, wrap it in shield().
# The function will wait until the future is actually cancelled, so the total wait time may exceed the timeout.
# If the wait is cancelled, the future aw is also cancelled.
# The 'loop' argument is deprecated and scheduled for removal in Python 3.10.
# 
# Example:
# 

async def eternity():

    # Sleep for one hour

    await asyncio.sleep(3600)
    print('yay!')

async def main():

    # Wait for at most 1 second

    try:
        await asyncio.wait_for(eternity(), timeout=1.0)

    except asyncio.TimeoutError:
        print('timeout!')

asyncio.run(main())

# Expected output:
#
#     timeout!
