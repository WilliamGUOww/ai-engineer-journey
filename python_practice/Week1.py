# dict

students = {
    "Alice": 95,
    "Bob": 88,
    "Charlie": 92
}

for key in students:
    print(key)

total = 0
for value in students.values():
    total += value
    
average = total / len(students)

max_student= ""
max_score = 0
for key, value in students.items():
    if value > max_score:
        max_student = key
        max_score = value
        
print("Average:", average)
print("Top Student:", max_student)
print("Top Score:", max_score)