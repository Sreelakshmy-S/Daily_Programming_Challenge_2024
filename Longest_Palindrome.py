# Daily Programming Challenge 2024 : Day 13
# Longest Palindromic Substring
'''
You are given a string s. 
Your task is to find and return the longest palindromic substring within the given string. 
A palindrome is a string that reads the same forwards and backwards
'''
def palindrome(s):
    if len(s)==0:
        return ""
    def check(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    start, end = 0, 0

    for i in range(len(s)):
        len1 = check(s, i, i)
        len2 = check(s, i, i + 1)
        max_len = max(len1, len2)

        if max_len > (end - start):
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    pal = s[start:end + 1]
    return pal
s = input()
s = s.strip('""')
print('"' + palindrome(s) + '"')