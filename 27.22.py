lines=['안녕하세요.\n', '저는\n', '김채현입니다.\n']

with open('hi.txt', 'w') as file:
    file.writelines(lines)
