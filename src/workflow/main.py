from . import homepage
from . import load_data
from . import symbol_images
from . import symbol_pages
from . import symbol_stats



def run():
    symbols, data = load_data.run()

    symbol_stats.run(symbols, data)

    symbol_images.run(symbols, data)
    symbol_pages.run(symbols, data)
    homepage.run(symbols, data)
    return