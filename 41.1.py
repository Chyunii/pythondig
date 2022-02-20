def number_corutine():
  while True:
    x=(yield)
    print(x)

co=number_corutine()

co.send(None)

co.send(1)
co.send(2)
co.send(3)
