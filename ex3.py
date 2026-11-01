numbers = [29, 10, 14, 37, 13]
arr = numbers.copy()
shifts = 0
print("Initial list:", arr)
print()
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        shifts += 1
        j -= 1
    arr[j + 1] = key
    print("Step", i, "(insert", key, "):", arr)
print()
print("Sorted list:", arr)
print("Total shifts:", shifts)

