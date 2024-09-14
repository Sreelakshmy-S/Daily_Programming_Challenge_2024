# Daily Programming Challenge 2024 : Day 6
# Find All Subarrays with Zero Sum
'''
You are given an integer array arr of size n. 
Your task is to find all the subarrays whose elements sum up to zero. 
A subarray is defined as a contiguous part of the array, and you must return the starting and ending indices of each subarray.
'''
def find_subarray(arr):
    s_arr=[]
    index_dict = {}
    total_sum = 0
    for i in range(len(arr)):
        total_sum += arr[i]                           # Add current element into array
        if total_sum == 0:                            # If sum is zero, then append index                       
            s_arr.append((0, i))
        
        if total_sum in index_dict:                   # If cumulative sum is already found in dictionary
            for start_index in index_dict[total_sum]:
                s_arr.append((start_index + 1, i))
        
        if total_sum in index_dict:                   # Add the current index to the list of indices for this cumulative sum
            index_dict[total_sum].append(i)
        else:
            index_dict[total_sum] = [i]
    
    return s_arr
arr = input()                                           # arr is the input array of size n
arr = list(map(int, arr.strip('[]').split(',')))
sub_array = find_subarray(arr)                         # calls function to find the zero sum sub arrays
print(sub_array)

# Time Complexity : O(n)
# Space Complexity : O(n) (Worst case scenario might be O(n^2) if we consider the soace for storing the result)