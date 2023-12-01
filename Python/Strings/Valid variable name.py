String=input()
valid=True
for characters in String:
    unicode_chr=ord(characters)
    if not((unicode_chr>=65 and unicode_chr<=90) or (unicode_chr>=97 and unicode_chr<=122) or (unicode_chr>=48 and unicode_chr<=57)):
        valid=False
        break
print(valid)