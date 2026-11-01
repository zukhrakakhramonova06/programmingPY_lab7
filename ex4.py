names = ["Sardor", "Malika", "Aziz", "Dilnoza", "Jasur", "Kamola"]
new_student = "Bekzod"
print("Initial roster:", names)
print()
arr = names.copy()
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
print("Sorted roster (A-Z):")
print(arr)
print()
arr = names.copy()
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] < key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
print("Sorted roster (Z-A):")
print(arr)
print()
print("Adding new student:", repr(new_student))
arr = names.copy()
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
arr.append(new_student)
key = arr[-1]
j = len(arr) - 2
while j >= 0 and arr[j] > key:
    arr[j + 1] = arr[j]
    j -= 1
arr[j + 1] = key
print("Updated roster (A-Z):")
print(arr)

