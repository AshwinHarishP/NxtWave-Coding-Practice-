def is_prime(n):
    if (n==1 or n==0):
        return False
    
    for i in range(2,n):
        if (n%i)==0:
            return False
    return True
    


n = int(input())
prime_numbers_list=[]
for i in range(1,n+1):
    if(is_prime(i)):
        prime_numbers_list.append(str(i))
        prime_numbers_sperated_by_space=" ".join(prime_numbers_list)
        
print(prime_numbers_sperated_by_space)
