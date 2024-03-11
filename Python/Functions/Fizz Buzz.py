def fizz_buzz(number):
    if number%5==0 and number%3==0:
        sentence="FizzBuzz"
    elif number%5==0:
        sentence="Buzz"
    
    elif number%3==0:
        sentence="Fizz"
    else:
        sentence=number
    return sentence

number = int(input())
result=fizz_buzz(number)
print(result)
