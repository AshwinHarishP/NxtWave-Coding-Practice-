try:
    A,B = map(int,input().split())
    C = A/B
    print(C)
except ValueError:
    print("Input should be an integer")
except ZeroDivisionError:
    print("Denominator can't be 0")
    
