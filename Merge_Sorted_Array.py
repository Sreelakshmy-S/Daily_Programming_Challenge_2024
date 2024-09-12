# Daily Programming Challenge 2024 : Day 4
# Merge two sorted arrays without using extra space
'''
You are given two sorted arrays arr1 of size m and arr2 of size n.
Your task is to merge these two arrays into a single sorted array without using any extra space (i.e., in-place merging). 
The elements in arr1 should be merged first, followed by the elements of arr2, resulting in both arrays being sorted after the merge.
'''
def calc_gap(gap):                                                       # Gap is initially large ans then slowly converges
    if gap<=1:
        return 0    
    return (gap//2) + (gap%2)

def sort(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    gap = calc_gap(m+n)

    while gap>0:                                                          # Compare the elements in arr1
        i=0 
        while i + gap < m:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i+=1

        j = max(0, gap - m)
        while i < m and j < n:                                            # Compare elements in both arr1 and arr2 and swap if arr1[i]>arr2[i]
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1

        if j < n:                                                         # Compare the elements in arr2
            j = 0
            while j + gap < n:
                if arr2[j] > arr2[j + gap]:
                    arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
                j += 1

        gap = calc_gap(gap)                                               # Update the gap (reduce)


arr1 = input("arr1 = ")                                          
arr1 = list(map(int, arr1.strip('[]').split(',')))
arr2 = input("arr2 = ")                                          
arr2 = list(map(int, arr2.strip('[]').split(',')))

sort(arr1,arr2)
print("arr1 =",arr1)
print("arr2 =",arr2)