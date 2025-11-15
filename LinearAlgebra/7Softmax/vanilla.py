
def softmax(x):
    e = 2.718281828
    ex = [e**xi for xi in x]
    suma = sum(ex)
    return [v/suma for v in ex]

print(softmax([6,3,5]))
