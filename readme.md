# PhD thesis
Sources for my PhD thesis: [La structuration dans les entités nommées](https://tel.archives-ouvertes.fr/tel-01772268/document).

Not very clean or anything, but it might be of some help, who knows?

There are two "flavours" (the first one might not be as up to date as the second one) of the PhD file:

- These_DUPONT_Yoann_2017.tex: this file will include multiple subfiles, its main purpose is to have the main file with a very readable plan;
- These_DUPONT_Yoann_2017-single_file.tex: the same file, but in a single source file, better for diffs with [latexdiff](https://www.ctan.org/tex-archive/support/latexdiff).

Single_file is a tad bit cleaner, might be better to use this one.

# Compile

On Windows:

```
.\compile.bat <file_name_no_extension>
```

On Linux, Unix, whatever:

```
./compile.sh <file_name_no_extension>
```

And CR your way through warnings and stuff... Sorry.


# Other files

- `xml.sty`: a style sheet for XML data (listings was not good enough for what I wanted to do).
- `insert_subfiles.py`: a script to put back together subfiles into a "main" file. Dirty, not configurable (no CL parsing) and python2, but might be useful nonetheless.


More will come later, I guess.


# About margins

My margins are not as correct as they could be, apparently, it would have been more conventional (for my "École Doctorale" at least) to use:

```
\geometry{
    top=20mm,
    bottom=30mm,
    left=25mm,
    right=25mm,
    head=15mm,
    foot=20mm
}
```
