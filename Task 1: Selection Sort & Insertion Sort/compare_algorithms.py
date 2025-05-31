# Importing necessary libraries
import time                   # Used to measure execution time of each sorting algorithm
import random                 # Used to generate random test datasets
import matplotlib.pyplot as plt  # Used to plot and visualize comparison graphs

from InsertionSort import InsertionSort   # Importing InsertionSort class
from SelectionSort import SelectionSort   # Importing SelectionSort class

# Function to compare performance of both sorting algorithms on different input sizes
def compare_algorithms():
    sizes = [10, 100, 500]       # Different dataset sizes for comparison
    selection_times = []         # To store execution times of selection sort
    insertion_times = []         # To store execution times of insertion sort

    # Loop through each dataset size
    for size in sizes:
        # Generate a random dataset of the given size
        test_data = [random.randint(0, 1000) for _ in range(size)]

        # Measure Selection Sort time
        ss = SelectionSort()
        start = time.time()
        ss.sort(test_data)
        selection_times.append(time.time() - start)

        # Measure Insertion Sort time
        isort = InsertionSort()
        start = time.time()
        isort.sort(test_data)
        insertion_times.append(time.time() - start)

    # Plotting the results
    plt.figure(figsize=(8, 6))
    plt.plot(sizes, selection_times, label='Selection Sort', marker='o')
    plt.plot(sizes, insertion_times, label='Insertion Sort', marker='o')
    plt.xlabel("Dataset Size")
    plt.ylabel("Execution Time (s)")
    plt.title("Selection vs Insertion Sort Performance")
    plt.legend()
    plt.grid(True)

    # Save the plot to file
    plt.savefig("selection_vs_insertion_sort.png")

    # Show the plot
    plt.show()

# Call the function to execute comparison
compare_algorithms()
