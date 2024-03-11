def check_divisible_by_9(first_number, second_number, third_number):
    is_divisible=( (first_number%9==0) or (second_number%9==0) or (third_number%9==0) )
    return is_divisible
    

first_number = int(input())
second_number = int(input())
third_number = int(input())

is_divisible = check_divisible_by_9(first_number,second_number,third_number)
print(is_divisible)
