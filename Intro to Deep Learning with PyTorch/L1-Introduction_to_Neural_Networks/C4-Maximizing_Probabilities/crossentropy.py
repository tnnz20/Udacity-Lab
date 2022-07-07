from cgi import test
import numpy as np

def cross_entropy(Y,P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))


test1 = cross_entropy((1,1,0), (0.8,0.7,0.1))
test2 = cross_entropy((0,0,1), (0.8,0.7,0.1))

print(f'Cross Entropy 1 : {test1:.2f}')
print(f'Cross Entropy 2 : {test2:.2f}')