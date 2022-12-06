def by_val(val):
    def _norm(array):
        return array / val
    return _norm

def by_first(array):
    print(array)
    print(array[0])
    return array / array[0]

def by_max(array):
    val = abs(array[0])
    for i in range(1, array.shape[0]):
        if abs(array[i]) > val:
            val = abs(array[i])
    if val == 0:
        return array
    return array / val

def by_total(array):
    val = sum(array)
    return array / val
