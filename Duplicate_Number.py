# Daily Programming Challenge 2024 : Day 3
# Find the duplicate number
'''
You are given an array arr containing n+1 integers, where each integer is in the range [1, n] inclusive.
There is exactly one duplicate number in the array, but it may appear more than once. 
Your task is to find the duplicate number without modifying the array and using constant extra space.
'''

def find_duplicate(arr):
    slow = arr[0]
    fast = arr[0]

    while True:                                         # We use the slow and fast pointer method used to find loops to find the duplicate elemet
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    slow = arr[0]
    while slow!= fast:                                  # Ensures that the duplicate element is returned, not where slow and fast pointers meet
        slow = arr[slow]
        fast = arr[fast]
        
    return fast

arr = input()                                           # arr is the input array of size n+1
arr = list(map(int, arr.strip('[]').split(',')))
duplicate = find_duplicate(arr)
print(duplicate)

# We only use constant extra space (i.e. slow and fast variables) independant of the input size. 
# Therefore Space Complexity is O(1)

# Time Complexity : O(n)
# Atmost both of the pointers will move 'n' places since the size of the array is n. They'll meet within one cycle of he array.