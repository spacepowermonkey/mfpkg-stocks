import os



def per_symbol_page(symbol, periods):
    file_path = f"/docs/symbols/{symbol['symbol']}"
    os.makedirs(file_path, exist_ok=True)

    page_text = "---\n"
    page_text += f"title: {symbol['symbol']} Report\n"
    page_text += "layout: page\n"
    page_text += "---\n"
    page_text += "\n\n"
    page_text += "Metric at | " + " | ".join(periods) + "\n"
    page_text += " --- | " + " | ".join(["---" for _ in periods]) + "\n"
    page_text += "Price | " + " | ".join([f"![](img/{period}-nclose.png)" for period in periods]) + "\n"
    page_text += "as Heatmap | " + " | ".join([f"![](img/{period}-nclose-heat.png)" for period in periods]) + "\n"
    page_text += "Rate | " + " | ".join([f"![](img/{period}-nclose-diff.png)" for period in periods]) + "\n"
    page_text += "as Heatmap | " + " | ".join([f"![](img/{period}-nclose-diff-heat.png)" for period in periods]) + "\n"
    page_text += "\n\n"

    with open(f"{file_path}/index.md", 'w') as outfile:
        outfile.write(page_text)

    return



def run(symbols, data):
    os.makedirs("/docs/symbols", exist_ok=True)

    periods = list(data.keys())
    periods.reverse()

    for symbol in symbols:
        per_symbol_page( symbols[symbol], periods )
        # The entire set of periods is used.
    return
