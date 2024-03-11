def get_first_upper_letter(string):
    for characters in string:
         if characters.isupper():
            upper_character=characters
            break
    return upper_character


string = input()
upper_case_character = get_first_upper_letter(string)
print(upper_case_character)
