from katas.isPalindrome import isPalindrome

def test_is_palindrome():
    """
    technique: two pointers
    """
    resultPalindrome = isPalindrome("A man, a plan, a canal: Panama")
    assert resultPalindrome == True