# import nbformat

# nb = nbformat.read("Nexus_Text_Processing_and_Generation_copy.ipynb", as_version=4)

# if "widgets" in nb.metadata:
#     del nb.metadata["widgets"]

# nbformat.write(nb, "Nexus_Text_Processing_and_Generation_copy.ipynb")
import nbformat

with open("Nexus_Text_Processing_and_Generation_copy.ipynb", "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# This will raise errors if the notebook is malformed
nbformat.validate(nb)

# Optionally write it back to fix minor issues
with open("Nexus_Text_Processing_and_Generation_copy.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(nb, f)