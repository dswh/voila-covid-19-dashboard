import nbformat

##read the notebooks
first_nb = nbformat.read('test/notebook_a.ipynb', 4)
second_nb = nbformat.read('test/notebook_b.ipynb', 4)

##create a new nb
final_nb = nbformat.v4.new_notebook(metadata=first_nb.metadata)

##concatenate the nbs
final_nb.cells = first_nb.cells + second_nb.cells

##saving the final nb
nbformat.write(final_nb, './test/final_merged.ipynb')
