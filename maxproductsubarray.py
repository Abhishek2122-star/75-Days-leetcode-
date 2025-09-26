# 152. Maximum Product Subarray

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


def maxproduct(nums):
    max_here = min_here = ans = nums[0]
    for x in nums[1:]:
        if x < 0 :

            max_here, min_here = min_here, max_here
        max_here = max ( x , max_here * x)
        min_here = min ( x , min_here * x)
        ans = max(ans , max_here )
    return ans 
nums = [2,3,-2,4]
print("product of subarray is :", maxproduct(nums))
