# we are given an integer and we need to reverse its bits and return the new integer
# for example
# n = 6 (binary representation: 110)
# output-> 3 (011)

# so think about what we can do
# we can take the LSB i.e. least significant bit and add it to our result from right
# we can shift result bits to left to make space for new bit
# and shift n one bit right so that we can keep processing the last bit

def reverseBits(n):
    result = 0
    for _ in range(32): # because the que guarntees us of max 32 bits
        bit = n & 1   # extracting the lsb
        result = (result << 1) | bit   # shifting result to left and adding new bit
        n >>= 1   # shifting n to right 

    return result

# n & 1 gives the last bit of n
# result << 1 shifts result 1 bit to the left
# | is bitwise OR, "(result << 1) | bit" adds bit to result's right

# lets dryrun n = 6 so that we understand better
# iteration   n    bit   result   
# start       110  0     000
# 1           110  0     000
# 2           011  1     001
# 3           001  1     011

# result is 011 = 3