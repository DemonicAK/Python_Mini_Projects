import pickle
import random

#########
files=['data/stationary.txt']

########

print('Welcome to the vocubulary quiz program.Select one of the following word lists:')
for i in files:
    print (i[5:])

############
p=input('enter:')
if p in files:
    k=open(p[:-4],'rb')
    try:
        while True:
            d=pickle.load(k)
    except:
        k.close()
#d is the data in file
    
    
else:
    print('pls name correct file')

#########d

print (len(d.keys()), 'entries found',end='')
Q=int(input('no of words want?'))
if len(d.keys())<Q:
    Q=len(d.keys())
###d.keys()
c=0
j=random.sample(d.keys(),Q)
for i in j :
    print('English word:',i)
    print('enter 1 equivalent to word.')
    ans=input('Word:')
    if ans.capitalize()==d[i].capitalize():
        print('Correct!')
        c+=1
    else:
        print('Incorrect!')
    print('---')

print(c,'out of',Q,'correct')   

    

        