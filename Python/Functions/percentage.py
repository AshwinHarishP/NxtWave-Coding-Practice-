def calculate_percentage(number):
    if number<1000:
        percentage=(5/100)*number
    else:
        percentage=(10/100)*number
    return percentage


number = int(input())
result = calculate_percentage(number)
print(result)
