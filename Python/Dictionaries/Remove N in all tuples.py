def removed_tuple_element(element,N):
    new_tuple = []
    for characters in element:
        if characters != N:
            new_tuple.append(characters)
    return tuple(new_tuple)


num_list = [(1, 2, 3, 4, 5, 6), (2, 4, 6, 8), (1, 3, 5, 7)]
N = int(input())

List = []
for tuple_a in range(len(num_list)):
    element = num_list[tuple_a]
    removed_element = removed_tuple_element(element,N)
    List.append(removed_element)
print(List)
