@echo OFF

latex ${1}.tex
bibtex ${1}
latex ${1}.tex
latex ${1}.tex
dvips ${1}.dvi
ps2pdf -dAutoRotatePages#/None ${1}.ps

del ${1}.aux
del ${1}.bbl
del ${1}.blg
del ${1}.dvi
del ${1}.maf
del ${1}.out
del ${1}.ps
del ${1}.toc

del ${1}.mtc*
