import pickle
import random

#########


print('Welcome to the vocubulary quiz program')


############


k=open('dictinary','rb')
try:
    while True:
        d=pickle.load(k)
except:
    k.close()
#d is the data in file


#########d

print (len(d.keys()), 'entries found',end='\n')
Q=int(input('no of words want?'))
if len(d.keys())<Q:
    Q=len(d.keys())
###d.keys()


    
    
correct = 0
words = random.sample(list(d.items()), Q)

for german, english in words:
    print(f"\nGerman word: {german}")
    answer = input('Enter the English equivalent: ')
    if answer.lower() == english.lower():
        print('Correct!')
        correct += 1
    else:
        print(f'Incorrect. The correct answer is: {english}')
    print('---')

print(correct, 'out of', Q, 'correct')

# Results
print(f"\nQuiz completed! You got {correct} out of {Q} correct.")
percentage = (correct / Q) * 100
print(f"Your score: {percentage:.2f}%")

if percentage >= 90:
    print("Excellent job!")
elif percentage >= 70:
    print("Good work!")
elif percentage >= 50:
    print("Not bad, keep practicing!")
else:
    print("You might want to study more. Keep it up!")


