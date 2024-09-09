# Daily Programming Challenge 2024 : Day 1
# Sort an Array of 0s, 1s, and 2s
'''
You are given an array arr consisting only of 0s, 1s, and 2s. 
The task is to sort the array in increasing order in linear time (i.e., O(n)) without using any extra space.
This means you need to rearrange the array in-place.
'''

def sort(A,n):                                      # Sorting using dutch national flag algortihm
    low = 0
    high = n -1
    mid = 0
    while mid<=high:
        if A[mid]==0:
            A[low], A[mid] = A[mid], A[low]
            low+=1
            mid+=1
        elif A[mid]==1:
            mid+=1
        else:
            A[high], A[mid] = A[mid], A[high]
            high-=1
    return A

A = input()
if A.strip()=="[]":                                # Accounts for empty array (corner case)
    array = []
else:                                              # If array not empty perform sorting
    A = list(map(int, A.strip('[]').split(',')))
    array = sort(A, len(A))
print(array)                                       # Prints the sorted array

# The algorithm runs in linear time complexity O(n)