list_a = [('apple', 'banana', 'orange', 'grapes'), ('cricket', 'football', 'hockey'), ('car', 'bicycle', 'bus')]
# Write your code here

N=int(input())
List_b = []
for _ in range(N):
    element = input().split()
    first_element = int(element[0])
    second_element = int(element[1])
    element = list_a[first_element][second_element]

    List_b.append(element)
print(List_b)
    
