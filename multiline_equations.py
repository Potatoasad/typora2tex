def multiline_equation_replacer(md_snippet):
	thelist = md_snippet.split("$$")
	finalthing = ""
	for i,snippet in enumerate(thelist):
		if i%2 == 0:
			finalthing += snippet
		else:
			stripped = snippet.strip()
			if stripped[0:7] == r"\begin{":
				finalthing += snippet
			else:
				finalthing += "\n\\begin{align}"
				finalthing += snippet
				finalthing += "\\end{align}\n"
	return finalthing