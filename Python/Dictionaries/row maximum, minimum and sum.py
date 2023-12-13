def maximum_list(num_list):
    List = []
    for elements in num_list:
        maximum_elements = max(elements)
        List.append(maximum_elements)
    return List
    
def minimum_list(num_list):
    List = []
    for elements in num_list:
        minimum_elements = min(elements)
        List.append(minimum_elements)
    return List

def sum_of_each_row_func(num_list):
    List = []
    for elements in num_list:
        minimum_elements =sum(elements)
        List.append(minimum_elements)
    return List

def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

Maximum = maximum_list(num_list)
Minimum = minimum_list(num_list)
sum_of_each_row = sum_of_each_row_func(num_list)
print(Maximum)
print(Minimum)
print(sum_of_each_row)
