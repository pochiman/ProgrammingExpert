##### Add One Asynchronous #####

# Write a function named add_one that accepts a coroutine as a mandatory parameter 
# then calls the coroutine and returns the coroutine's return value plus one.

async def add_one(coroutine):
    return_value = await coroutine()
    return return_value + 1