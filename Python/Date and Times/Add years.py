from datetime import datetime,timedelta

input_string = input()
year = int(input())

formatted = "%b %d %Y"
formatted_string = datetime.strptime(input_string,formatted)
after_N_years = formatted_string + timedelta(days = 365*year)
print(after_N_years)
