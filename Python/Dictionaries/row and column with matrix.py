def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list

def row_matrix(num_list,Maximum_number):
    for elements in num_list:
        if Maximum_number in elements:
             row = elements
    return row
    
def get_transpose_matrix(n,m,num_list):
    transpose_matrix = []
    for i in range(n):
        row = [] 
        for j in range(m):
            row_matrix = num_list[j][i]
            row.append(row_matrix)
        transpose_matrix.append(row)
    return transpose_matrix
    
def get_column_matrix(Maximum_number):
    transpose_matrix = get_transpose_matrix(n,m,num_list)
    for elements in transpose_matrix:
        if Maximum_number in elements:
            column = elements
    return column
    
    

m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

Maximum_number = max(max(num_list))

row = row_matrix(num_list,Maximum_number)
column = get_column_matrix(Maximum_number)
print(row)
print(column)
