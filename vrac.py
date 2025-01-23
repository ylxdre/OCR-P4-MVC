# generate player list
from random import randint

list = []
for i in range(16):
    list.append(["Player"+str(i+1), randint(0, 8)])

