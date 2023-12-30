def validate_atm_pin_code(pin):
    if ( (len(pin)==4 or len(pin)==6) and pin.isdigit()):
        sentence="Valid PIN Code"
    else:
        sentence="Invalid PIN Code"
    return sentence


word = input()
result=validate_atm_pin_code(pin=word)
print(result)
