def calc():
    a=3
    b=5
    def mul_add(x):
        return a*x+b
    return mul_add

c=calc()
print(c(1), c(2), c(3), c(4), c(5))
