# How to calculate execution time in Python


import time

start_time = time.perf_counter() # Start the timer

for i in range(1000000): 
    pass  # Simulating some work

end_time = time.perf_counter() # End the timer

elapsed_time = end_time - start_time # Calculate the elapsed time

print(f"Elapsed time: {elapsed_time:.6f} seconds")