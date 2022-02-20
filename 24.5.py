a=input().split()

count=0

for i in a:
    
    if i.strip(',.')=='the':
        count+=1

print(count)
