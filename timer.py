import time
from functools import wraps

# Decorator to time the function execution
def time_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the actual function
        end_time = time.time()  # Record the end time
        elapsed_time = round(end_time - start_time, 4)
        print(f"Function '{func.__name__}' executed in {elapsed_time} seconds.")
        return result  # Return the result of the original function
    return wrapper
