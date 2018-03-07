#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string
import re

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated) 
        
        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        
        """


    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""

    ## Quiz 11
    
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)

        ### project part 2: comment out the line below
        ##words = text_string

        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        
        ##from nltk.tokenize import word_tokenize
        ##word_array = word_tokenize(text_string)
        ## Enero 29 
        word_array = text_string.split()
       
        tmp_count = 0
        stemmer = SnowballStemmer("english")
        ## Enero 29
        tmp_array = []
        for word in word_array:
            ## Enero 29
            no_space_word = word.strip()
            
            ##words += stemmer.stem(word).strip() + " "
            
            ## Enero 29
            stemmed_word = stemmer.stem(no_space_word)
            tmp_array.append(stemmed_word)
            ## stemmed_word = (stemmer.stem(word)).strip()
            ##print stemmed_word
            ## Enero 29
  
            
            ##stemmed_word = word_tokenize(stemmed_word)
            ##if tmp_count == len(word_array)-1:
               ##words += stemmed_word
            ##else:
                ##words += stemmed_word + " "

            tmp_count += 1
            
       
            
    
        
        
        
    ## Enero 29
    ## Apppend the word to words using a single space ' ' between words
    words = ' '.join(tmp_array)

    ##print words
    return words

    

def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print text



if __name__ == '__main__':
    main()

