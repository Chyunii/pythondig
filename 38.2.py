try:
    x=int(input('나눌 숫자를 입력하세요: '))
    y=10/x

except ZeroDivisionError:
    print('숫자를 0으로 나눌 수 없습니다.')

else:
    print(y)

finally:
    print('코드 실행이 끝났습니다.')
