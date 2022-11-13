user = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key,value in user.items():
    print("\nkey: " + key)
    print("\nvalue: " + value)

favourite_language = {
    'jen': 'python',
    'serah': 'c',
    'edward': 'ruby',
    'phillip': 'python',
}
for name,language in favourite_language.items():
    print("\n" + name.title() + "'s favourite language is " +
          language.title() +".")
    print("\n" +language.title())
favourite_language = {
    'jen': 'python',
    'serah': 'c',
    'edward': 'ruby',
    'phillip': 'python',
}
for name in favourite_language:
    print(name.title())
favourite_language = {
    'jen': 'python',
    'serah': 'c',
    'edward': 'ruby',
    'phillip': 'python',
}
friend = ['phillip','serah']
for name in favourite_language:
    print(name.title())

    if name in friend:
        print(" hi " + name.title() +
          ", i see ur favourite language is " +
          favourite_language[name].title()+ "!")

