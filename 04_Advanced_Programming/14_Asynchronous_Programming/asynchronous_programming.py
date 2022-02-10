# import asyncio


# async def print_something():
#   await asyncio.sleep(1)
#   print("something")


# async def main():
#   print("main")
#   await print_something()
#   print("main again")

# print(type(main()))
# asyncio.run(main())

########## ########## ########## ########## ##########

# import asyncio


# async def print_something():
#   await asyncio.sleep(1)
#   print("something")
#   return "finished"


# async def main():
#   print("main")

#   task = asyncio.create_task(print_something())

#   print("main again")
#   result = await task
  # print("awaited")
  # print(result)


# asyncio.run(main())

########## ########## ########## ########## ##########

# import asyncio


# async def print_values(values, delay):
#   for item in values:
#     print(item)
#     await asyncio.sleep(delay)


# async def main():
#   await print_values([1, 3, 5], 0.2)
#   await print_values([2, 4], 0.3)


# asyncio.run(main())

########## ########## ########## ########## ##########

# import asyncio


# async def print_values(values, delay):
#   for item in values:
#     print(item)
#     await asyncio.sleep(delay)


# async def main():
#   task1 = asyncio.create_task(print_values([1, 3, 5], 0.2))
#   task2 = asyncio.create_task(print_values([2, 4], 0.3))

#   await task1
#   await task2


# asyncio.run(main())

########## ########## ########## ########## ##########

# import asyncio


# async def print_values(values, delay):
#   for item in values:
#     print(item)
#     await asyncio.sleep(delay)

#   return delay


# async def main():
#   values = await asyncio.gather(print_values([1, 3, 5], 0.2),
#                                 print_values([2, 4], 0.3))

#   print(values)

# asyncio.run(main())

########## ########## ########## ########## ##########

# import asyncio


# async def fetch_data():
#   print("Start fetching")
#   await asyncio.sleep(2)
#   print("Done fetching")
#   return [1, 2, 3, 4, 5, 6]


# async def run_algorithm():
#   for i in range(10):
#     print(i)
#     await asyncio.sleep(0.5)


# async def main():
  # data = await asyncio.gather(fetch_data(), run_algorithm())
  # data = await fetch_data()
  # await run_algorithm()
#   data = asyncio.create_task(fetch_data())
#   await run_algorithm()
#   print(await data)


# asyncio.run(main())

########## ########## ########## ########## ##########

# import asyncio

# async def gen(n):
#   for i in range(n):
#     yield i
#     await asyncio.sleep(0.5)


# async def main():
#   async for i in gen(10):
#     print(i)


# asyncio.run(main())

########## ########## ########## ########## ##########

import asyncio

class Test:
  @staticmethod
  async def test():
    print("hi")


async def main():
  await Test.test()


asyncio.run(main())