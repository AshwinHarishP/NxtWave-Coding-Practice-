def smallest(numbers,k):
    for digits in range(len(numbers)):
        numbers[digits]=int(numbers[digits])
    sorted_numbers=sorted(numbers)
    kth_element=sorted_numbers[k-1]
    return kth_element
    
numbers=input().split(",")
k=int(input())
result=smallest(numbers,k)
print(result)
