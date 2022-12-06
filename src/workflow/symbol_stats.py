import pdb
from .. import tools



POWER = 8



def per_symbol_stats(datum, norm_idx=0):
    ### NORMED CLOSE
    # norm_idx is used to set the base point for norming to, 
    # eg, the correct base of an overwide window to "smooth" EMA transition when cut to window
    print(datum)
    base_val = datum["close"][norm_idx]
    datum["nclose"] = datum["close"] / base_val

    nclose_array = datum["nclose"].to_numpy(copy=True)
    datum["nclose_EMA"] = tools.ema.spectrum(nclose_array, POWER).transpose().tolist()

    ### DIFFERENCES
    datum["nclose_diff"] = 0
    for idx in range(1, len(datum.index)):
        datum["nclose_diff"][idx] = datum["nclose"][idx] - datum["nclose"][idx - 1]
    
    nclose_diff_array = datum["nclose_diff"].to_numpy(copy=True)
    datum["nclose_diff_EMA"] = tools.ema.spectrum(nclose_diff_array, POWER).transpose().tolist()

    return


def run(symbols, data):
    for period in data:
        for symbol in symbols:
            per_symbol_stats( data[period][symbol] )
    return
