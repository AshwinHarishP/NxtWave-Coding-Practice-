S=input()
N=int(input())
count=0
for letters in S:
    if(ord(letters)==N):
       count+=1
print(count)
