import math



def linearSearch(array, needle):
    """linear search
        complexity : O(n)
    """
    
    for item in array:
        if item == needle:
            return True

    return False



def binarySearch(array, needle):
    """binary search
        complexity : O(log n)
    """
    
    low = 0
    high = len(array)

    while low < high:
        medium = math.floor(low + (high - low) / 2)
        value = array[medium]

        if value == needle:
            return True
        elif value > needle:
            high = medium
        else:
            low = medium + 1
    return False
