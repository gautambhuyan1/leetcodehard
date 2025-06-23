# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

def inputMatrix():
    """
    Reads a matrix from standard input.
    The first line contains two integers, m and n, representing the number of rows and columns.
    The next m lines contain n integers each, representing the matrix elements.
    """
    m, n = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(m)]
    return matrix


def maximumSquare(matrix): 

    m = len(matrix)
    n = len(matrix[0])

    #print("m, n", m, n)

    maximumSum = 0
    currentSum = 0
    k = 0
    j = 0
    ax = ay = bx = by = 0

    for i in range(m):
        for j in range(n):
            currentSum = 0
            if matrix[i][j] == 1:
                currentSum = currentSum + 1
                k = 0
                l = 0
                while (j + k) < n and matrix[i][j + k] == 1:
                    k = k + 1
        
                while (i + l) < m and matrix[i + l][j] == 1:
                    l = l + 1

                #print("i, j, k, l, maximumSum", i, j, k, l, maximumSum)
        

                if l > k:
                    maxDepth = l
                    for p in range(k):
                        x = 0
                        while (i + x) < m and matrix[i + x][j + p] == 1:
                            x = x + 1
                        if x < maxDepth:
                            maxDepth = x
                        currentSum = (p + 1) * maxDepth
                        if currentSum > maximumSum:
                            ay = i
                            ax = j
                            by = i + maxDepth
                            bx = j + p
                            maximumSum = currentSum
                else:
                    maxDepth = k
                    for p in range(l):
                        x = 0
                        while (j + x) < n and matrix[i + p][j + x] == 1:
                            x = x + 1
                        if x < maxDepth:
                            maxDepth = x
                        currentSum = (p + 1) * maxDepth
                        if currentSum > maximumSum:
                            ay = i
                            ax = j
                            by = i + p
                            bx = j + maxDepth
                            maximumSum = currentSum
                         
    print("Maximum square sum: ax, bx, ay, by", maximumSum, ax, bx, ay, by)
    return maximumSum
                
                


mat = inputMatrix()

print("Matrix:", mat)

maximumSquare(mat)
