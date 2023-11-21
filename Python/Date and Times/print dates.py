from datetime import datetime, timedelta
string = input()
input_date = "%d %b %Y"

today = datetime.strptime(string,input_date)
yestarday = today - timedelta(days=1)
tomarrow = today + timedelta(days=1)
print(yestarday)
print(today)
print(tomarrow)
