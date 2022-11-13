print(len('hello'))
name = ['oyin', 'timmy', 'afeez', 'lafeef']
name[0] = 'lateef'
print(name)
print('my name is  ' + name[1].title() + '.')
name[1] = 'spendo'
print(name)
name.append('spending')
print(name)
food = []
food.append('yam')
food.append('rice')
food.append('beans')
print(food[1])
name.insert(0, 'spendiling')
print(name)
del name[-1]
print(name)
colour = []
colour.append('blue'.upper())
colour.append('green'.upper())
print(colour)
colour.insert(0,'red'.upper())
print(colour)
colour[0].upper()
del colour[0]
print(colour)
colour.append('')
guest_list = ['oyin', 'timmy','afeez']
x = ' you are invited to a dinner in my house'
print(guest_list[0] + ' u are invited to a dinner in my house')
print(guest_list[1] + ' you are invited to a dinner in my house')
print(guest_list[2] + ' u are invited to a dinner in my house')
#change of one guest
guest_list[0] = 'spending'
print(guest_list[0] + x )
print(guest_list[1] + x)
print(guest_list[2] + x)
#change of more guest
guest_list.insert(0, 'lateef')
guest_list.insert(2, 'spendo')
guest_list.append('ope')
#using for loop for d question
for i in guest_list:
    print(i + ' you are invited to my house for dinner')
guest_list.reverse()
print(guest_list)
print(len(guest_list))
#some practical
town = ['minna','Bida', 'mokwa','ilorin']
town.sort()
print(town)
town.reverse()
print(town)
magicians = ['Alice', 'David', 'Caro']
for i in magicians:
    print(i.upper() + ' that was a great task')
    print('i can wait to see ur next trick '+ i.lower() +'.\n')
    print('thanks')
    



