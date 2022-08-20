import pickle
 
s=open('stationary','wb')
d={
    'spitzer':'sharpner',
    'kuli':'pen',
    'buch':'book'
    }
pickle.dump(d,s)
s.close()