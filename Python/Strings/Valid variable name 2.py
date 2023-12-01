String=input()
first_letter=String[0]
flag=0
for letters in String:
    if(first_letter.isdigit() or first_letter!=first_letter.isalpha()):
        if(first_letter=="_" or first_letter.isupper() or first_letter.islower()):
            flag=0
        else:
            
            print("False")
            flag=1
            break

if(flag==0): 
    print("True")
    