from dataset import students, products
students_by_score = students[:]
for i in range(1, len(students_by_score)):
    key = students_by_score[i]
    j = i - 1
    while j >= 0 and students_by_score[j]["exam_score"] < key["exam_score"]:
        students_by_score[j + 1] = students_by_score[j]
        j = j - 1
    students_by_score[j + 1] = key
print("--- Top 3 Students by Exam Score ---")
for i in range(3):
    s = students_by_score[i]
    print(f"{i + 1}. {s['name']} (Score: {s['exam_score']}, GPA: {s['gpa']})")
students_by_name = students[:]
n = len(students_by_name)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if students_by_name[j]["name"] > students_by_name[j + 1]["name"]:
            temp = students_by_name[j]
            students_by_name[j] = students_by_name[j + 1]
            students_by_name[j + 1] = temp
print("\n--- Students Sorted Alphabetically ---")
for i in range(n):
    s = students_by_name[i]
    print(f"{i + 1}. {s['name']} ({s['group']})")
cheap = products[:]
help_list = products[:]
length = len(cheap)
size = 1
while size < length:
    start = 0
    while start < length:
        left_end = start + size
        right_end = start + 2 * size
        if left_end > length:
            left_end = length
        if right_end > length:
            right_end = length
        a = start
        b = left_end
        k = start
        while a < left_end and b < right_end:
            if cheap[a]["price"] <= cheap[b]["price"]:
                help_list[k] = cheap[a]
                a = a + 1
            else:
                help_list[k] = cheap[b]
                b = b + 1
            k = k + 1
        while a < left_end:
            help_list[k] = cheap[a]
            a = a + 1
            k = k + 1
        while b < right_end:
            help_list[k] = cheap[b]
            b = b + 1
            k = k + 1
        start = start + 2 * size
    for x in range(length):
        cheap[x] = help_list[x]
    size = size * 2
print("\n--- Top 3 Cheapest Products ---")
for i in range(3):
    p = cheap[i]
    print(f"{i + 1}. {p['name']} - ${p['price']}")
kamola_pos = 0
madina_pos = 0
for i in range(len(students_by_score)):
    if students_by_score[i]["name"] == "Kamola":
        kamola_pos = i
    if students_by_score[i]["name"] == "Madina":
        madina_pos = i
print("\n--- Stability Check ---")
if kamola_pos < madina_pos:
    print("Kamola appears before Madina: the sort is stable.")
else:
    print("Kamola appears after Madina: the sort is NOT stable.")