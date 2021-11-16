import re

def fetch_text_and_add(line):
	path = line.replace("!!!include!!!","")
	file = open(path)
	stuff_to_add = file.read()
	file.close()
	begin = r"\begin{document}";
	endin = r"\end{document}"
	if begin in stuff_to_add:
		stuff_to_add = stuff_to_add.split(begin)[1].split(endin)[0]
	return stuff_to_add



def post_process(md_snippet):
	thelines = md_snippet.splitlines()

	finallines = []
	for i,line in enumerate(thelines):
		### Finds a post processing command
		is_a_bold = re.match(r"^\!\!\!include\!\!\!.+", line)
		if is_a_bold:
			finallines.append(fetch_text_and_add(line))
		else:
			finallines.append(line)

	finalstring = "\n".join(finallines)
	return finalstring