import cairosvg
import math
import matplotlib.figure as figure
import numpy
import os



def norm_diff(val):
    return 0.5 + 0.5*math.tanh(val)
vec_norm_diff = numpy.vectorize(norm_diff)

def norm_price(val):
    return 0.25*val if val <= 1 else 0.25 + 0.75*math.tanh(val - 1) 
vec_norm_price = numpy.vectorize(norm_price)


def _initialize_image(width=11, height=8.5, dpi=300):
    fig = figure.Figure(figsize=(width, height), dpi=dpi)
    ax = fig.add_axes([0,0,1,1])
    ax.axis("off")

    return (fig, ax)

def _save_image(fig, path_prefix):
    fig.savefig(f"{path_prefix}.svg")
    cairosvg.svg2png(
        file_obj=open(f"{path_prefix}.svg", "rb"), write_to=f"{path_prefix}.png"
    )
    return


def _nclose_image(img_path, period, datum):
    nclose_path = f"{img_path}/{period}-nclose"
    fig, ax = _initialize_image()

    nclose_array = datum["nclose"].to_numpy()
    nclose_array = nclose_array.reshape((nclose_array.shape[0], 1))
    nclose_ema_array = numpy.array(datum["nclose_EMA"].tolist())
    nclose_full_array = numpy.concatenate([nclose_array, nclose_ema_array], axis=1).transpose()

    nnclose_array = vec_norm_price(nclose_full_array).transpose()

    ax.set_xlim(0, nnclose_array.shape[0])
    ax.set_ylim(0, 1)
    ax.plot(nnclose_array, color="black")

    _save_image(fig, nclose_path)
    return

def _nclose_heat_image(img_path, period, datum):
    nclose_heat_path = f"{img_path}/{period}-nclose-heat"
    fig, ax = _initialize_image()

    nclose_array = datum["nclose"].to_numpy()
    nclose_array = nclose_array.reshape((nclose_array.shape[0], 1))
    nclose_ema_array = numpy.array(datum["nclose_EMA"].tolist())
    nclose_full_array = numpy.concatenate([nclose_array, nclose_ema_array], axis=1).transpose()

    ax.imshow(nclose_full_array,
        vmin=0,
        cmap="plasma", aspect="auto"
    )
    _save_image(fig, nclose_heat_path)
    return

def _nclose_diff_image(img_path, period, datum):
    nclose_diff_path = f"{img_path}/{period}-nclose-diff"
    fig, ax = _initialize_image()

    nclose_diff_array = datum["nclose_diff"].to_numpy()
    nclose_diff_array = nclose_diff_array.reshape((nclose_diff_array.shape[0], 1))
    nclose_diff_ema_array = numpy.array(datum["nclose_diff_EMA"].tolist())
    nclose_diff_full_array = numpy.concatenate([nclose_diff_array, nclose_diff_ema_array], axis=1).transpose()

    nnclose_diff_array = vec_norm_diff(nclose_diff_full_array).transpose()

    ax.set_xlim(0, nnclose_diff_array.shape[0])
    ax.set_ylim(0, 1)
    ax.plot(nnclose_diff_array, color="black")

    _save_image(fig, nclose_diff_path)
    return

def _nclose_diff_heat_image(img_path, period, datum):
    nclose_diff_heat_path = f"{img_path}/{period}-nclose-diff-heat"
    fig, ax = _initialize_image()

    nclose_diff_array = datum["nclose_diff"].to_numpy()
    nclose_diff_array = nclose_diff_array.reshape((nclose_diff_array.shape[0], 1))
    nclose_diff_ema_array = numpy.array(datum["nclose_diff_EMA"].tolist())
    nclose_diff_full_array = numpy.concatenate([nclose_diff_array, nclose_diff_ema_array], axis=1).transpose()

    ax.imshow(nclose_diff_full_array,
        vmin=0,
        cmap="plasma", aspect="auto"
    )
    _save_image(fig, nclose_diff_heat_path)


def per_symbol_render(period, symbol, datum):
    img_path = f"/docs/symbols/{symbol['symbol']}/img"
    os.makedirs(img_path, exist_ok=True)

    _nclose_image(img_path, period, datum)
    _nclose_heat_image(img_path, period, datum)
    _nclose_diff_image(img_path, period, datum)
    _nclose_diff_heat_image(img_path, period, datum)
    
    return


def run(symbols, data):
    os.makedirs("/docs/symbols", exist_ok=True)

    for period in data:
        for symbol in symbols:
            per_symbol_render( period, symbols[symbol], data[period][symbol] )
    return
