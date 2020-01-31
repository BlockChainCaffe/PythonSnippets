import asyncio, time

# def memo(fn):
#     cache = {}
#     async def wrap(n):
#         if n in cache:
#             print("found %s in cache" % (n))
#             return cache[n]
#         res = await fn(n)
#         print("calculated %s" % (n))
#         cache[n]= res
#         return res
#     return wrap

# @memo
async def fibn(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return await fibn(n-2) + await fibn(n-1)


start=time.time()
loop = asyncio.get_event_loop()
c = loop.run_until_complete(asyncio.gather(fibn(20)))
print(c)
loop.close()
print(time.time()-start)