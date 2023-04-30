# 03
# -*- coding: utf-8 -*-
import re

def main():
	str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
	str = re.sub('[,/.]','',str)
	word_list = str.split()
	word_len_list = []
	for word in word_list:
		word_len_list.append(len(word))
	print(word_len_list)
if __name__ == '__main__':
	main()