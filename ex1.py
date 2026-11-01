
numbers = [64, 34, 25, 12, 22, 11, 90]
arr = numbers.copy()
comparisons = 0
swaps = 0
print("Initial list:", arr)
print()
for i in range(len(arr) - 1):
    for j in range(len(arr) - 1 - i):
        comparisons += 1
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swaps += 1
    print("Pass", i + 1, ":", arr)
print()
print("Sorted list:", arr)
print("Total comparisons:", comparisons)
print("Total swaps:", swaps)
