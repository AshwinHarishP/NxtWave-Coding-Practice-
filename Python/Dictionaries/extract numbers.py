def conv_int(elements):
    List_a=[]
    for characters in elements:
        if characters.isdigit():
            number=int(characters)
            List_a.append(number)
    return List_a
        
    
    
    
    
elements=input().split(",")
result=conv_int(elements)
print(result)
    
