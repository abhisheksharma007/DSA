# cpu_threading.py
import time
from threading import Thread
from multiprocessing import Process
import asyncio

# CPU Tasks
def cpu_task(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

# Single-thread run
# start = time.time()
# cpu_task(20_000_000)
# cpu_task(20_000_000)
# print("Single-thread time:", time.time() - start)

# Multithreading run
# start = time.time()
# t1 = Thread(target=cpu_task, args=(20_000_000,))
# t2 = Thread(target=cpu_task, args=(20_000_000,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("Multithreading time:", time.time() - start)

# Multiprocessing run
# if __name__ == "__main__":
    # start = time.time()
    # p1 = Process(target=cpu_task, args=(20_000_000,))
    # p2 = Process(target=cpu_task, args=(20_000_000,))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    # print("Multiprocessing time:", time.time() - start)
    

# I/O Tasks
def io_task():
    time.sleep(1)

# Single Thread run
# start = time.time()
# for _ in range(5):
#     io_task()
# print("Single-thread I/O time:", time.time() - start)

# Multithreading I/O run
# threads = []
# start = time.time()
# for _ in range(5):
#     t = Thread(target=io_task)
#     threads.append(t)
#     t.start()
# for t in threads:
#     t.join()
# print("Multithreading I/O time:", time.time() - start)

# Async I/O run
async def io_task():
    await asyncio.sleep(1)
async def main():
    tasks = [io_task() for _ in range(5)]
    await asyncio.gather(*tasks)
start = time.time()
asyncio.run(main())
print("Async I/O time:", time.time() - start)