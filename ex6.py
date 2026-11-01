
numbers = [38, 27, 43, 3, 9, 82, 10]
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
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged
def merge_sort(arr, level=0):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    space = "  " * level
    print(space + "Split:", left, "and", right)
    sorted_left = merge_sort(left, level + 1)
    sorted_right = merge_sort(right, level + 1)
    result = merge(sorted_left, sorted_right)
    print(space + "Merged:", result)
    return result
print("Initial list:", numbers)
print()
result = merge_sort(numbers)
print()
print("Final sorted list:", result)
