import pandas



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
    
    set_data = []
    for symbol in symbol_set:
        symbol_extract = symbol_data[symbol][["date", "nclose"]]
        symbol_extract["date"] = pandas.to_datetime(symbol_extract["date"])
        symbol_extract.rename(columns={"nclose":f"{symbol}"}, inplace=True)
        set_data.append(
            symbol_extract
        )
    
    joined_set_data = set_data[0]
    joined_set_data["date"] = pandas.to_datetime(joined_set_data["date"])
    for frame in set_data[1:]:
        print(joined_set_data)
        print(joined_set_data.dtypes)
        joined_set_data = joined_set_data.merge(frame, on="date", how="outer", sort=True)

    datum["avg_nclose"] = joined_set_data.mean(axis=1)


    nclose_array = datum["avg_nclose"].to_numpy(copy=True)
    datum["nclose_EMA"] = tools.ema.spectrum(nclose_array, POWER).transpose().tolist()

    ### DIFFERENCES
    datum["nclose_diff"] = 0
    for idx in range(1, len(datum.index)):
        datum["nclose_diff"][idx] = datum["avg_nclose"][idx] - datum["avg_nclose"][idx - 1]
    
    nclose_diff_array = datum["nclose_diff"].to_numpy(copy=True)
    datum["nclose_diff_EMA"] = tools.ema.spectrum(nclose_diff_array, POWER).transpose().tolist()

    return


def run(indexes, index_data, symbols, symbol_data):

    for period in index_data:
        for index in indexes:
            per_symbol_stats( indexes[index], index_data[period][index], symbols, symbol_data[period] )
    return
