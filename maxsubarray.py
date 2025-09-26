# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


def maxsubarray(nums):
    maxsub = nums[0]
    currsum = 0

    for n in nums:
        if currsum < 0 :
            currsum = 0 
        currsum += n 
        maxsub = max(maxsub,currsum)
    return maxsub

nums = [5 , 4 ,-1 , 7 , 8 ]
print("the max sub array is :" , maxsubarray(nums) )