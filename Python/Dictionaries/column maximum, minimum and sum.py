def get_transpose_of_matrix(matrix, m, n):
    transpose_matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row_matrix = num_list[j][i]
            row.append(row_matrix)
        transpose_matrix.append(row)
    return transpose_matrix


def get_print_max_min_sum_for_row_wise(transpose_of_matrix):
    max_list = []
    min_list = []
    sum_list = []
    for elements in transpose_of_matrix:
        max_list.append(max(elements))
        min_list.append(min(elements))
        sum_list.append(sum(elements))
    print(max_list)
    print(min_list)
    print(sum_list)


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

transpose_of_matrix = get_transpose_of_matrix(num_list, m, n)
print_max_min_sum_for_row_wise = get_print_max_min_sum_for_row_wise(transpose_of_matrix)
