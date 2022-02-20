def countdown(n):
    
    
    def count():
        
        nonlocal n

        r=n

        n-=1
        
        return r
    
    return count

n=int(input())

c=countdown(n)

for i in range(n):
    
    print(c(), end=' ')
