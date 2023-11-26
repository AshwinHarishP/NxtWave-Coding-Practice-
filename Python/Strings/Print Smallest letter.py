S=input()
smallest_value=ord(S[0])
for letters in S:
    unicode_value=ord(letters)
    if(unicode_value<smallest_value):
        smallest_value=unicode_value
print(chr(smallest_value))