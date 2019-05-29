# Python Coroutines and Tasks. 
# Coroutines declared with async/await syntax is the preferred way of writing asyncio applications.
#
# To actually run a coroutine, asyncio provides three main mechanisms:
#
# > The asyncio.run() function to run the top-level entry point “main()” function.
# > Awaiting on a coroutine. 
# > The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.
#
# cancel(): 
#
# Request the Task to be cancelled.
# This arranges for a CancelledError exception to be thrown into the wrapped coroutine on the next cycle of the event loop.
# The coroutine then has a chance to clean up or even deny the request by suppressing the exception with a try … … except CancelledError … finally block.
# Therefore, unlike Future.cancel(), Task.cancel() does not guarantee that the Task will be cancelled, although suppressing cancellation completely is not
# common and is actively discouraged.
#
# The following example illustrates how coroutines can intercept the cancellation request:
 
async def cancel_me():
    print('cancel_me(): before sleep')

    try:

        # Wait for 1 hour

        await asyncio.sleep(3600)

    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')

        raise

    finally:
        print('cancel_me(): after sleep')

async def main():

    # Create a "cancel_me" Task

    task = asyncio.create_task(cancel_me())

    # Wait for 1 second

    await asyncio.sleep(1)

    task.cancel()

    try:
        await task

    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")

asyncio.run(main())

# Expected output:
#
#     cancel_me(): before sleep
#     cancel_me(): cancel sleep
#     cancel_me(): after sleep
#     main(): cancel_me is cancelled now
