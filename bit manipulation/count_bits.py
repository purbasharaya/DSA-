# for n we need to return an array with number of 1 bits from 0 to n
# for example
# n = 5  output = [0, 1, 1, 2, 1, 2]
# explanation => 
# 0 --> 000 --> 0
# 1 --> 001 --> 1
# 2 --> 010 --> 1
# 3 --> 011 --> 2
# 4 --> 100 --> 1
# 5 --> 101 --> 2

# so we can use the same concept as we used in counting number of 1 bits because obviously we're doing the same thing!

# for every element from 0 to 5 i.e. 6 elements we'll run a loop
# which will keep shifting ans[i>>1] and adding i&1

def countBits(n):
    ans = [0]*(n+1)  # answer array
    for i in range(1, n+1):  # 1 to (n+1) because there is not 1 bit in zero
        ans[i] = ans[i>>1] + (i&1)

    return ans
