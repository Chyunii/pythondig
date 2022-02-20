with open('words.txt', 'r') as file:
    
  word = None
  
  while word != '':
      
    word = file.readline().strip('\n')
    
    if  word == ''.join(reversed(word)):
        
      print(word)

    
