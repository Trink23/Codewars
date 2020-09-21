def get_middle(s):
    charString = [char for char in s]
    lenString = len(s)
    midpoint = lenString / 2
    isEven = lenString % 2
    if (isEven == 0):
        return charString[midpoint - 1] + charString[midpoint]
    else:
        return charString[midpoint]
