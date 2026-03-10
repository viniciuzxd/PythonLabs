import os
from random import random

def gera_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]
    return cpf