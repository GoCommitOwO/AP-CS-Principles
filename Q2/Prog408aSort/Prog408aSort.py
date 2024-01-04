# MainProgram.py
import time
from SortLibrary import *
from Helper import *

# Function to print a list of ScoreRecord objects
def print_sorted_data(data, label):
    print(f"{label} sorted:")
    stringtoprint = ""
    for record in data:
        stringtoprint += str(record) + "\t"
    print(stringtoprint)

# Function to benchmark sorting algorithms
def benchmark_sorting(data, sort_function, label):
    start_time = time.perf_counter()
    sort_function(data)
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"\n{label} sort duration: {duration:.6f} seconds")

# Read data from prg408a.dat
with open("C:\\Users\\rynes.a\\PycharmProjects\\AP-CS-Principles\\Langdat\\prg408a.txt", "r") as file:
    lines = file.readlines()

# Create a list of ScoreRecord objects
score_records = []
for line in lines:
    id_str, score_str = line.strip().split()
    id = int(id_str)
    score = int(score_str)
    record = className(id, score)
    score_records.append(record)

# Create copies of the original list for sorting
bubble_sort_data = score_records[:]
selection_sort_data = score_records[:]
insertion_sort_data = score_records[:]
python_sort_data = score_records[:]


# Reverse the sorted lists
bubble_sort_data.reverse()


# sort data and then get time

# bubble
benchmark_sorting(bubble_sort_data, bubbleSort, "Bubble")
print_sorted_data(bubble_sort_data, "Bubble")


# selection
benchmark_sorting(selection_sort_data, selectionSort, "Selection")
print_sorted_data(selection_sort_data, "Selection")

# insertion
benchmark_sorting(insertion_sort_data, insertionSort, "Insertion")
print_sorted_data(insertion_sort_data, "Insertion")

# python default
benchmark_sorting(python_sort_data, pythonSort, "Python")
print_sorted_data(python_sort_data, "Python")
