# ============================================================
#
#  ┌─────────────────────────────────────────────────────────┐
#  │  СРАВНЕНИЕ list vs tuple vs dict                        │
#  ├──────────────┬──────────────┬─────────────┬─────────────┤
#  │ Характеристика│    list      │    tuple    │    dict     │
#  ├──────────────┼──────────────┼─────────────┼─────────────┤
#  │ Изменяемость │   mutable    │  immutable  │  mutable    │
#  │ Упорядочен   │     да       │     да      │ да (3.7+)   │
#  │ Доступ       │ по индексу   │ по индексу  │ по ключу    │
#  │ Дубликаты    │ элементов да │ элементов да│ ключей нет  │
#  │ Хешируемость │     нет      │ если элем.  │    нет      │
#  │ Память       │   средне     │   мало      │   много     │
#  │ Методов      │     11       │     2       │    11       │
#  │ Создание     │  [] или list │ () или tuple│ {} или dict │
#  └──────────────┴──────────────┴─────────────┴─────────────┘
#
# ============================================================

import random
#проба работы с разными типами
dictat = {}
english_names = [
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer",
    "Michael", "Linda", "William", "Elizabeth", "David", "Barbara",
    "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah",    "Charles", "Karen", "Christopher", "Lisa", "Daniel", "Nancy",
    "Matthew", "Betty", "Anthony", "Margaret", "Mark", "Sandra",
    "Donald", "Ashley", "Steven", "Kimberly", "Paul", "Emily",
    "Andrew", "Donna", "Joshua", "Michelle", "Kenneth", "Carol",
    "Kevin", "Amanda", "Brian", "Dorothy", "George", "Melissa"
]
#  x in lst         — проверяет наличие элемента
#  x not in lst     — проверяет отсутствие элемента
for _ in range(10): 
    name = random.choice(english_names)
    value = random.randint(1,1000)
    if name not in dictat:
        dictat[name] = value
print(dictat)



def keys_checker(d: dict, l:list):
    names = []
    counter = 0
    for _ in range(random.randint(1,5)):
        names.append(random.choice(l))
    print(f"Random keys to check: {names}")
    for i in names:
        if d.get(names[i], default = None) == None: #переделать 
            print(f"Unavalable key: {names[i]}")
            continue
        elif d.get(names[i]) == names[i]:
            counter += 1
            print(f'Key is available: {names[i]}')
    if counter == len(names):
        print('All keys are available')
    else:
        print('not all keys available')

keys_checker(dictat, english_names)


        
