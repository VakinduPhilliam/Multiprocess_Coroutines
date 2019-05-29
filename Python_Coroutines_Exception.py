# Python Coroutines and Tasks. 
# Coroutines declared with async/await syntax is the preferred way of writing asyncio applications.
#
# To actually run a coroutine, asyncio provides three main mechanisms:
#
# > The asyncio.run() function to run the top-level entry point “main()” function.
# > Awaiting on a coroutine. 
# > The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.
#
# If an exception is raised in the coroutine, the returned Future will be notified.
# It can also be used to cancel the task in the event loop:
 

try:
    result = future.result(timeout)

except asyncio.TimeoutError:
    print('The coroutine took too long, cancelling the task...')

    future.cancel()

except Exception as exc:
    print(f'The coroutine raised an exception: {exc!r}')

else:
    print(f'The coroutine returned: {result!r}')
