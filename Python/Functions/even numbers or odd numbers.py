def show_numbers(number):
    
    for limit in range(number+1):
        if limit%2==0:
            print(str(limit)+" EVEN")
        else:
            print(str(limit)+" ODD")

number = int(input())
show_numbers(number)
