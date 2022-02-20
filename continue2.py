start, stop = map(int, input().split())
 
i = start
 
while True:
    if 1<=i<=200 and 10<=stop<=200:
        if i%10==3:
            i+=1
            continue

        if i>stop:
            break

    print(i, end=' ')
    i+=1
