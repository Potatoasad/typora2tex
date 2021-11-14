import sys
import argparse
import pkg_resources
import os

from table import *
from itemlist import *
from multiline_equations import *
from headings import *
from images import *

def main():
	cwd = os.getcwd()

	#### PARSING COMMAND LINE ARGUMENTS

	template_help = """
	Sets the default template to work with. 
	Should end with .tex to be interpreted as a custom tex template document
	Should be one of 
		1. article
	For the typical default templates
	"""

	parser = argparse.ArgumentParser(description='Convert Typora Markdown files to LaTeX')
	parser.add_argument('filename', metavar='filename', type=str,
	                    help='the path to / name of the markdown file')
	parser.add_argument("-o","--outputfile", dest='outputfile',default="THE_DEFAULT",
	                    help='sets the output file name and/or path)')
	parser.add_argument("-a","--author", dest='author',default="Asad Hussain",
	                    help="sets the author name. The default name is mine .. hehe")
	parser.add_argument("-p","--template", dest='templatefile',default="article",
	                    help=template_help.strip())
	parser.add_argument("-i","--imagesfolder", dest='imagesfolder',default="images",
	                    help=template_help.strip())

	args = parser.parse_args()

	inputfile = args.filename
	outputfile = args.outputfile
	imagesfolder = args.imagesfolder
	templatefile = args.templatefile

	#### GRAB THE IMAGES FOLDER AND CONVERT ALL THE IMAGES
	if imagesfolder == "images":
		if len(inputfile.split(r"/")) > 1:
			imagesfolder = inputfile.split(r"/")
			imagesfolder[-1] = r"images/"
			imagesfolder = r"/".join(imagesfolder)
		else:
			imagesfolder = r"./images/"
	else:
		if imagesfolder[-1] != r"/":
			imagesfolder += r"/"

	inkscape_convert_svg_to_eps(imagesfolder)

	#### USING IT TO GET THE MARKDOWN FILE

	if outputfile == "THE_DEFAULT":
		if len(inputfile.split(r"/")) > 1:
			outputfile = inputfile.split(r"/")
			outputfile[-1] = "output.tex"
			outputfile = r"/".join(outputfile)
		else:
			outputfile = r"./output.tex"

	file = open(inputfile)
	input_string = file.read()
	file.close()

	if (len(templatefile.split(".")) > 1) and (templatefile.split(".")[1] == "tex"):
		file = open(templatefile)
		latex_template = file.read()
		file.close()
	else:
		latex_template = pkg_resources.resource_string(__name__, r'templates/'+templatefile+".tex")
	latex_template = latex_template.decode("ascii")

	#### CONVERTING THE DOCUMENT

	### FIND TITLE
	title = input_string.strip().split("#")[1].splitlines()[0].strip()

	### TABLES
	Table = TableConverter();

	output = Table.process_string(input_string)

	### ITEMLISTS
	output = itemlist_replacer(output)

	### MULTILINE EQUATIONS
	output = multiline_equation_replacer(output)

	### INLINE CODES
	output = total_inline_code_replacer(output)

	### HEADINGS
	output = heading_replacer(output)

	### IMAGES
	output = images_replacer(output)

	latex_template = latex_template.replace("THE_TITLE",title)
	latex_template = latex_template.replace("THE_AUTHOR","Asad Hussain")
	final = latex_template.replace("THE_BODY",output)

	with open(outputfile, "w") as text_file:
		text_file.write(final)

if __name__ == '__main__':
	main()

