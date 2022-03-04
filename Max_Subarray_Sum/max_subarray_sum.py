################################
#
# The Max Subarray Problem is as follows: in an array, we want to find the
# subarray whose sum is the max. The brute force method is to go through 
# all possible sums, which is O(n^2), but how could we improve this. One thing
# can do is again, divide and conquer. This takes advantage of the fact that when 
# we split our problem into subproblems, we reduce the # of searches (in proportion) 
# to the size, from n to logn. Then, we could solve this problem in O(nlogn).
#
################################
from cmath import inf
import examples

# This problem searches for a max_sum, but what if our sum is in between? Meaning 
# that we are searching for the sum on the left and right, but the sum is actually
# right smack in the middle, crossing from our left_sub_array and right_sub_array?
# in actuality, we want to consider the max_crossing as our main sum to check
# Thus: have a max_crossing function in the middle index, and recursively call 
# max_subarray on the left and subarray.
def max_subarray_sum(arr):
    if len(arr) <= 1:
        return arr[0]
    else:
        m = len(arr) // 2
        l = max_subarray_sum(arr[:m])
        r = max_subarray_sum(arr[m:])
        crossing = max_crossing(arr)
        return max(l, r, crossing)

# max_crossing starts at the center index, and branches out to the left and right, finding
# the greatest sum that would include the center index
def max_crossing(arr):
    m = len(arr) // 2
    
    # calculate the greatest the left side sum connected to the middle can be
    left_sum = -1000000000000
    sum = 0
    for i in reversed(range(0, m + 1)):
        sum += arr[i]
        left_sum = max(sum, left_sum)
    
    # calculate the greatest the right side sum connected to the middle can be
    right_sum = -1000000000000
    sum = 0
    for j in range(m + 1, len(arr)):
        sum += arr[j]
        right_sum = max(sum, right_sum)
    
    max_cross_sum = max(left_sum, 0) + max(right_sum, 0)
    
    return max_cross_sum

if __name__ == '__main__':
    print(max_subarray_sum(examples.arr1))
    print(max_subarray_sum(examples.arr2))
    print(max_subarray_sum(examples.arr3))