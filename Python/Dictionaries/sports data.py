students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}

N = int(input())
for i in range(N):
    key,value = input().split()
    students_dict[key] = value
print(students_dict)
