from .. import tools



POWER = 8



def per_symbol_stats(index, datum, symbols, symbol_data, norm_idx=0):
    ### NORMED CLOSE
    # norm_idx is used to set the base point for norming to, 
    # eg, the correct base of an overwide window to "smooth" EMA transition when cut to window
    if index["symbols"][0] == "*":
        symbol_set = list(symbols.keys())
    else:
        symbol_set = list(index["symbols"])
    
    norm = 1 / len(symbol_set)
    datum["nclose"] = symbol_data[symbol_set[0]]["nclose"] * norm
    for symbol in symbol_set[1:]:
        datum["nclose"] += symbol_data[symbol]["nclose"] * norm

    nclose_array = datum["nclose"].to_numpy(copy=True)
    datum["nclose_EMA"] = tools.ema.spectrum(nclose_array, POWER).transpose().tolist()

    ### DIFFERENCES
    datum["nclose_diff"] = 0
    for idx in range(1, len(datum.index)):
        datum["nclose_diff"][idx] = datum["nclose"][idx] - datum["nclose"][idx - 1]
    
    nclose_diff_array = datum["nclose_diff"].to_numpy(copy=True)
    datum["nclose_diff_EMA"] = tools.ema.spectrum(nclose_diff_array, POWER).transpose().tolist()

    return


def run(indexes, index_data, symbols, symbol_data):

    for period in index_data:
        for index in indexes:
            per_symbol_stats( indexes[index], index_data[period][index], symbols, symbol_data[period] )
    return
