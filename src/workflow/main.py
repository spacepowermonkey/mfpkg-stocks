from . import homepage
from . import index_images
from . import index_pages
from . import index_stats
from . import load_data
from . import symbol_images
from . import symbol_pages
from . import symbol_stats



def run():
    symbols, symbol_data, indexes, index_data = load_data.run()

    symbol_stats.run(symbols, symbol_data)
    index_stats.run(indexes, index_data, symbols, symbol_data)

    symbol_images.run(symbols, symbol_data)
    index_images.run(indexes, index_data)
    
    symbol_pages.run(symbols, symbol_data)
    index_pages.run(indexes, index_data)
    homepage.run(indexes, index_data, symbols, symbol_data)
    return
