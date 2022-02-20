col, row=map(int, input().split())        # 가로, 세로


matrix = []

for i in range(row):                      # 반복. row값이 3이면 그냥 3번 반복한다는 뜻

    matrix.append(list(input()))          # 입력된 문자열이 2차원 리스트 형태로 들어감

                                          # 2차원 리스트 준비 완료 


# 이제 for range로 col, row만큼 반복


for i in range(row):                      # 행 : row : 세로 : 층수 : i
    
    for j in range(col):                  # 열 : col : 가로 : 호수 : j
        
        count=0                           # 훗날 '.'자리에 들어갈 녀석(값)
        
        if matrix[i][j]=='.':             # 만약 요소가 '.'이면, 주변의 '*'개수를 찾는다(for 반복문으로!)
            
            for a in range(i-1, i+2):     # 한 칸 위부터 한 칸 아래까지 반복
                
                for b in range(j-1, j+2): # 한 칸 앞(왼쪽)부터 한 칸 뒤(오른쪽)까지 반복
                    
                    if not(a<0 or b<0 or a>=row or b>=col):   # 찾는 인덱스가 정해진 리스트의 범위를 넘어가면 오류
                        
                        if matrix[a][b]=='*':
                            
                            count+=1    # 주위를 빙 돌며 '*' 갯수를 찾고 그 수를 누적
                            
            matrix[i][j]=count          # 원래 '.'이던 자리(요소)에 '*' 갯수값 할당
            
            print(matrix[i][j], end='') # 만약 요소가 '.'이면 뚱땅뚱땅 하고 요소를 출력해라!
            
        else:
            
            print(matrix[i][j], end='') # 만약 요소가 '.'이 아니면 그냥 요소를 출력해라!

    print()                             # 다음 줄(행)로 넘어가기
