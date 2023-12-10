def print_lower_triangle(m,matrix):
    for i in range(m):
        lower_triangle = []
        
        for j in range(i+1):
            lower_triangle.append(matrix[i][j])
        print(lower_triangle)

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

lower_triangle = print_lower_triangle(m,num_list)
