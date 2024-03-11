def factors_of_n(number):
    factors=""
    for numbers in range(1,number+1):
        if number%numbers==0:
            factors+=str(numbers)+" "
    return factors
    
number = int(input())
result = factors_of_n(number)
print(result)
