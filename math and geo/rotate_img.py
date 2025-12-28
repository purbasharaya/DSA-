# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise)
# Input: matrix = [
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]
# Output: [
# [7,4,1],
# [8,5,2],
# [9,6,3]
# ]

# to achieve a 90 degree rotation we need to do 2 things
# 1-> vertical reversal(flip along the horizontal axis)
#  -->input
# 1  2  3  
# 4  5  6  
# 7  8  9
# --> output
# 7 8 9
# 4 5 6 
# 1 2 3

# 2-> transpose (swap rows and column)
# input (taking transpose of the vertically reversed matrix above)
# 7 8 9
# 4 5 6 
# 1 2 3
# output
# 7 4 1
# 8 5 2
# 9 6 3
# now my matrix is 90 degree rotated 

def rotate_image(matrix):
    edge_length = len(matrix)
    top = 0
    bottom = edge_length - 1

    while top < bottom:
        for  col in range(edge_length):
            matrix[top][col], matrix[bottom][col] = matrix[bottom][col], matrix[top][col] # swapping top with bottom
        
        top += 1 # increasing top count because its coming downwards
        bottom -= 1 # decreasing bottom count because its moving upwards
        # the above loop will work till mid

    for row in range(edge_length):
        for col in range(row+1, edge_length):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    return matrix