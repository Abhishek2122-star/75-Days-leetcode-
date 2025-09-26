# 217 - contains duplicate 

# problem 02


# the code is for find duplicate nunmbers in array 

# there are three approch to solve this problem 
# approach - try to comapare with the next number 
# approach - we can solve using sorting ...
# approach - using hashset we can solve it 


def contain_duplicate(nums):
    hashset = set()
    for i in nums :
        if i in hashset :
            return True 
        hashset.add(i)
    return False    

nums = [ 2,3,4,9]
print(contain_duplicate(nums))
        



# for finding the exact number are duplicates in given array 
# same hashset approach 

def contain_duplicates(nums):
    hashset = set()
    duplicate = set()

    for i in nums :
        if i in hashset:
            duplicate.add(i)
        else:
            hashset.add(i)
    return list(duplicate)

nums = [ 2,3,4,3,2,1,6,7]
print(contain_duplicates(nums))