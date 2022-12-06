import numpy



def apply(a1, a2, output=None):
    return numpy.subtract(a1, a2, out=output)


def baseline(a):
    n = a.shape[0]
    s = a.shape[1:]

    baseline = numpy.zeros(shape=a.shape)
    for i in range(n):
        apply(a[i],a[n-1], output=baseline[i])

    return baseline

def pairwise(a, invert=False):
    n = a.shape[0]

    pairwise = numpy.zeros(shape=a.shape)
    if not invert:
        for i in range(1,n):
            apply(a[i],a[i-1], output=pairwise[i])
    else:
        for i in range(1,n):
            apply(a[i-1],a[i], output=pairwise[i])

    return pairwise
