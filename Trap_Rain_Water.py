# Daily Programming Challenge 2024 : Day 7
# Trapping Rain Water
'''
You are given an array height[] of non-negative integers where each element represents the height of a bar in a histogram-like structure. 
These bars are placed next to each other, and the width of each bar is 1 unit. 
When it rains, water gets trapped between the bars if there are taller bars on both the left and right of the shorter bars. 
The task is to calculate how much water can be trapped between these bars after the rain.
'''

def cal_water(arr):
    n = len(arr)
    if n < 3:
        return 0
    left = [0] * n
    right = [0] * n
    water = 0
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], arr[i])
    right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], arr[i])

    for i in range(n):                              # Calculate the water trapped
        water += min(left[i], right[i]) - arr[i]

    return water
    return
arr = input("height[] = ")                                          
arr = list(map(int, arr.strip('[]').split(',')))
water = cal_water(arr)
print(water)