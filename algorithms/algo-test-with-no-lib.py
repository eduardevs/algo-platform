from search.binary_search import binarySearch, linearSearch

tab = range(1, 10 + 1)

value = 11
"""linear search test"""
linear_search_test = linearSearch(tab, value)
print(f"linear search result is: {linear_search_test}")

"""binary search test
    """

binary_search_test = binarySearch(tab, value)
print(f"binary_search_test result : {binary_search_test}")
