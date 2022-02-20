x=int(input())

for i in range(x):

    for j in range(x):

        if j<i:
            print('*', end='')

    print()
