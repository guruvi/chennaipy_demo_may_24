from subinterpreter_parallelism import parallel
from random import randint
import isolated_benchmark
import time

# Number of task runs to spawn.
NUM_TASKS = 10

# Increase MIN & MAX to increase time taken by each task (should be < 1000000000)
MIN = 90000000
MAX = 90000100

# Benchmark Python function against the custom handwritten sub-interpreter parallelism module.
print(f"Sub-interpreter started for {NUM_TASKS} regular Python tasks")
start = time.time()

result = parallel(*[['isolated_benchmark', 'some_method', (randint(MIN,MAX),)] for _ in range(NUM_TASKS)])

end = time.time()
print(f"Sub-interpreter execution ended in {end-start} seconds")
