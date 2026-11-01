
import time
from dataset import small_benchmark_list, large_sorted_numbers, large_unsorted_numbers
def bubble_sort(arr):
    arr = arr.copy()
    comparisons = 0
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, comparisons
def optimized_bubble_sort(arr):
    arr = arr.copy()
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
def insertion_sort(arr):
    arr = arr.copy()
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr, comparisons
def merge(left, right):
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy(), 0
    mid = len(arr) // 2
    left, count1 = merge_sort(arr[:mid])
    right, count2 = merge_sort(arr[mid:])
    merged = []
    i = 0
    j = 0
    comparisons = count1 + count2
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, comparisons
print("--- Test 1: Small List (20 elements) ---")
a, c1 = bubble_sort(small_benchmark_list)
b, c2 = insertion_sort(small_benchmark_list)
c, c3 = merge_sort(small_benchmark_list)
print("Bubble Sort:", c1, "comparisons")
print("Insertion Sort:", c2, "comparisons")
print("Merge Sort:", c3, "comparisons")
print()
print("--- Test 2: Large Unsorted List (2,000 elements) ---")
start = time.perf_counter()
bubble_sort(large_unsorted_numbers)
bubble_time = time.perf_counter() - start
start = time.perf_counter()
insertion_sort(large_unsorted_numbers)
insertion_time = time.perf_counter() - start
start = time.perf_counter()
merge_sort(large_unsorted_numbers)
merge_time = time.perf_counter() - start
print("Bubble Sort:", round(bubble_time, 4), "seconds")
print("Insertion Sort:", round(insertion_time, 4), "seconds")
print("Merge Sort:", round(merge_time, 4), "seconds")
print()
print("--- Test 3: Already Sorted List (2,000 elements) ---")
start = time.perf_counter()
optimized_bubble_sort(large_sorted_numbers)
bubble_time = time.perf_counter() - start
start = time.perf_counter()
insertion_sort(large_sorted_numbers)
insertion_time = time.perf_counter() - start
start = time.perf_counter()
merge_sort(large_sorted_numbers)
merge_time = time.perf_counter() - start
print("Optimized Bubble:", round(bubble_time, 4), "seconds")
print("Insertion Sort:", round(insertion_time, 4), "seconds")
print("Merge Sort:", round(merge_time, 4), "seconds")
print()
print("Conclusion:")
print("Merge Sort is usually faster on large unsorted lists.")
print("Insertion Sort works well on already sorted lists.")
print("Optimized Bubble Sort stops early when no swaps are needed.")
