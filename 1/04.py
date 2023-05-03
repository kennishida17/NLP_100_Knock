# 04
# -*- coding: utf-8 -*-
import re

def main():
	str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
	str = re.sub('[,/.]','',str)
	word_list = str.split()
	initial_only_number = [1, 5, 6, 7, 8, 9, 15, 16, 19]
	ans = {}
	for i in range(len(word_list)):
		if i+1 in initial_only_number:
			ans[(word_list[i])[:1]] = i+1
		else:
			ans[(word_list[i])[:2]] = i+1
	return print(ans)
if __name__ == '__main__':
	main()