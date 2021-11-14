import re

MAX_HEADINGS = 5
HEADINGS = [r"\section{thetext}",
			r"\subsection{thetext}",
			r"\subsubection{thetext}",
			r"\paragraph{thetext}",
			r"\subparagraph{thetext}"]

def heading_replacer(md_snippet):
	thelines = md_snippet.splitlines()

	finallines = []
	for i,line in enumerate(thelines):
		### Heading replacer
		is_a_heading = re.match(r"^#+\ ", line)
		if is_a_heading:
			thestuff = line.split("#")
			headingind = min(0, len(thestuff[0:-1])-1 , MAX_HEADINGS-1)
			thetext = thestuff[-1].strip()
			finallines.append(HEADINGS[headingind].replace("thetext",thetext))
		else:
			finallines.append(line)

	finalstring = "\n".join(finallines)
	return finalstring


def inlinecode_replacer(md_snippet):
	thelist = md_snippet.split("`")
	finalthing = ""
	for i,snippet in enumerate(thelist):
		if i%2 == 0:
			finalthing += snippet
		else:
			finalthing += r"\texttt{"
			finalthing += snippet
			finalthing += r"}"
	return finalthing 

def total_inline_code_replacer(md_snippet):
	thelines = md_snippet.splitlines()

	finallines = []
	for i,line in enumerate(thelines):
		### Heading replacer
		if "`" in line:
			finallines.append(inlinecode_replacer(line))
		else:
			finallines.append(line)

	finalstring = "\n".join(finallines)
	return finalstring
