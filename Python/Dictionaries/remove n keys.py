alphabets = {
    'a': 97,
    'b': 98,
    'c': 99,
    'd': 100,
    'e': 101,
    'f': 102,
    'g': 103,
    'h': 104,
}
alphabets_1 = alphabets.copy()
keys_input = input().split()
for keys in alphabets_1:
    if keys in keys_input:
        del alphabets[keys]
print(alphabets)
