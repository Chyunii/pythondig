a=list(map(int, input().split(';')))

a.sort(reverse=True)

for i in a:
    
    i='{0:>9,}'.format(i)

    print(i)
