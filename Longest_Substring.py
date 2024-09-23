# Daily Programming Challenge 2024 : Day 15
# Find the Longest Substring Without Repeating Characters
'''
You are given a string S, and your task is to find the length of the longest substring that contains no repeating characters. A substring is a contiguous block of characters in the string.
In this problem, you need to find the length of the longest substring where all the characters are unique. The substring can be formed by starting at any position in the string, but it must not contain any repeated characters.
'''
def length_of_longest_substring(s: str) -> int:
    char_set = set()                                # To store unique characters
    left = 0                                        # Left pointer for the sliding window
    max_length = 0                                  # To keep track of the maximum length

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])                    # Remove the leftmost character
            left += 1                                   # Move the left pointer to the right
        char_set.add(s[right])                          # Add the current character to the set
        max_length = max(max_length, right - left + 1)  # Update max length

    return max_length

str = input().strip('""')
length = length_of_longest_substring(str)
print(length)

# Time Complexity : O(n)
# Space Complexity : O(min(n+m))