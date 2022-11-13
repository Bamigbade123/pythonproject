#checking user name
current_user = ['timmy','abass','afeez','oyin', 'spendo']
new_user = [ 'timmy', 'lateef', 'oyin', 'faith', 'saka']
for i in new_user:
    if i in current_user:
        print(i.title() + ", you will need to enter another user name")
    else:
        print(i.title() +", the username is available")