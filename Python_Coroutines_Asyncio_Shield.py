# Python Coroutines and Tasks. 
# Coroutines declared with async/await syntax is the preferred way of writing asyncio applications.
#
# To actually run a coroutine, asyncio provides three main mechanisms:
#
# > The asyncio.run() function to run the top-level entry point “main()” function.
# > Awaiting on a coroutine. 
# > The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.
# Shielding From Cancellation:
# awaitable asyncio.shield(aw, *, loop=None): 
# Protect an awaitable object from being cancelled.
# If aw is a coroutine it is automatically scheduled as a Task.
#
# 
# The statement:
#
# 

res = await shield(something())
 
#
#
# is equivalent to:
#
# 

res = await something()
 
#
#
# except that if the coroutine containing it is cancelled, the Task running in something() is not cancelled.
# From the point of view of something(), the cancellation did not happen. Although its caller is still cancelled, so the “await” expression still raises
# a CancelledError.
# 
# If something() is cancelled by other means (i.e. from within itself) that would also cancel shield().
# 
# If it is desired to completely ignore cancellation (not recommended) the shield() function should be combined with a try/except clause, as follows:
# 

try:
    res = await shield(something())

except CancelledError:
    res = None
