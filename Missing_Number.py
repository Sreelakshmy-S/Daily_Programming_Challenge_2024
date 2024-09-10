# Daily Programming Challenge 2024 : Day 2
# Find the missing number
'''
You are given an array arr containing n-1 distinct integers. 
The array consists of integers taken from the range 1 to n, meaning one integer is missing from this sequence. 
Your task is to find the missing integer.
'''

arr = input()                                           # arr is the input array of size n-1
arr = list(map(int, arr.strip('[]').split(',')))
n = len(arr) + 1                                        # n (array size+1)
total = n * (n+1) / 2                                   # Calculates total : sum of the first n integers
sum = 0
for i in range (0,len(arr)):                            # Iterate through loop and find sum of all array elements
    sum = sum + arr[i]
print(int(total-sum))                                   # The difference between the total sum and the sum of array elements gives us the missing element

# Time Complexity: Since we only traverse through the array once, we have linear time complexity. O(n)
# Space Complexity: No extra data structures are used other than the exisiting array and a few variables with fixed space. O(1)
