# 10
# -*- coding: utf-8 -*-

def main():
    f = open('popular_names.txt','r')
    data = f.read()
    print(data.count('\n'))
    f.close()

if __name__ == '__main__':
	main()