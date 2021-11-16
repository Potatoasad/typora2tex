import re

def inlinebold_replacer(md_snippet):
	thelist = md_snippet.split("__")
	finalthing = ""
	for i,snippet in enumerate(thelist):
		if i%2 == 0:
			finalthing += snippet
		else:
			finalthing += r"\textbf{"
			finalthing += snippet
			finalthing += r"}"
	return finalthing 

def total_inline_bold_replacer(md_snippet):
	thelines = md_snippet.splitlines()

	finallines = []
	for i,line in enumerate(thelines):
		### Bold replacer
		is_a_bold = re.search(r"\_\_.+\_\_", line)
		if is_a_bold:
			finallines.append(inlinebold_replacer(line))
		else:
			finallines.append(line)

	finalstring = "\n".join(finallines)
	return finalstring