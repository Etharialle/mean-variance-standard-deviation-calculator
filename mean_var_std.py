import numpy as np


def calculate(list):
    # Check to see if the list has less than 9 values, raise an error if less than 9
    # I would probably make this "!= 9" rather than "< 9" so it errors if there are greater than 9 values as well
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        calculations = {}
        arr = np.asarray(list)
        shaped_arr = arr.reshape(3, 3)

        # mean calcs
        mean0 = shaped_arr.mean(axis=0, keepdims=True)
        mean1 = shaped_arr.mean(axis=1, keepdims=True)
        mean1 = mean1.T
        meanf = arr.mean(axis=0, keepdims=True)
        mean = (mean0.tolist() + mean1.tolist() + meanf.tolist())
        calculations['mean'] = mean

        # variance calcs
        var0 = shaped_arr.var(axis=0, keepdims=True)
        var1 = shaped_arr.var(axis=1, keepdims=True)
        var1 = var1.T
        varf = arr.var(axis=0, keepdims=True)
        var = (var0.tolist() + var1.tolist() + varf.tolist())
        calculations['variance'] = var

        # standard deviation calcs
        std0 = shaped_arr.std(axis=0, keepdims=True)
        std1 = shaped_arr.std(axis=1, keepdims=True)
        std1 = std1.T
        stdf = arr.std(axis=0, keepdims=True)
        std = (std0.tolist() + std1.tolist() + stdf.tolist())
        calculations['standard deviation'] = std

        # find max values
        max0 = shaped_arr.max(axis=0, keepdims=True)
        max1 = shaped_arr.max(axis=1, keepdims=True)
        max1 = max1.T
        maxf = arr.max(axis=0, keepdims=True)
        max = (max0.tolist() + max1.tolist() + maxf.tolist())
        calculations['max'] = max

        # find min values
        min0 = shaped_arr.min(axis=0, keepdims=True)
        min1 = shaped_arr.min(axis=1, keepdims=True)
        min1 = min1.T
        minf = arr.min(axis=0, keepdims=True)
        min = (min0.tolist() + min1.tolist() + minf.tolist())
        calculations['min'] = min

        # sum values
        sum0 = shaped_arr.sum(axis=0, keepdims=True)
        sum1 = shaped_arr.sum(axis=1, keepdims=True)
        sum1 = sum1.T
        sumf = arr.sum(axis=0, keepdims=True)
        sum = (sum0.tolist() + sum1.tolist() + sumf.tolist())
        calculations['sum'] = sum

    return calculations
