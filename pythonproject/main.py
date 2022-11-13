family = ["lukman", "sukrat", "afeez", "ramon", "morufat"]
print(family[-1].upper())
print(family[1].title())
print(family[0].title())
family[0] = "abass"
print(family)
family.append('lukman')
print(family)
family.insert(1, 'samad')
print(family)
del family[2]
print(family)
print(family[:3])
print(family[1:4])
print(family[2:5])
