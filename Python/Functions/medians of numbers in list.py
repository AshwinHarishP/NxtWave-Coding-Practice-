def median(numbers):
    count=0
    for digits in range(len(numbers)):
        numbers[digits]=int(numbers[digits])
        count+=1
    sorted_numbers=sorted(numbers)
    if count%2==0:
        
        middle_value=(len(sorted_numbers)//2)-1
        Median=(sorted_numbers[middle_value]+( (sorted_numbers[middle_value+1])) )/2
        return Median
    else:
        middle_value=len(sorted_numbers)//2
        Median=sorted_numbers[middle_value]
        return Median
        
    
    
numbers=input().split(",")
result=median(numbers)
print(result)
