def sum_corutine():
  total=0
  while True:
    x=(yield total)
    total+=x

co=sum_corutine()
print(next(co))

print(co.send(1))
print(co.send(2))
print(co.send(3))
