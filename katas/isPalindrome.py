def isPalindrome(us):
    """
    :type s: str
    :rtype: bool
    """

    removeSpaces = us.replace(" ","")
    removeCommas = removeSpaces.replace(",", "")
    s = removeCommas.replace(":", "")
    
    start = 0
    end = len(s) - 1

    while(start < end):
        if s[start].lower() != s[end].lower():
            return False
        start+=1
        end-=1

    return True
