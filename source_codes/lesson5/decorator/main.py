import time

def time_it(func):
    """Decorator that prints the execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start
        result = func(*args, **kwargs)  # Run the actual function
        end_time = time.time()    # Record end
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

@time_it
def heavy_computation():
    # Simulate a delay
    time.sleep(1.5)
    print("Computation complete!")

heavy_computation()