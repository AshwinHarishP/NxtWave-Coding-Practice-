def Range(list_a,list_b,list_c):

    for i in range(len(list_a)):
        list_a[i]=int(list_a[i])
    list_a=set(list_a)
    

    for j in range(len(list_b)):
        list_b[j]=int(list_b[j])
    list_b=set(list_b)

    for k in range(len(list_c)):
        list_c[k]=int(list_c[k])
    list_c=set(list_c)
    check_1=list_a.intersection(list_b).intersection(list_c)

    return(list(check_1))






list_a=input().split()
list_b=input().split()
list_c=input().split()

result=Range(list_a,list_b,list_c)
print(result)
