from datetime import datetime
string = input()
date_format = "%d %b %Y"
result = datetime.strptime(string,date_format)
print(result)
