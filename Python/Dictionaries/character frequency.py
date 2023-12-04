string = input().lower()
new_string = set(string)
new_string.discard(" ")
new_string = list(new_string)
for characters in sorted(new_string):
    Count = string.count(characters)
    print("{}: {}".format(characters,Count))
