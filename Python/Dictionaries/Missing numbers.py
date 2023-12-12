def conv_int(List_a):
    converted_list = []
    for elements in List_a:
        digits = int(elements)
        converted_list.append(digits)
    return converted_list

def missing_number(converted_list):
    missed_number = []
    last_element = converted_list[-1]
    for i in range(1,last_element+1):
        if i not in converted_list:
            missed_number.append(i)
    return(missed_number)
    

List_a = input().split()

converted_list = conv_int(List_a)
missed_number = missing_number(converted_list)
print(missed_number)
