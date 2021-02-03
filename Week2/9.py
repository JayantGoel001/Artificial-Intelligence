n = int(input("Enter number of rows and columns:\n"))

print("Enter The values of matrix 1:")
matrix1 = [[]] * n
for i in range(n):
    matrix1[i] = list(map(int, input().split()))


print("Enter The values of matrix 2:")
matrix2 = [[]]*n
for i in range(n):
    matrix2[i] = list(map(int, input().split()))

result = [[0]*n]*n

for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j] += matrix1[i][k]*matrix2[k][j]

print(result)