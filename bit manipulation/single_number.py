# hashmap approach

def singleNumber(nums):
    hashmap = {}

    for i in nums:
        hashmap[i] = hashmap.get(i, 0) + 1
    for k, v in hashmap.items():
        if v == 1:
            return k
    return -1

# bitwise approach
# we know that 
# 1 xor 1 = 0
# 1 xor 0 = 1
# for example nums = [1, 1, 2, 5, 5]
# (1^1)^2^(5^5) = 2

def singleNumber(nums):
    ans = 0
    for i in range(len(nums)):
        ans ^= nums[i]

    return ans