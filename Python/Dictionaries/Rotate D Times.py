def conv_str_to_int(numbers):
    int_list=[]
    for elements in numbers:
        digits=int(elements)
        int_list.append(digits)
    return int_list
        
def rotate(int_list,rotate_times):
    times = len(int_list)%rotate_times
    first_part = int_list[:times]
    second_part = int_list[times:]
    #first_part.extend(second_part)
    return first_part
        
        
        
numbers = input().split(",")
rotate_times = int(input())
int_list = conv_str_to_int(numbers)
rotated_list = rotate(int_list,rotate_times)
print(rotated_list)
