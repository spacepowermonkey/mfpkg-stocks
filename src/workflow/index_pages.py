import os



def per_index_page(index, periods):
    file_path = f"/docs/indexes/{index['short']}"
    os.makedirs(file_path, exist_ok=True)

    page_text = "---\n"
    page_text += f"title: {index['name']} Report\n"
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



def run(indexes, index_data):
    os.makedirs("/docs/indexes", exist_ok=True)

    periods = list(index_data.keys())
    periods.reverse()

    for index in indexes:
        per_index_page( indexes[index], periods )
        # The entire set of periods is used.
    return
