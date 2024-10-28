import time
import random


def measure_execution_time(func, sizes):
    times = []
    for size in sizes:
        # Create a random array of the given size
        arr = random.sample(range(size), size)

        # Measure the time taken by the function
        start_time = time.time()
        func(arr)
        end_time = time.time()

        # Calculate the time difference
        times.append(end_time - start_time)

    return times
