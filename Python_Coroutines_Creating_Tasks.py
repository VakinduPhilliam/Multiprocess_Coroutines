# Python Coroutines and Tasks. 
# Coroutines declared with async/await syntax is the preferred way of writing asyncio applications.
#
# To actually run a coroutine, asyncio provides three main mechanisms:
#
# > The asyncio.run() function to run the top-level entry point “main()” function.
# > Awaiting on a coroutine. 
# > The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.
#
# Creating Tasks:
# asyncio.create_task(coro) 
# Wrap the coro coroutine into a Task and schedule its execution. Return the Task object.
# The task is executed in the loop returned by get_running_loop(), RuntimeError is raised if there is no running loop in current thread.
# This function has been added in Python 3.7. Prior to Python 3.7, the low-level asyncio.ensure_future() function can be used instead:
# 

async def coro():

#    ...

# In Python 3.7+

task = asyncio.create_task(coro())

# ...

# This works in all Python versions but is less readable

task = asyncio.ensure_future(coro())

# ...
