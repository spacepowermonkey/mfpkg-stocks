def run(indexes, index_data, symbols, symbol_data):
    periods = list(symbol_data.keys())
    periods.reverse()

    symbols_by_letter = {}
    for symbol in symbols:
        first_letter = symbol[0]
        try:
            symbols_by_letter[first_letter].append(symbol)
        except KeyError:
            symbols_by_letter[first_letter] = [symbol]
    
    indexes_by_letter = {}
    for index in indexes:
        first_letter = index[0]
        try:
            indexes_by_letter[first_letter].append(index)
        except KeyError:
            indexes_by_letter[first_letter] = [index]
    
    page_text = "---\n"
    page_text += f"title: Stock Report\n"
    page_text += "layout: page\n"
    page_text += "---\n"
    page_text += "\n\n"
    page_text += f"This report is automatically generated, summarizing market activity at various scales: {', '.join(periods)}\n"
    page_text += "\n\n"

    page_text += "## Indexes\n"
    page_text += "\n"
    page_text += "Letter | | | | | \n"
    page_text += "--- | --- | --- | --- | --- | ---\n"
    letters = list(indexes_by_letter.keys())
    letters.sort()
    for letter in letters:
        # Add the letter as just its cell.
        page_text += f"{letter}"

        # Then add the symbols in the rightmost columns.
        idx = 1
        for index in indexes_by_letter[letter]:
            if idx == 0:
                # With the first cell of each row empty.
                page_text += f"\n   "
            else:
                page_text += f" | [{index}](indexes/{index}/)"
            idx = (idx + 1) % 6
        # Pad the table if your last row isn't full.
        if not idx == 0:
            while idx > 0:
                page_text += f" |   "
                idx = (idx + 1) % 6
        page_text += "\n"
    page_text += "\n\n"
    
    page_text += "## Symbols\n"
    page_text += "\n"
    page_text += "Letter | | | | | \n"
    page_text += "--- | --- | --- | --- | --- | ---\n"
    
    letters = list(symbols_by_letter.keys())
    letters.sort()
    for letter in letters:
        # Add the letter as just its cell.
        page_text += f"{letter}"

        # Then add the symbols in the rightmost columns.
        idx = 1
        for symbol in symbols_by_letter[letter]:
            if idx == 0:
                # With the first cell of each row empty.
                page_text += f"\n   "
            else:
                page_text += f" | [{symbol}](symbols/{symbol}/)"
            idx = (idx + 1) % 6
        # Pad the table if your last row isn't full.
        if not idx == 0:
            while idx > 0:
                page_text += f" |   "
                idx = (idx + 1) % 6
        page_text += "\n"
    page_text += "\n\n"

    with open(f"/docs/index.md", 'w') as outfile:
        outfile.write(page_text)

    return
