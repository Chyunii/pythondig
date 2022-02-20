import pickle

name='james'
age=17
address='서울시 서초구 반포동'
scores={'korean':90, 'english':95, 'mathmatics':85, 'science':82}

with open('james.p', 'wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)
    
