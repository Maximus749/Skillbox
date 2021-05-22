from random import randint

MAX_BUNCHES = 5
MAX_BUNCHE_SIZE = 20

_holder = {}

def put_stones():
    global _holder
    _holder = {}
    for i in range(1, MAX_BUNCHES + 1):
        _holder[i] = randint(1, MAX_BUNCHE_SIZE)

def take_from_bunch(position, quantity):
    if position in _holder:
        _holder[position] -= quantity

# def get_bunches():
#     return list(_holder.values())
def get_bunches():
    res = []
    for key in sorted(_holder.keys()):
        res.append(_holder[key])
    return res

def gameover():
    return sum(_holder.values()) == 0
