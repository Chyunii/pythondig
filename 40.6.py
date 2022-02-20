def prime_number_generator(start, stop):

  for n in range(start, stop):
    is_prime=True
    for i in range(2, n):
      if n%i==0:
        is_prime=False
    if is_prime:
      yield n

start, stop = map(int, input().split())
 
g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')
