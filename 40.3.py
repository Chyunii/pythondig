def number_generator(stop):
  n=0
  while n< stop:
    yield n
    n+=1

def three_generator():
  yield from number_generator(3)

for i in three_generator():
  print(i)
