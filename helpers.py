import time

class PerformanceOptimizer:
    def __init__(self):
        self.execution_times = []

    def time_function(self, func):
        """Decorator to time a function's execution."""
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            self.execution_times.append(end_time - start_time)
            return result
        return wrapper

    def average_execution_time(self):
        """Calculate average execution time of decorated functions."""
        if not self.execution_times:
            return 0
        return sum(self.execution_times) / len(self.execution_times)

optimizer = PerformanceOptimizer()

@optimizer.time_function
def some_heavy_computation(x):
    time.sleep(x)  # Simulate a time-consuming function
    return x * 2

if __name__ == '__main__':
    for i in range(1, 6):
        print(some_heavy_computation(i))
    print(f"Average execution time: {optimizer.average_execution_time():.4f} seconds")
