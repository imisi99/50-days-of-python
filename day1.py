import math

def divide_or_square(x: int):
    if x % 5 == 0:
        return math.sqrt(x)
    else:
        return x % 5
    
print(divide_or_square(10))