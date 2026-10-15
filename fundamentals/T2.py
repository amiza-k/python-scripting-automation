names=['ali','amir','Zahra','zahra']

people={
    'Amir': {'age':45,'ghad':171} ,
    'ali':{'age':35,'ghad':190},
    'zahra':{'age':90,'ghad':153}
}

for name in names:
    if name in people:
        print(name , end='=> \t')
        print(f"{name} is {people[name]['age']} years old and is {people[name]['ghad']} ")