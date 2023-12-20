import pandas as pd
from os import listdir
import numpy as np

class ReturnValue:
    def __init__(self, C, S, P, T):
        self.C_counts = C
        self.C_sec = S
        self.T = T
        self.P = P

def LoadMatrices():
    C = [pd.read_csv(f'csv/C/{x}', index_col = 0) for x in listdir('csv/C')]
    P = [pd.read_csv(f'csv/P/{x}', index_col = 0) for x in listdir('csv/P')]
    S = [pd.read_csv(f'csv/S/{x}', index_col = 0) for x in listdir('csv/S')]
    T = [pd.read_csv(f'csv/T/{x}', index_col = 0) for x in listdir('csv/T')]

    indices = np.array([x.split('.')[0].split('_') for x in listdir('csv/C')]).astype(int)

    return dict(zip([tuple(idx) for idx in indices], [ReturnValue(c, s, p, t) for (c, s, p, t) in zip(C, S, P, T)]))

