list_a = [3, 9, 15, 27]
list_b = [2, 8, 18, 20, 25]
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
print("List A:", list_a)
print("List B:", list_b)
print()
print("Merged result:")
print(merge(list_a, list_b))
print()
print("Test empty list merge:")
print("Merged with empty:", merge([], [1, 2, 3]))
