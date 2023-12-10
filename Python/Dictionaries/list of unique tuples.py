def conv_str_to_int(inputs):
    int_list = []
    for elements in inputs:
        digits = int(elements)
        int_list.append(digits)
    return int_list


N = int(input())
numbers_list=[]
for elements in range(N):
    inputs = input().split()
    int_list = conv_str_to_int(inputs)
    set_list = set(int_list)
    if len(int_list)==len(set_list):
        int_list=list(int_list)
        numbers_list+=[int_list]
print(numbers_list)
    
    
    
