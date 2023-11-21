from datetime import datetime
year_A,year_B = input().split()
monday = 0
months = range(1,13)

for years in range(int(year_A),int(year_B)+1):
    for month in months:
       formated_date_object = datetime(years,month,1)
       formated_date = formated_date_object.strftime("%A")
       
       if formated_date =="Monday":
           monday+=1
print(monday)
