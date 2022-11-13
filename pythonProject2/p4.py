#length = eval(input('Enter a legth: '))
#import math
#if length <0:
 #   print('invalid')
#else:
 #   print('valid')
tem = float(input('Enter a number in celsius: '))
if tem > -273.15:
    print('invalid, because the temperature is below absolutely zero')
elif tem <-273.15:
    print('the temperature is below freezing point')
elif tem == -273.15:
    print('the temperature is absolutely zero')
elif tem == 0:
    print('the temperature is at freezing point')
elif  tem >100:
    print('the temperature is between d normal range')
elif tem == 100:
    print('the temperature is at boiling point')
else:
    print('the temperature is above the boiling point')




