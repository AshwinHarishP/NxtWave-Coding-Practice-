def replace_old_value_with_new_value(m,n,matrix, old_value, new_value):
    updated_list = []
    for i in range(m):
        List = []
        for j in range(n):
            if matrix[i][j] == old_value:
               matrix[i][j] = new_value
            List.append(matrix[i][j])
        print(List)

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

values = input().split()
old_value, new_value = convert_string_to_int(values)

replaced_value = replace_old_value_with_new_value(m,n,num_list, old_value, new_value)

