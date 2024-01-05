# MainProgram.py
import time
from SortLibrary import *
from Helper import *

# Function to print a list of ScoreRecord objects

def print_sorted_data(data, label):
    data.reverse()
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
    return duration


# Read data from data.dat
with open("Data/data.dat", "r") as file:
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


# benchmark the sorted data
bubble_time = benchmark_sorting(bubble_sort_data, bubbleSort, "Bubble")
selection_time = benchmark_sorting(selection_sort_data, selectionSort, "Selection")
insertion_time = benchmark_sorting(insertion_sort_data, insertionSort, "Insertion")
python_time = benchmark_sorting(python_sort_data, pythonSort, "Python")

# add the times to a list and find the fastest and slowest
times = [bubble_time, selection_time, insertion_time, python_time]
fastestTime = min(times)
slowestTime = max(times)

#get the index of the sort
fastestIndex = times.index(fastestTime)
slowestIndex = times.index(slowestTime)

# get the name of the sort
fastestSortName = ["Bubble", "Selection", "Insertion", "Python"][fastestIndex]
slowestSortName = ["Bubble", "Selection", "Insertion", "Python"][slowestIndex]


# bubble
print_sort_time("Bubble", bubble_time)
print_sorted_data(bubble_sort_data, "Bubble")

# selection
print_sort_time("Selection", selection_time)
print_sorted_data(selection_sort_data, "Selection")

# insertion
print_sort_time("Insertion", insertion_time)
print_sorted_data(insertion_sort_data, "Insertion")

# python default
print_sort_time("Python", python_time)
print_sorted_data(python_sort_data, "Python")

# fastest sort
print(f"\n\nFastest sort: {fastestSortName} sort")
print(f"{fastestSortName} time: {fastestTime:.7f} seconds")

# slowest sort
print(f"\n\nSlowest sort: {slowestSortName} sort")
print(f"{slowestSortName} time: {slowestTime:.7f} seconds")
