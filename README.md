# wordFinder
Finds all possible words based on a inputed string of letters

everyWord.py - Returns all possible words that can be made using the provided string of letters. 
               Finds words by generating every perumuation of the letter string 
               and comparing against a reference of 60,298 words. 
               
preprocess.py - Used to clean the master text file when adding words from various sources.
                Cleans dictionary reference text file by 
                            - removing duplicates 
                            - changing all items to lower case 
                            
splitDict.py - Used to split the reference text file to improve speed 
               - master reference file is split into small files based on word length 
               - spilt is arbitrary and based on frequecy of each word length
