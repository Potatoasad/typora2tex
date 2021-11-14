import re
import subprocess
import glob

def inkscape_convert_svg_to_eps(imagepath):
	globpath = imagepath + "*.svg"
	for file in glob.glob(globpath):
		command = ['inkscape', file]
		command += ['-o',file.replace(".svg",".eps")]
		command += ['--export-ignore-filters','--export-ps-level=3']

		process = subprocess.run(command,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def images_replacer(md_snippet):
	thelines = md_snippet.splitlines()

	include_mod = r"[width=\textwidth,height=\textheight,keepaspectratio]"

	finallines = []
	for i,line in enumerate(thelines):
		### images replacer
		is_a_heading = re.match(r"\!\[.*\]\(.*\)", line)
		if is_a_heading:
			imagename = line.split("![")[0].split("]")[0]
			imagepath = line.split("](")[1].split(")")[0]
			imagepath = imagepath.replace(".svg",".eps")
			finallines.append(r"\begin{figure}[h]")
			finallines.append(r"\includegraphics"+include_mod+"{" + imagepath + r"}")
			finallines.append(r"\caption{" + imagename + r"}")
			finallines.append(r"\centering")
			finallines.append(r"\end{figure}")
		else:
			finallines.append(line)

	finalstring = "\n".join(finallines)
	return finalstring