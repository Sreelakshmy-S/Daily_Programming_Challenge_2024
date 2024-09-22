# Daily Programming Challenge 2024 : Day 14
# Count Substrings with Exactly K Distinct Characters
'''
You are given a string s of lowercase English alphabets and an integer k. 
Your task is to count all possible substrings of s that contain exactly k distinct characters.
'''
def count_distinct_sub(s, k):
    from collections import defaultdict
    
    def at_most_k_distinct(s, k):
        n = len(s)
        result = 0
        char_count = defaultdict(int)
        left = 0
        for right in range(n):
            if char_count[s[right]] == 0:
                k -= 1
            char_count[s[right]] += 1
            while k < 0:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    k += 1
                left += 1
            result += right - left + 1
        return result
    
    # Count substrings with at most k distinct characters
    at_most_k = at_most_k_distinct(s, k)
    # Count substrings with at most k-1 distinct characters
    at_most_k_minus_1 = at_most_k_distinct(s, k - 1)
    
    # The number of substrings with exactly k distinct characters is the difference
    return at_most_k - at_most_k_minus_1

# Example usage
s = input("s = ").strip('""')
k = int(input("k = "))
num = count_distinct_sub(s, k)
print(num)
