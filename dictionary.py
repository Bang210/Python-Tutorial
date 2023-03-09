persons = [
    {'name' : 'a', 'level' : 1, 'home' : 'Seoul'},
    {'name' : 'b', 'level' : 2, 'home' : 'Jeju'},
    {'name' : 'c', 'level' : 3, 'home' : 'Incheon'}
]
for person in persons :
    for key in person :
        print(key, ':', person[key])
    print('-' * 50)
