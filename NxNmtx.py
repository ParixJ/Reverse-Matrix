# Input to get N for NxN matrix
n = int(input('Enter n for n-dimentional matrix : '))

# Create blank NxN matrix :
matrix = [[0] * n for i in range(n)]

left,right,top,botton = 0,n,0,n
l = len(matrix)
h = 1

# Fills the matrix in reverse :
for i in range(n):

    # To get negative i-1th index in the array
    j = i-(i *2) -1

    for k in range(n):
        if k == 0:
            matrix[j][k-1] = h
        else:
            matrix[j][k-(k *2) -1] = h
        h += 1

# Print the matrix : (The fist number in the matrix will be the square of N)
print(matrix,'\n\n')

# Iterate the matrix as it is column and row wise :
def iterate(matrix):
    for i in range(l):
        for j in range(l):
            print(matrix[i][j],'  ',end='')
        print()

# Iterate the matrix in reverse :
def iterate_reverse(matrix):
    for i in range(l):
        if i == 0:
            j = i - 1 
        else :
            j = i - (i * 2) - 1
        for k in range(l):
            print(matrix[j][k - (k * 2) - 1],' ',end='')
        print()

print(iterate(matrix),'\n\n')
print(iterate_reverse(matrix))