from datetime import datetime,timedelta
start_date = input()
end_date = input()

formated_value = "%b %d %Y"
formated_string_1 = datetime.strptime(start_date,formated_value)
formated_string_2 = datetime.strptime(end_date,formated_value)

Range = (formated_string_2 - formated_string_1).days

for i in range(Range):
    dates = start_date+timedelta(days=i)
    print(dates)
