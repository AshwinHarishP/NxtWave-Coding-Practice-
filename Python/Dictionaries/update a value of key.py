students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket",
    "Deepak": "Boxing"
}

input_key ,input_value = input().split()
students_dict[input_key] = input_value
print(students_dict)
