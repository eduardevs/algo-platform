from algorithms.sort import bubble_sort
from algorithms.search.binary_search import binarySearch

def test_bubble_sort():
    
    
    a_bubble_sort = bubble_sort([1,3,2])
    
    assert a_bubble_sort == [1,2, 3]
    
    
def test_binary_search():
    a_binary_search = binarySearch(range(1,10), 2)
    
    assert a_binary_search == True
    