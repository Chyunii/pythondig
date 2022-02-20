col, row = map(int, input().split())

matrix=[]

for i in range(row):
    matrix.append(list(input()))



for i in range(row):
    for j in range(col):

        count=0

        if matrix[i][j]=='.':

            for a in range(i-1,i+2):
                for b in range(j-1, j+2):

                    if not(a<0 or b<0 or a>=row or b>=col):
                        if matrix[a][b]=='*':
                            count+=1
                            
            matrix[i][j]=count

            print(matrix[i][j], end='')

        else :
            print(matrix[i][j], end='')

    print()
