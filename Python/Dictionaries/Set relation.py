def operation(num_set_2):
    for characters in range(len(num_set_2)):
        num_set_2[characters]=int(num_set_2[characters])
    return num_set_2
    
def check(num_set_1):
    Check=operation(num_set_2)
    if num_set_1.issuperset(num_set_2):
        return("Superset")
    elif num_set_1.issubset(num_set_2):
        return("Subset")
    else:
        return("Disjoint Set")
    
num_set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
num_set_2=input().split()
result=check(num_set_1)
print(result)
