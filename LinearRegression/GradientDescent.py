y = [3,9]
x = [[1,4,7],[2,5,8]] 
teta = [0.1,0.1,0.1]


def hyp(params, xi):
    acum = 0
    for j in range(len(xi)):
        acum += params[j] * xi[j]
    return acum

def cost(params, x, y):
    acum = 0
    m = len(x)
    for i in range(m):
        acum += (hyp(params, x[i]) - y[i]) ** 2

    acum = acum/(2*m)
    return acum

def gradient(params, samples, y):
    new_params = [0,0,0]
    acum = 0
    lg = 0.003
    m = len(samples)
    for j in range(len(params)):
        for i in range(m):
            acum += (hyp(params, samples[i]) - y[i])*samples[i][j]
        grad = lg * (acum/(2*m))
        new_params[j] = params[j]-grad
    return new_params

def training(params, samples, y):
    epoch = 0
    while True:
        old_params = params
        params = gradient(params, samples, y)
        epoch += 1
        if old_params == params:
            return params

t = training(teta, x, y)
print(t)