import re
import random
def main(str):
    word_list = str.split(" ")
    ans = []
    for word in word_list:
        if(len(word)>4):
            ans.append(word[0] + ''.join(random.sample(word[1:len(word)-1], len(word[1:len(word)-1]))) + word[len(word)-1])
        else: ans.append(word)
    ans = ' '.join(ans)
    print(ans)

main("I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
          

