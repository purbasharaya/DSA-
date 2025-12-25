# we need to count the number of 1's in the binary representation of n

# eg: n = 5
# binary representation = 1010
# output = 2 since there are 2 ones

# we use the concent of AND operator
# 1 & 1 = 1
# 1 & 0 = 0

# n & 1 ==> this will check the last bit of n
# if last bit of n = 1, we increase the counter
# n >> 1 ==> this will push the bits to the right

# lets code!

def hammingWeight(n):
    count = 0

    while n:
        count += n & 1
        n >>= 1

    return count