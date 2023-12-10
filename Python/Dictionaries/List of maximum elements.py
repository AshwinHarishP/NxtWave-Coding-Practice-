def conv_str_to_int(inputs):
    int_inputs =[]
    for elements in inputs:
        digits = int(elements)
        int_inputs.append(digits)
    return int_inputs

N = int(input())
max_list=[]
for _ in range(N):
    inputs = input().split()
    int_inputs = conv_str_to_int(inputs)
    max_input=max(int_inputs)
    max_list.append(max_input)
print(max_list)


    
