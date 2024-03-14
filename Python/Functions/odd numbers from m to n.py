def get_odd_numbers_in_range(start_number, end_number):
    List=[]
    for numbers in range(start_number,end_number+1):
        if (numbers%2)!=0:
            List+=str(numbers)+" "
            List="".join(List)
    return List
    

start_number = int(input())
end_number = int(input())

odd_numbers = get_odd_numbers_in_range(start_number,end_number)

print(odd_numbers)
