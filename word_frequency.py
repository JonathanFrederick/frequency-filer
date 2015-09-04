import re

def word_frequency(text):
    count_dict = {}
    text = re.sub(r'[^a-z\s(\w\'\w)]+', '', text.lower()).split()#normalize text (no punctuation, no capitals)
#        print(line)
    for word in text:  #start counting dictionary
        if word in count_dict:
            count_dict[word] = count_dict[word]+1
        else:
            count_dict[word] = 1

#    print(count_dict)

#    for line in text:
#        print(line)
    return count_dict

def main():
    txt = open('sample.txt')#import file to string
    file_count = {}
    for line in txt:
        count = word_frequency(line)
#        print(count)
        for word in count:
            if word in file_count:
                file_count[word] = file_count[word]+count[word]
            else:
                file_count[word] = 1
#            file_count[word] = file_count[word] + line[word]
    #print(file_count)

    top_20 = list(zip(range(1,21),sorted(file_count, key=lambda d: file_count[d] , reverse=True)))#print top 20
    for w in top_20:
        print(str(w[0]).rjust(3), "-", w[1].ljust(8), "-", file_count[w[1]])


if __name__ == '__main__':
    main()
