def upper_generator(x):
  for i in x:
    yield i.upper()

fruit=['apple', 'pear', 'grape', 'pineapple', 'orange']

for i in upper_generator(fruit):
  print(i)
