import nbformat

source_path = "Nexus_Text_Processing_and_Generation.ipynb"
target_path = "latest.ipynb"

# Read the source notebook
with open(source_path, "r", encoding="utf-8") as f:
    src_nb = nbformat.read(f, as_version=4)

# Create a new empty notebook and copy cells
tgt_nb = nbformat.v4.new_notebook()
tgt_nb.cells = src_nb.cells

# Write the new notebook to the target path
with open(target_path, "w", encoding="utf-8") as f:
    nbformat.write(tgt_nb, f)

print(f"Copied {len(src_nb.cells)} cells from {source_path} to {target_path}")
