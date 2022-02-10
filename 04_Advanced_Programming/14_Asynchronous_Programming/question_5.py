##### Asynchronous Concurrency #####

# Schedule the existing function to run multiple times such that lst = [1, 3, 2, 4, 6, 5] at the end of the program.
# Run all your function calls concurrently using asyncio.  Your code should not take longer than 1 second to run.

import asyncio


async def append_two_values(lst, value1, value2):
    lst.append(value1)
    await asyncio.sleep(0.5)
    lst.append(value2)


lst = []


async def main(lst):
    futures = [append_two_values(lst, 1, 4), append_two_values(lst, 3, 6), append_two_values(lst, 2, 5)]
    await asyncio.gather(*futures)


asyncio.run(main(lst))