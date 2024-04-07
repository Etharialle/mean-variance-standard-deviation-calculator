import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        calculations = {}
        arr = np.asarray(list)
        print(arr)
        shaped_arr = arr.reshape(3, 3)
        print(shaped_arr)

        # mean calcs
        mean0 = shaped_arr.mean(axis=0, keepdims=True)
        print(mean0)
        mean1 = shaped_arr.mean(axis=1, keepdims=True)
        mean1 = mean1.T
        print(mean1)
        meanf = arr.mean(axis=0, keepdims=True)
        print(meanf)
        mean0 = mean0.tolist()
        mean1 = mean1.tolist()
        meanf = meanf.tolist()
        mean = mean0 + mean1 + meanf
        calculations['mean'] = mean

        # variance calcs
        var0 = shaped_arr.var(axis=0, keepdims=True)
        print(var0)
        var1 = shaped_arr.var(axis=1, keepdims=True)
        var1 = var1.T
        print(var1)
        varf = arr.var(axis=0, keepdims=True)
        print(varf)
        var0 = var0.tolist()
        var1 = var1.tolist()
        varf = varf.tolist()
        var = var0 + var1 + varf
        calculations['variance'] = var

        # standard deviation calcs
        std0 = shaped_arr.std(axis=0, keepdims=True)
        print(std0)
        std1 = shaped_arr.std(axis=1, keepdims=True)
        std1 = std1.T
        print(std1)
        stdf = arr.std(axis=0, keepdims=True)
        print(stdf)
        std0 = std0.tolist()
        std1 = std1.tolist()
        stdf = stdf.tolist()
        std = std0 + std1 + stdf
        calculations['standard deviation'] = std

        # find max values
        max0 = shaped_arr.max(axis=0, keepdims=True)
        print(max0)
        max1 = shaped_arr.max(axis=1, keepdims=True)
        max1 = max1.T
        maxf = arr.max(axis=0, keepdims=True)
        print(maxf)
        max0 = max0.tolist()
        max1 = max1.tolist()
        maxf = maxf.tolist()
        max = max0 + max1 + maxf
        calculations['max'] = max

        # find min values
        min0 = shaped_arr.min(axis=0, keepdims=True)
        print(min0)
        min1 = shaped_arr.min(axis=1, keepdims=True)
        min1 = min1.T
        minf = arr.min(axis=0, keepdims=True)
        print(minf)
        min0 = min0.tolist()
        min1 = min1.tolist()
        minf = minf.tolist()
        min = min0 + min1 + minf
        calculations['min'] = min

        # sum values
        sum0 = shaped_arr.sum(axis=0, keepdims=True)
        print(sum0)
        sum1 = shaped_arr.sum(axis=1, keepdims=True)
        sum1 = sum1.T
        sumf = arr.sum(axis=0, keepdims=True)
        print(sumf)
        sum0 = sum0.tolist()
        sum1 = sum1.tolist()
        sumf = sumf.tolist()
        sum = sum0 + sum1 + sumf
        calculations['sum'] = sum

    return calculations
