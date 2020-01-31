import asyncio,time

def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    return n


start=time.time()
result =fib(20)
print(result)
print(time.time()-start)
