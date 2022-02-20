
with open ('words.txt', 'r') as file:

    line=file.read().split()

    for i in line:

        if 'c' in i:
            
            print(i.strip(',.'))  
