import nbformat

nb = nbformat.read("Nexus_Text_Processing_and_Generation_copy.ipynb", as_version=4)

if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

nbformat.write(nb, "Nexus_Text_Processing_and_Generation_copy.ipynb")