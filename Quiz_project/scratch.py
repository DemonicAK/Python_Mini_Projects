


print('welcome to the quiz')   #welcome

Q=input('DO U WANT TO PLAY: ')      #asking user 


    
def gameplay():
    c=0
    Q=0
    file =open('datw.txt','r')
    p=" "
    while p :
        p=file.readline()
        print(p,end='')
        Q+=1
        k=input('ans: ')
        if k==file.readline():
            print ('GOOD JOB')
            c+=1
        else:
            print("nope")
            
    file.close()
    print(c,'out of ',Q,'questions correct')
    print('accuracy',eval('c*100/Q'))

    

    
    
if Q=='y':
    print ('playing....')
    gameplay()
else:
    
    print ("thanks")
    print('exited')
        
            
    