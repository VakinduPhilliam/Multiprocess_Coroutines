# Python Coroutines and Tasks. 
# Coroutines declared with async/await syntax is the preferred way of writing asyncio applications.
#
# To actually run a coroutine, asyncio provides three main mechanisms:
#
# > The asyncio.run() function to run the top-level entry point “main()” function.
# > Awaiting on a coroutine. 
# > The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.
# Generator-based Coroutines:
# 
# Note: 
# Support for generator-based coroutines is deprecated and is scheduled for removal in Python 3.10.
# Generator-based coroutines predate async/await syntax. They are Python generators that use yield from expressions to await on Futures and other coroutines.
# Generator-based coroutines should be decorated with @asyncio.coroutine, although this is not enforced.
#
# @asyncio.coroutine: 
# Decorator to mark generator-based coroutines. 
#
# This decorator enables legacy generator-based coroutines to be compatible with async/await code:
# 

@asyncio.coroutine

def old_style_coroutine():
    yield from asyncio.sleep(1)

async def main():
    await old_style_coroutine()
