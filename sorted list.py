
students = [

    ['john', 'C', 19],

    ['maria', 'A', 25],

    ['andrew', 'B', 7]

]
 
print(sorted(students, key=lambda student: student[1]))  # 안쪽 리스트의 인덱스 1을 기준으로 정렬

print(sorted(students, key=lambda student: student[2]))  # 안쪽 리스트의 인덱스 2를 기준으로 정렬
