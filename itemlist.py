import re

def itemlist_replacer(md_snippet):
	thelines = md_snippet.splitlines()

	finallines = []
	indentstate = 0
	for i,line in enumerate(thelines):
		### Text replacer
		is_a_itemlist = re.match(r"^(\t)*\-\ ", line)
		if is_a_itemlist:
			prefixnumber = len(line.split("-")[0])+1
			if prefixnumber > indentstate:
				begins = prefixnumber - indentstate;
				for _ in range(begins):
					finallines.append(r"\begin{itemize}")
				finallines.append(line.replace("-",r"\item",1))
				indentstate = prefixnumber
			elif prefixnumber < indentstate:
				ends = indentstate - prefixnumber;
				for _ in range(ends):
					finallines.append(r"\end{itemize}")
				finallines.append(line.replace("-",r"\item",1))
				indentstate = prefixnumber
			else:
				finallines.append(line.replace("-",r"\item",1))
		else:
			prefixnumber = 0
			if prefixnumber < indentstate:
				ends = indentstate - prefixnumber;
				for _ in range(ends):
					finallines.append(r"\end{itemize}")
				finallines.append(line.replace("-",r"\item",1))
				indentstate = prefixnumber
			finallines.append(line)


	finalstring = "\n".join(finallines)
	return finalstring
