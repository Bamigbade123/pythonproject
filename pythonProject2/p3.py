from random import randint
num = randint(1,10)
#guess =eval(input('Enter your guess: '))
#if guess == num:
 #   print('you got it')
#else:
    #print('sorry, the num is: ',num)
grade = eval(input('Enter your grade: '))
if grade>=70:
    print('A')
elif grade>=60:
    print('B')
elif grade>=50:
    print('C')
elif grade>=40:
    print('D')
else:
    print('E')




