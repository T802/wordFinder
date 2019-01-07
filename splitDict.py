from itertools import chain
from glob import glob 



def freqDistro(master):
    #groups words by length, and visualizes the frequency of each group 

    # sort by length
    lenSorted = sorted(master, key=len)
    #get longest word  
    maxLen = len(lenSorted[-1])
    # create a list of each possible length
    groups = range(1, maxLen + 1)
    #convert list to dictionary wuth a default value of zero 
    distro = dict((k, 0) for k in groups)
    # tally the length of each word length 
    for i in range(1, maxLen + 1):
        for word in lenSorted:
            if len(word) == i:
                distro[i] += 1
    #print distrobution 
    #for key, item in distro.items():
        #print(str(key) + ": " + str(item))


# open dictionary reference file 
with open('resources/allWords.txt', 'r') as data:
    # replace newlines and read data as variable 
    WORDS= (data.read().replace("\n"," ")).split(" ")
# close dictionary file 
data.close()

#freqDistro(WORDS)
# lengths of words are grouped together to reduce search times
combo = [[1,2,3], [4], [5], [6], [7], [8,9], [10, 11], [12,13,14], [15,16,17,18,19,20,21,22,23,24]]

# cycles through each group
for group in combo:
    # initialize an empty list 
    temp = []
    #creates a filename based on the combined group range 
    filename = str(group[0]) + "_" + str(group[-1]) + ".txt"
    #searches for each word length in the dictionary 
    for num in group:
        for word in WORDS:
            if len(word) == num:
                # adds words to temperary list 
                temp.append(word)

    # opens/creates generated file name 
    with open(filename, 'w') as out:
        print("-Writing Lines to: " + filename)
        # writes dictionary words of certain length to file separated by newlines 
        for item in sorted(set(temp)):
            out.write("%s\n" % item)

        #closes file
        out.close()




