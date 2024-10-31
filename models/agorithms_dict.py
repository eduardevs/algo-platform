from enum import Enum

class BigOComplexity(Enum):
    CONSTANT = 'O(1)',
    LINEAR = 'O(N)',
    QUADRATIC = 'O(N^2)',
    LOGARITHMIC = 'O(logN)',
    LOG_LINEAR = 'O(NlogN)',
    CUBIC = 'O(n^3)',
    EXPONENTIAL = 'O(2^n)',
    FACTORIAL = 'O(n!)'
    
    


algorithms_dict = {
    'linear_search': BigOComplexity.LINEAR,
    'binary_search': BigOComplexity.LOGARITHMIC,
    'bubble_sort': BigOComplexity.QUADRATIC
}


"""
  print("linear_search", "linear search" in algorithms)
"""