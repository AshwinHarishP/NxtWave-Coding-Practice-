num_list = [(2, 4, 6, 8), (5, 15, 25, 35), (7, 14, 21)]

N=int(input())
for i in range(len(num_list)):
    for j in range(len(num_list[i])):
        if N == num_list[i][j]:
            print(str(i)+" "+str(j))

        
