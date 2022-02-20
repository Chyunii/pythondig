x, y = map(int, input().split())

if x<1 or x>20:
    print("잘못된 입력입니다")
if y<10 or y>30:
    print("잘못된 입력입니다")

a=[2**i for i in range(x,y+1)]

a.pop(1)
a.pop(-2)

print(a)
