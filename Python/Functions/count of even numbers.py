def get_even_numbers_count(numbers):
    count=0
    numbers=numbers.split()
    for digits in numbers:
        if int(digits)%2==0:
            count+=1
    return count

numbers = input()
result = get_even_numbers_count(numbers)
print(result)
