import re

def word_frequency(text):
    count_dict = {}
    for line in text:
        line = re.sub(r'[^a-z\s(\w\'\w)]', '', line.lower())#normalize text (no punctuation, no capitals)
        for word in line.split():  #start counting dictionary
            if word in count_dict:
                count_dict[word] = count_dict[word]+1
            else:
                count_dict[word] = 1

    print(count_dict["the"])
#        print(new_line)


    #print top 20
#    for line in text:
#        print(line)
    return {"hello": 1}

def main():
    txt = open('sample.txt')#import file to string

    word_frequency(txt)


if __name__ == '__main__':
    main()
