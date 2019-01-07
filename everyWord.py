import itertools
import winsound

  
# function that retruns all possible words given a 
# string of letters
def everyWord(letters):
    # dictionary reference to files containing all 
    #possible words of a given length
    # key = <filename> : item = lengths of words within
    directory = {
            "1_3.txt":[1,2,3], 
            "4_4.txt":[4], 
            "5_5.txt":[5], 
            "6_6.txt":[6], 
            "7_7.txt":[7], 
            "8_9.txt":[8, 9], 
            "10_11.txt":[10, 11], 
            "12_14.txt":[12, 13, 14], 
            "15_24.txt":[15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        }
    
    print("Checking combinations")

    # loops through permutation lengths, 
    # starting with the longest and stopping at 3
    for i in range(len(letters), 2, -1):
        # for each permutation length, sets the 
        #filename based on dictionary key
        for key, item in directory.items():
            if i in item:
                file = key

        # opens dictionary reference file, replacing newlines
        with open(file, 'r') as data:
            WORDS= (data.read().replace("\n"," ")).split(" ")
        # closes dictionary reference file 
        data.close()

        # using given user string and permutation length, 
        # calculates all possible permutations 
        perms = set(list(itertools.permutations(letters, i)))

        # cycles through all permutations 
        # checking for matches to words in given dictionary file 
        output= []
        for opti in perms:
            # joins permuation items into a string
            temp = "".join(opti)
            # checks permutation against dictionary
            if temp in WORDS:
                # appends matches to output list 
                output.append(temp)
        # prints all matches and an idicaiton of words length
        print (' ' + str(i) + '--' + str(sorted(output)))

# prompts user for a string of letters
everyWord(raw_input("Enter Letters: "))
# beeps to signal function completion 
winsound.Beep(800, 300)



