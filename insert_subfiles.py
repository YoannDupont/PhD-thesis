import codecs, re

inputfilename = u"These_DUPONT_Yoann_2017.tex"
outpufilename = u"These_DUPONT_Yoann_2017-reference.tex"
subfile_re = re.compile(u"\\s+\\\\subfile\{(.+?)\}", re.U + re.M)

content = codecs.open(inputfilename, "rU", "utf-8").read()

parts = []
prev = 0
for subfile in subfile_re.finditer(content):
    start = subfile.start()
    end = subfile.end()
    latex_src = subfile.group(1) + ".tex"
    sub_content = u"".join(codecs.open(latex_src, "rU", "utf-8").readlines()[2:-1])
    parts.append(content[prev : start])
    parts.append(sub_content)
    prev = end
parts.append(content[prev : ])

with codecs.open(outpufilename, "w", "utf-8") as O:
    for part in parts:
        O.write(part)