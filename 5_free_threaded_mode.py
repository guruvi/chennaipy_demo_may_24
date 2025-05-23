from concurrent.futures import ThreadPoolExecutor
import time

def some_method(n):
    x = 0
    for i in range(10**7):
        x += i * i
    return x


start = time.time()
with ThreadPoolExecutor(max_workers=10) as executor:
	results = executor.map(some_method, range(10))

print("Time taken:", time.time() - start)
