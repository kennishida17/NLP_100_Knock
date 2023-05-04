# 10
# -*- coding: utf-8 -*-

def main():
    f = open('popular_names.txt','r')
    for data in f:
        print(data.replace('\t',' '),end='')
    


if __name__ == '__main__':
	main()