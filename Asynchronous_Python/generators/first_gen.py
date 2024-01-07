# просто пример работы различных генераторов и взаимодействий с ними
from time import time
def gen(name):
    for i in name:
        yield i

g = gen("daniil")

# (venv) sib-coder@fedora ~/P/pythonProject1> python3 -i main.py
# >>> g
# <generator object gen at 0x7ff6f4e76140>
# >>> next(g)
# 'd'

def gen_filename():
    while True:
        pattern = 'file-{}.txt'
        t=int(time()*1000)
        yield pattern.format(str(t))

# (venv) sib-coder@fedora ~/P/pythonProject1> python3 -i main.py
# >>> g = gen_filename()
# >>> next(g)
# 'file-1704621694783.txt'
# >>> next(g)
# 'file-1704621695970.txt'
def gen1(s):
    for i in s:
        yield i

def gen2(n):
    for i in range(n):
        yield i

g1 = gen1("daniil")
g2 = gen2(6)

tasks = [g1,g2]
while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass

# (venv) sib-coder@fedora ~/P/pythonProject1> python3 -i main.py
# d
# 0
# a
# 1
# n
# 2
# i
# 3
# i
# 4
# l
# 5
# >>>
