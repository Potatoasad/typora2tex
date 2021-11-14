import subprocess
import re

class TableConverter:

	def __init__(self):
		pass

	def table_finder(self,md_snippet):
		thelines = md_snippet.splitlines()
		thelines += [" "]

		# Finding all the lines where we have |---|
		tablelines = []
		for i,a in enumerate(thelines):
			result = re.match(r"\|[\ -]+\|",a)
			if result:
				tablelines.append(i)

		tablestructure = []
		for i in tablelines:
			MAX_ITERS = 50
			for n in range(1,MAX_ITERS):
				currentline = thelines[i+n]
				endoftable = re.match(r".*\|$",currentline.strip())
				if not endoftable:
					tablestructure.append([i-1 , i+n-1])
					break
					tablesnippets
		tablesnippets = []
		for i0,i1 in tablestructure:
			#initialsnippet = "\n".join(thelines[k] for k in range(i0,i1+1))
			finalsnippet = "\n".join(thelines[k] for k in range(i0,i1+1))
			tablesnippets.append((i0,i1,finalsnippet))
		return tablesnippets

	def pandoc_convert_to_string(self,md_snippet):

		command = ['pandoc']
		command += ['-f','markdown']
		command += ['-t','latex']

		process = subprocess.Popen(command, 
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE)

		output = process.communicate(input=md_snippet.encode("ascii"))
		result = output[0].decode("ascii") 

		return result


	def preprocess_math(self, md_snippet):
		return md_snippet.replace("$","xmathx$")

	def postprocess_math(self, md_snippet):
		return md_snippet.replace(r"xmathx\(", "$").replace(r"xmathx\)", "$")

	def process_string(self, md_snippet):
		tablesnippets = self.table_finder(md_snippet)
		alltables = []
		for i,j,table_snippet in tablesnippets:
			pre_processed = self.preprocess_math(table_snippet)
			processed = self.pandoc_convert_to_string(pre_processed)
			post_processed = self.postprocess_math(processed)
			alltables.append([(i,j,table_snippet,post_processed)])
			md_snippet = md_snippet.replace(table_snippet, post_processed)
		return md_snippet
