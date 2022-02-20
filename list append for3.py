a=[3,1,3,2,5]    #톱니형 리스트 만들기
b=[]

for i in a:
    line=[]
    for j in range(i):
        line.append(0)
    b.append(line)

print(b)
