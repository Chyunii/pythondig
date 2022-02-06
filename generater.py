def prime_number_generator(start, stop):
    for i in range(start, stop):

        is_prime = True

        for n in range(2, i):

            if i % n == 0:
                is_prime = False

        if is_prime:
            yield i


start, stop = map(int, input().split())

g = prime_number_generator(start, stop)

print(type(g))

for i in g:
    print(i, end=' ')
