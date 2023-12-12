def conv_st_to_int(elements):
    int_elements = []
    for characters in elements:
        digits = int(characters)
        int_elements.append(digits)
    return int_elements 

N=int(input())

max_value_of_first_element =[]
max_value_of_second_element = []

for _ in range(N):
    elements = input().split()
    int_elements = conv_st_to_int(elements)
    max_value_of_first_element.append(int_elements[0])
    max_value_of_second_element.append(int_elements[1])


for i in range(2):
    max_min_list = []
    if i ==0:
        max_min_list.append(max(max_value_of_first_element))
        max_min_list.append(min(max_value_of_first_element))
        print(tuple(max_min_list))
    else:
        max_min_list.append(max(max_value_of_second_element))
        max_min_list.append(min(max_value_of_second_element))
        print(tuple(max_min_list))
