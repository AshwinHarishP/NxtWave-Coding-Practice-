import datetime
u = int(input())
start_year = datetime.datetime(1970,1,1)
seconds = datetime.timedelta(seconds=u)
year = start_year+seconds
print(year)
