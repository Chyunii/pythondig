
number_list = [1, 2, 3]
 
def append_number(n):        # 함수 실행이 외부 상태에 영향을 끼침

    number_list.append(n)    # 함수 외부에 있는 number_list의 상태가 바뀜
 
