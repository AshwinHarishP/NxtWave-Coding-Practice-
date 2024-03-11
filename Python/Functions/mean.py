def mean(numbers):
    Sum=0
    numbers=numbers.split(",")
    for digits in range(len(numbers)):
        numbers[digits]=int(numbers[digits])
        Sum+=numbers[digits]
    length=len(numbers)
    average=Sum/length
    return average
    
    
numbers=input()
result=mean(numbers)
print(result)
