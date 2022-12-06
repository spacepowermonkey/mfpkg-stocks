import numpy



_SIZE = 3



def _calc(array, period):
    n = array.shape[0]

    mass = 0
    avg = 0
    for i in range(n):
        # Mass is halved per period.
        mass_i = (0.5)**((n-i)/period)

        avg += mass_i * array[i]
        mass += mass_i

    return avg/mass


def apply(array, period):
    n = array.shape[0]
    window = 2**_SIZE * period

    ema_array = numpy.zeros(shape=(n,))
    ema_array[0] = array[0]
    for i in range(1,n):
        start = max(0, i - window)
        ema_array[i] = _calc(array[start:i], period)

    return ema_array


def spectrum(array, power):
    n = array.shape[0]

    spec_array = numpy.zeros(shape=(power, n))
    for i in range(power):
        spec_array[i] = apply(array, 2**i)
    
    return spec_array
