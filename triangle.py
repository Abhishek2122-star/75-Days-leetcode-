# 611. Valid Triangle Number
# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3

# this is an brute force solution 

def validtriangle(nums):
    n = len(nums)
    count = 0 
    nums.sort()

    for i in range(n):
        for j in range (i + 1 , n):
            for k in range (j + 1 , n):
                if nums[i] + nums[j] > nums[k]:
                    count +=1 
    return count 
nums = [2,2,3,4]
print ( " the maximum triangle number is :", validtriangle(nums))