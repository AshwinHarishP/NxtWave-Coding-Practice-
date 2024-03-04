def count_the_vowels(word):
    count=0
    vowels="aeiou"
    for letters in word:
        if letters.casefold() in vowels.casefold():
            count+=1
    return count

word = input()
vowels_count=count_the_vowels(word)
print(vowels_count)
