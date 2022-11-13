invited = ['afeez','abass', 'qodir']
for x in invited:
 print(f"i am inviting you mr Bamigbade {x.title()} to a dinner party in my house")

del invited[2]
print(invited)
invited.insert(2, "samad")
print(f'i am inviting you mr Bamigbade {invited[2]} to a dinner party in my house')
invited.insert(3, "ramon")
invited. insert(4, "morufat")
invited.insert(5,"alao")
for invited in range(0, 4):
 print(invited)