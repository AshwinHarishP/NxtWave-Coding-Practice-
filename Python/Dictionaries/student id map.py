def student_details_conv(value_list,key_list):
    student_dict = dict()
    length = len(key_list)
    for i in range(length):
        values = value_list[i]
        keys = key_list[i]
        student_dict[values] = keys
    return student_dict


Ni = input().split(",")
Di = input().split(",")

student_details = student_details_conv(Ni,Di)
student_details = student_details.items()
student_details = sorted(student_details)

for item in student_details:
    print(*item)
