import turtle as t

n=6

t.shape('turtle')
t.color('#ff6984')
t.begin_fill()

for i in range(n):
    t.forward(100)
    t.right(360/n)

t.end_fill()
