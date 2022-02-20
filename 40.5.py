def file_read():
  with open('words.txt', 'r') as file:
    
    for i in file.readlines():
      yield i.strip('\n')

for i in file_read():
  print(i)
