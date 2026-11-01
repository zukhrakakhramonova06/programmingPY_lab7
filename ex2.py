nearly_sorted = [10, 20, 25, 30, 50, 40, 60, 70]
already_sorted = [5, 15, 25, 35, 45, 55]
print(" Testing nearly_sorted")
arr = nearly_sorted.copy()
print("List:", arr)
passes = 0
for i in range(len(arr) - 1):
    swapped = False
    passes += 1
    for j in range(len(arr) - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    if swapped == False:
        print("Pass", passes, ":", arr,
              "(no swaps, stopping early!)")
        break
    else:
        print("Pass", passes, ":", arr)
print("Optimized passes:", passes,
      "(Standard would take", len(arr) - 1, "passes)")
print("Sorted list:", arr)
print()
print("Testing already_sorted ")
arr = already_sorted.copy()
print("List:", arr)
passes = 0
for i in range(len(arr) - 1):
    swapped = False
    passes += 1
    for j in range(len(arr) - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    if swapped == False:
        print("Pass", passes, ":", arr,
              "(no swaps, stopping early!)")
        break
    else:
        print("Pass", passes, ":", arr)
print("Optimized passes:", passes,
      "(Standard would take", len(arr) - 1, "passes)")
print("Sorted list:", arr)
