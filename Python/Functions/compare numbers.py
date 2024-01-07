def compare_numbers(first_number, second_number):
    is_greater_than_100 = first_number>100 and second_number>100
    is_less_than= first_number<second_number
    
    if is_greater_than_100 and is_less_than:
        return(bool(1))
    else:
        return(bool(0))
    

first_number = int(input())
second_number = int(input())

is_true = compare_numbers(first_number,second_number)
print(is_true)
