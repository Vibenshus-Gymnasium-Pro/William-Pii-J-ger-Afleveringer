import time

def cleanword(word):
    
    blacklist = ["=", "[", "]", ")", "(", "-", ",", ".", ";", "!", "?", '"']
    cleanversion = ""
    for x in word:
        if x not in blacklist:
            cleanversion = cleanversion + x
    cleanversion = cleanversion.lower()
    return cleanversion



def wordfrequency(file, print_words = False):

    wordlist = {}
    longword_count = 0

    for line in file:
        for word in line.split():
            

            tempword = cleanword(word)
            if (tempword == ""):
                break

            if (tempword.__len__() >= 6):
                longword_count += 1
            
            if tempword in wordlist:
                wordlist[tempword] += 1
            else:
                wordlist[tempword] = 1

    if print_words:
        for words in wordlist:
            print("WORD:    " ,words, "  AMOUNT:   ", wordlist[words])


    amount_of_words = 0
    for word in wordlist:
        amount_of_words += wordlist[word]

    return amount_of_words, longword_count




def sentenceamount(file, print_words = False):
    punctuations = {".", "!", "?"}

    sentence_count = 0
    wordlist = {}
    last_sentence = {}


    for sentence in file:
        for word in sentence.split():
            stringsentence = True
            for x in (punctuations):
                if (x in word):
                    stringsentence = False


            if (stringsentence == True):
                last_sentence = "{} {}".format(last_sentence, word)

            if (stringsentence == False and last_sentence != ""):
                last_sentence = "{} {}".format(last_sentence, word)
                
                # Print debug
                if print_words:
                    print(last_sentence)
                
                sentence_count += 1
                last_sentence = ""

    return sentence_count

def main():

    amount_of_sentences = 0
    amount_of_words = 0
    amount_of_words_long = 0

    start_time = time.time()

    contents = {}
    with open('macbeth.txt', 'r') as f:
        contents = f.readlines()


    # 1st argument = contents/file, 2nd argument = print words/sentences (default: False)
    amount_of_words, amount_of_words_long = wordfrequency(contents)
    amount_of_sentences = sentenceamount(contents)

    print("Lixtal: " ,amount_of_words/amount_of_sentences + amount_of_words_long *100/amount_of_words, "\n")

    print("--- %s seconds ---" % (time.time() - start_time))


if (__name__ == "__main__"):
    main()