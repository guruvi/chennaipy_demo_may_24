from concurrent.futures import ProcessPoolExecutor
import time

def some_method(n):
    x = 0
    for i in range(10**7):
        x += i * i
    return x

if __name__ == "__main__":
    start = time.time()
    with ProcessPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(some_method, range(10)))
    print("ProcessPool time:", time.time() - start)
