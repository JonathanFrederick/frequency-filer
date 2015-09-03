import re

def word_frequency(text):
    for line in text:
        new_line = re.sub(r'[^a-z\s(\w\'\w)]', '', line.lower())#normalize text (no punctuation, no capitals)
        print(new_line)
    #start counting dictionary
    #print top 20
#    for line in text:
#        print(line)
    return {"hello": 1}

def main():
    txt = open('sample.txt')#import file to string

    word_frequency(txt)


if __name__ == '__main__':
    main()
