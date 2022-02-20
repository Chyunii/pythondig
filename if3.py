a,b,c,d = map(int, input().split())

if (a or b or c or d) <0 or (a or b or c or d) >100 :
    print('잘못된 점수')

else :
    if (a+b+c+d)/4 >= 80 :
        print('합격')
    else :
        print('불합격')
        
