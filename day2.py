def convert_add(array):
    sum = 0
    for val in array:
        val_int = int(val)
        sum += val_int
        
    return sum


print(convert_add(["1", "3", "5"]))
    