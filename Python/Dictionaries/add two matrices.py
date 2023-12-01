def get_add_two_matrices(first_matrix, second_matrix, m, n):
    length = len(first_matrix)
    add_two_matrices = []
    for i in range(m):
        Sum_list = []
        for j in range(n):
            Sum = first_matrix[i][j]+second_matrix[i][j]
            Sum_list.append(Sum)
        add_two_matrices.append(Sum_list)
    return add_two_matrices
        
        
        
def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


def read_matrix_inputs(m):
    num_list = []
    for i in range(m):
        list_a = input().split()
        list_a = convert_string_to_int(list_a)
        num_list.append(list_a)
    return num_list


m, n = input().split()
m, n = int(m), int(n)

first_matrix = read_matrix_inputs(m)
second_matrix = read_matrix_inputs(m)


add_two_matrices = get_add_two_matrices(first_matrix, second_matrix, m, n)

for elements in add_two_matrices:
    print(elements)
