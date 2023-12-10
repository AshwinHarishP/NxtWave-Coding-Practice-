def get_consecutive_sum(int_list):
    Sum_list = []
    for elements in range(len(int_list)-1):
        Sum = int_list[elements]+int_list[elements+1]
        Sum_list.append(Sum)
    return Sum_list

def get_consecutive_sum_list(int_list):
    while len(int_list)>1:
        consecutive_sum_list = get_consecutive_sum(int_list)
        print(consecutive_sum_list)
        int_list = consecutive_sum_list
    
    
    
def convert_str_to_int(input_list):
    int_list = []
    for elements in input_list:
        elements = int(elements)
        int_list.append(elements)
    return int_list

input_list = input().split(",")
int_list = convert_str_to_int(input_list)
print(int_list)

consecutive_sum = get_consecutive_sum_list(int_list)
