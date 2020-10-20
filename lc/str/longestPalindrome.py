
'''
# 5. Longest Palindromic Substring
Medium

8352

586

Add to List

Share
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
'''

def longestPalindrome(s):
    memo = {}
    def dp(l,r):
        nonlocal memo
        if l == r:
            return s[l]
        
        # memo dict
        key = (l,r)
        if key in memo:
            return memo[key]
        res = None
        
        # format str to left and right
        temp = s[l:r]
        if temp == temp[::-1]:
            return temp
        else:
            # curr string is not pal            
            a = dp(l+1,r)
            b = dp(l,r-1)
            if len(a) > len(b):
                res = a
            else:
                res = b
        memo[key] = res
        return memo[key]
    # base case, if input string is pal
    if s == s[::-1]:
        return s
    return dp(0,len(s))


print(longestPalindrome("abb"))
