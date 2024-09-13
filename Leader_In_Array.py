# Daily Programming Challenge 2024 : Day 5
# Find the Leaders in an Array
'''
You are given an integer array arr of size n. 
An element is considered a leader if it is greater than all the elements to its right. 
Your task is to find all such leader elements in the array.
'''
def find_leaders(arr):
    n = len(arr)
    leaders = []
    
    last_element = arr[-1]                              # The last element is always present in the leader array
    leaders.append(last_element)
    
    for i in range(n-2, -1, -1):                        # Move from the second last element to the first element
        if arr[i] >= last_element:
            leaders.append(arr[i])
            last_element = arr[i]                       # last_element replaced with the largest element from right(last)
    
    leaders.reverse()
    return leaders

arr = input()                                           # arr is the input array of size n
arr = list(map(int, arr.strip('[]').split(',')))
leader_arr = find_leaders(arr)                          # calls function to find leaders of array
print(leader_arr)

# Time Complexity : O(n)    [we traverse the array exactly once from right to left]
# Space Complexity : O(n)   [worst case: when all elements are leaders]