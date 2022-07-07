import numpy as np

def score(w1,w2,b):
    return w1*.4 + w2*.6 + b

def sigmoid(w1,w2,b):
    x = score(w1,w2,b)
    return 1/(1+np.exp(-x))    

print(sigmoid(2,6,-2))
print(sigmoid(3,5,-2.2))
print(sigmoid(5,4,-3))