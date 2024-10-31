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
        
        print(f"half is {medium}")
        value = array[medium]

        if value == needle:
            return True
        elif value > needle:
            high = medium
        else:
            low = medium + 1
    return False

def main():
    
    arr = [*range(1,10, 1)]
   
    
    print(arr, ',dsqofdqsd')
    a_binary_search = binarySearch(arr, 2)
    print(a_binary_search)
    # print(a_binary_search)
# if __name__ == 'main':
#     main()

main()