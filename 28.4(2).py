with open('wordss.txt', 'r') as file:

    words=file.readlines()

    for i in words:

        if i.strip('\n')==i.strip('\n')[::-1]:

            print(i.strip('\n'))
