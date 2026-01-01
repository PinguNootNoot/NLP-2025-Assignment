import numpy as np
import re
import random
import pandas as pd

def Preprocess(data, filename):
    OP = ['+', '-', '*']

    with open(filename, 'w') as f:
        for equ in data:
            op = OP[random.randint(0,2)]
            update = ')' + op
            equ = re.sub('[)][+\-*]*', update, equ)
            if equ[len(equ)-1] in OP:
                equ = equ[:-1]
            f.write(equ + '\n')


def DataBuilder(data):
    ans = list()
    for d in data:
        aw = eval(d)
        ans.append(aw)

    equations = list()
    for d in data:
        e = d + '='
        equations.append(e)

    df = pd.DataFrame({'src': equations, 'tgt': ans})
    df.to_csv('./data/arithmetic_3digit.csv', index=False)


file = './data/arith.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

DataBuilder(data)
