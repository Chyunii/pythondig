def calc():
  result=0
  while True:
    expression=(yield result)
    a, b, c=expression.split()
    if b=='+':
      result=int(a)+int(c)
    elif b=='-':
      result=int(a)-int(c)
    elif b=='*':
      result=int(a)*int(c)
    elif b=='/':
      result=int(a)/int(c)
    

expressions = input().split(', ')
 
c = calc()
next(c)
 
for e in expressions:
    print(c.send(e))
 
c.close()
