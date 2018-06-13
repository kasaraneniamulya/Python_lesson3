sen=input("PLease enter a sentence") #input sentence
words=sen.split()                    #input sentence is splitted into words
wordsdic=dict()
for i in words:                       #loop for all words in sentence
    if i in wordsdic:                  #(first word is hello it is not in the dictionary so it goes to else statement
        wordsdic[i]+=1                 #when comes to last word it is already in the dictionary so if statement gets executed)
    else:
        wordsdic[i] = 1
for key in sorted(wordsdic):           #words in wordsdic are sorted and are displayed as key values
    print("%s: %s" % (key, wordsdic[key]))