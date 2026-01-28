import random as random


def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))
print(add_item(2))

def random_walk(k):
    l=[]
    for i in range(1000):
        step=random.choice([-1,1])
        l.append(step)
    return l

l_data=[]

for i in range(1000):
    l_data.append(random_walk(i))

print(l_data)


