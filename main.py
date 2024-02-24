import timeit
import matplotlib.pyplot as plt

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Measure execution time for recursion and iteration
input_sizes = list(range(1, 101))  # Input sizes from 1 to 100
recursive_times = []
iterative_times = []

for n in input_sizes:
    recursive_time = timeit.timeit(lambda: factorial_recursive(n), number=1000)
    recursive_times.append(recursive_time)

    iterative_time = timeit.timeit(lambda: factorial_iterative(n), number=1000)
    iterative_times.append(iterative_time)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, recursive_times, label='Recursive', marker='o')
plt.plot(input_sizes, iterative_times, label='Iterative', marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Performance Comparison: Recursion vs. Iteration')
plt.legend()
plt.grid(True)
# Add footer with @sudheer debbati
plt.figtext(0.5, 0.01, '@sudheer debbati', horizontalalignment='center', fontsize=10)

plt.show()