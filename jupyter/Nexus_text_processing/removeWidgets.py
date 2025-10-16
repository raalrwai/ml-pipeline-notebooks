import nbformat

def clean_cell_metadata(cell):
    # Remove widget metadata keys inside the cell's metadata if they exist
    if 'metadata' in cell and cell['metadata']:
        cell_meta = cell['metadata']
        if 'widgets' in cell_meta:
            del cell_meta['widgets']
        # Sometimes widgets metadata can be nested, remove broadly if needed
        if 'nbformat' in cell_meta:
            # Optional: you can add more cleaning rules here
            pass
    return cell

def copy_cells_clean(src_path, dst_path):
    # Load source notebook
    with open(src_path, 'r', encoding='utf-8') as f:
        src_nb = nbformat.read(f, as_version=4)

    # Create a fresh notebook with default metadata
    new_nb = nbformat.v4.new_notebook()

    # Copy and clean cells
    new_cells = []
    for cell in src_nb.cells:
        clean_cell = clean_cell_metadata(cell)
        new_cells.append(clean_cell)

    new_nb.cells = new_cells

    # Optionally you can set some minimal metadata (or leave as is)
    new_nb.metadata = {
        "kernelspec": src_nb.metadata.get("kernelspec", {}),
        "language_info": src_nb.metadata.get("language_info", {}),
    }

    # Save to destination file
    with open(dst_path, 'w', encoding='utf-8') as f:
        nbformat.write(new_nb, f)

    print(f"Copied and cleaned cells from {src_path} to {dst_path}")

# Example usage:
copy_cells_clean(
    "Nexus_Text_Processing_and_Generation.ipynb",  # Your source notebook
    "Nexus_Text_Processing_and_Generation_clean.ipynb"  # Your cleaned target notebook
)

