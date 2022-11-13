alien = {'colour': 'green', 'point': 5}
print(alien['colour'])
print(alien['point'])
alien['x_position'] = 0
alien['y_position'] = 25
print(alien)
alien = {}
alien['colour'] = "green"
alien['point'] = 5
print(alien)
alien = {'colour': 'green'}
print('the alien is ' + alien['colour'] + ".")

alien['colour'] = 'yellow'
print("the alien is now " + alien['colour'] + ".")
alien = {'x_position': 0, 'y_positoin': 25, 'speed': 'medium'}
print("original x_position: " + str(alien['x_position']))
if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien['x_position'] = alien['x_position'] + x_increment
print("New x_position: " + str(alien['x_position']))
alien = {'colour': 'green', 'point': 5}
print(alien)
del alien['point']
print(alien)
