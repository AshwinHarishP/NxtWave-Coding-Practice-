def Elements(elements):
    length=len(elements)
    j=0 
    flag=0
    for i in range(len(elements)):
        elements[i]=int(elements[i])
        if elements.count(elements[j])==length:
            flag=1
            break
    if flag==1:
        return("True")
    else:
        return(sorted(list(set(elements))))
    
elements=input().split()
result=Elements(elements)
print(result)
