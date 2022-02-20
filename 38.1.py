y=[10,20,30]

try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index]/x)

except Exception as e:
    print('예외가 발생했습니다.', e)
