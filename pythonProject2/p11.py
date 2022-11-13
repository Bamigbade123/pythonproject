alien_colour = 'red'
if 'green' in alien_colour:
    print('the player just earned 5 points')
elif 'yellow'in alien_colour:
    print('the player earned 10 points')
elif 'red'in alien_colour:
    print('the player just earned 15 points')

age = eval(input('enter your age: '))
if age <2:
    print('the person is a baby')
elif age <4:
    print('the person is a toddler')
elif age<13:
    print('the person is a kid')
elif age<20:
    print('the person is a teenager')
elif age<65:
    print('the person is an adult')
else:
    print('the person is an elder')

favourite_fruits = [ 'bananas','lemon','oranges','mangoes','melon']
if 'bananas' in favourite_fruits:
    print('i really like bananas')
reguested_toppings = ['mshrooms', 'green peppers', 'extra cheese']
for i in reguested_toppings:
    if i == 'green peppers':
        print('sorry, we are out of green peppers right now.')
    else:
        print("Addding " + i + ".")

print("\nFinish making your pizza")
reguested_toppings = []
if i:
    for i in reguested_toppings:
        print("Adding" + i +".")
    print("\nFinish making your pizza")
available_topping = ['mushroom', 'french fries', 'extra cheese'
                     'pepperoni', 'pineapple', 'extra']
reguested_toppings = ['mushrooms', 'olives', 'extra cheese']
for i in reguested_toppings:
    if i in available_topping:
        print('adding '+ i + '.')
    else:
        print("sorry, we don't have "+ i + '.')
print("\nfinished making your pizza")
