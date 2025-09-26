# 1 - Two Sum 
# problem 01 

# two sum mean the target element match the index in array 
# [ 2,3,4,7,2,] target = 6 
# index is [0 , 2 ]  

'''Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].'''



def twoSum(nums,target):
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found

nums = [2,3,4,7,2]
target = 6
print(twoSum(nums,target))