def calculate_bill(amount):
    if amount<500:
        discount=float((5/100)*amount)
        discount=amount-discount
        
    elif amount>=500 and amount<2500:
        discount=float((10/100)*amount)
        discount=amount-discount
    
    else:
        discount=float((20/100)*amount)
        discount=amount-discount
    return discount

bill_amount = int(input())
result=calculate_bill(amount=bill_amount)
print(result)
