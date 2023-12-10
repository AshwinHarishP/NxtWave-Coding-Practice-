def get_dictionary_items(input_string):
    dictionary_items = dict()
    for elements in input_string:
        string_values = elements.split(":")
        key = string_values[0]
        value = int(string_values[1])
        if key in dictionary_items:
            total = value+dictionary_items[key]
            dictionary_items[key] = total
        else:
            dictionary_items[key] = value
    return dictionary_items
        

input_string = input().split(",")
dictionary_items = get_dictionary_items(input_string)
dictionary_items = sorted(dictionary_items.items())
print(dictionary_items)
