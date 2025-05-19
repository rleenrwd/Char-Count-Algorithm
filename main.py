
def charCount(str):
    """
    Takes a string and returns an object with counts of each 
    alphanumeric character in the string
    """

    counts = {}
    
    for char in str.lower():
        if char.isalnum():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts
        
print(charCount('Norwood from the netherlands!'))
print(charCount('Hello world'))
print(charCount('9999 python programming'))