# Merge sort is an algorithm that reduces to time complexity of sorting
# from O(n^2) naive approach to a O(nlogn). It uses a divide and conquer
# paradigm to recursively sort subarrays before sorting the main array, 
# reducing the number of times we need to "resort" from n times to logn times

import examples
# merge sort is a function that takes into two sorted arrays, and 
# merges them together and returns that
def merge_sort(l, r):
    ret = []
    l_i = 0
    r_i = 0
    while (l_i < len(l) and r_i < len(r)):
        if l[l_i] < r[r_i]:
            ret.append(l[l_i])
            l_i += 1
        else:
            ret.append(r[r_i])
            r_i += 1
            
    if l_i == len(l):
        ret += r[r_i:]
    else:
        ret += l[l_i:]
        
    return ret

def merge(arr):
    if len(arr) <= 1:
        return arr
    m = len(arr) // 2
    l = merge(arr[0:m])
    r = merge(arr[m:])
    
    return merge_sort(l, r)
        
        
    
if __name__ == '__main__':
    print(merge(examples.arr1))
    print(merge(examples.arr2))
    print(merge(examples.arr3))