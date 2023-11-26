S=input()
first_word="z"
last_word="a"
word=""

for characters in range(len(S)):
    letters=S[characters]
    if letters!=" ":
        word+=letters
    if letters==" " or characters==len(S)-1:
        if word.lower()<first_word.lower():
            first_word=word
        if word.lower()>last_word.lower():
            last_word=word
        word=""

first_word_and_last_word=first_word+" "+last_word
print(first_word_and_last_word)
        