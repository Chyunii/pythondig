import sys
print(sys.getrefcount(1000))    # 2: Windows에서 처음 레퍼런스 카운트는 2
                                
x = 1000                        # x에 1000을 저장
print(sys.getrefcount(1000))    # 3: 1000을 한 번 사용하여 레퍼런스 카운트 1 증가(Windows)
                                
y = 1000                        # y에 1000을 저장
print(sys.getrefcount(1000))    # 4: 1000을 한 번 사용하여 레퍼런스 카운트 1 증가(Windows)
                               
print(x is y)    # True: x와 y가 같은 객체를 가리키고 있으므로 True가 나옴
