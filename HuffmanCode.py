from Node import *

class HuffmanCode:
	def calculate_freq(string):
		freq = {}

		for char in string:
			if char in freq:
				freq[char] += 1
			else:
				freq[char] = 1

		freq = sorted(freq.items(), key=lambda item: item[1])
		return freq

	def generate_node_tree(freq):
		nodes = []
		while len(freq) > 1:
			letter1, freq1 = freq[-1]
			letter2, freq2 = freq[-2]
			freq = freq[:-2]
			node = Node(letter1,letter2)
			nodes.append([node, freq1 + freq2])
		return nodes

