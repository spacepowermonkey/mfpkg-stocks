import numpy



def apply(array, period=1):
    n = array.shape[0]

    roc_array = numpy.zeros(shape=(n,))
    
    roc_array[0] = 0
    for i in range(1,n):
        di = max(0, i - period)
        if array[di] == 0:
            roc_array[i] = 0
        else:
            roc_array[i] = (array[i] - array[di])/array[di]

    return roc_array


def twoD(array, period=1):
    m, n = array.shape[0:2]

    roc_array = numpy.zeros(shape=(m,n))

    for i in range(m):
        roc_array[i] = apply(array[i], period)

    return roc_array
