col, row=map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))

i=0

while i<len(matrix):
    
    j=0
    while j<len(matrix[i]):
        if matrix[i][j]=='.':
            matrix[i][j]=matrix[i-1][j-1].count('*')+matrix[i-1][j].count('*')+matrix[i-1][j+1].count('*')+matrix[i][j-1].count('*')+matrix[i][j+1].count('*')+matrix[i+1][j-1].count('*')+matrix[i+1][j].count('*')+matrix[i+1][j+1].count('*')
            
        print(matrix[i][j], end='')
        j+=1
        
    print()
    i+=1
