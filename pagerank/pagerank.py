#Python 3.0
import re
import os
import collections
import time
#import other modules as needed

class pagerank:
	def __init__(self,file_name):
		# instantiate class level members
		self.transition_matrix = None
		self.eigenvector = None
		self.input_file = file_name
		self.total_pages = self.total_links = None
		self.build_transition_matrix()
		self.links_by_page = None

	"""
		This function builds the transition matrix and the initial vector
		used by pagerank

		We open the file and parse the input and build the matrix based on
		src -> dst links
	"""
	def build_transition_matrix(self):
		content = open(self.input_file, "r+").readlines()
		self.total_pages = int(content[0])
		self.total_links = int(content[1])
		# dictionary to store the number of outgoing links for each page
		self.links_by_page = {k:0 for k in range(self.total_pages)}
		# instantiate the transition matrix as an NxN matrix of all 0s
		self.transition_matrix = [[0]*self.total_pages for p in range(self.total_pages)]
		# the eigenvector is 1/total_pages for each entry
		self.eigenvector = [1/self.total_pages for p in range(self.total_pages)]

		# parse the src dst pairs from the input file and modify the transition_matrix accordingly
		for i in range(2,len(content)):
			# remove white space characters
			cleaned = [x for x in content[i] if x.isdigit()]
			src, dst = int(cleaned[0]),int(cleaned[1])
			self.links_by_page[src] += 1
			self.transition_matrix[src][dst] = 1
		# convert the transition matrix to a teleportation matrix
		# following the algorithm on slide 109 of lecture 9
		# alpha is 0.15
		for row in range(self.total_pages):
			for col in range(self.total_pages):
				if self.links_by_page[row] != 0:
					self.transition_matrix[row][col] = (self.transition_matrix[row][col]/self.links_by_page[row])*(0.85)+(0.15/self.total_pages)
				else:
					self.transition_matrix[row][col] = 1/self.total_pages
		print(self.transition_matrix)

	"""
		This is the naive implementation of matrix multiplication
	"""
	def matrix_multiply(self):
		res = [0 for x in range(self.total_pages)]
		for row in range(self.total_pages):
			temp = 0
			for col in range(self.total_pages):
				# dot product
				temp += self.eigenvector[col] * self.transition_matrix[col][row]
			res[row] = temp
		return res

	"""
		This function implements the pagerank algorithm

		We terminate when the pagerank vector has reached its steady state
	"""
	def pagerank(self):
		# instantiate temp vars
		old = self.eigenvector
		new = None
		# terminate when old vector == new vector
		# indicating that the principal eigenvector has been found
		while new != old:
			old=new
			new = self.matrix_multiply()
			self.eigenvector = new
		self.print_results()

	"""
		This function simply prints the results of the pagerank algorithm

		The output is ALSO written to the file: out.txt as the assignment instructions require
	"""
	def print_results(self):
		# store the eigenvector as a dictionary for sorting and retaining the page_id
		d = {k:self.eigenvector[k] for k in range(self.total_pages)}
		# sort the dictionary and save as a list
		d = sorted(d, key=d.get, reverse=False)
		out_file = open("out.txt", "w+")
		print("\nOutput for file  {}".format(self.input_file))
		out_file.write("\nOutput for file  {}\n".format(self.input_file))
		print("Using initial vector with value of 1/{} for each element".format(self.total_pages))
		out_file.write("Using initial vector with value of 1/{} for each element\n".format(self.total_pages))
		print("Doc	 Page Rank Score")
		out_file.write("Doc	 Page Rank Score\n")
		print("============================")
		out_file.write("============================\n")
		for i in d:
			print("{}	 {}".format(i,self.eigenvector[i]))
			out_file.write("{}	 {}\n".format(i,self.eigenvector[i]))
		print("============================\n")
		out_file.write("============================\n")
		out_file.close()

if __name__ == '__main__':
	p = pagerank("test1.txt")
	p.pagerank()
