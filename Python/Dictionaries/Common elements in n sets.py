def conv_str_to_int(list_a):
    new_list=[]
    for elements in list_a:
        digits=int(elements)
        new_list.append(digits)
    return new_list
    
def get_intersection(num_set_list):
    result=num_set_list[0]
    for num_set in num_set_list:
        result=result.intersection(num_set)
    return result
N=int(input())
num_set_list=[]
for i in range(N):
    values_list = input().split()
    values_list = conv_str_to_int(values_list)  #function call
    values_list=set(values_list)
    num_set_list.append(values_list)

result_set = get_intersection(num_set_list)
result_set=sorted(list(result_set))
print(result_set)
