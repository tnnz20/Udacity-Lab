import numpy as np

def score(x1,x2):
    return (4*x1) + (5*x2) - 9

def sigmoid(x1,x2):
    x = score(x1,x2)
    return 1/(1+np.exp(-x))

num = [[1,1], [2,4], [5,-5], [-4,5]]

step = 0
for x1,x2 in num:
    prob = sigmoid(x1,x2)
    print(f'Probability (sigmoid) {num[step]} : {prob}')
    step +=1
    
