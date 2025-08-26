# #Task 3

words = ["Write","good","code","every","day"]

def columns(words):

    max_length = max(len(word) for word in words)  #Find the largest length of the words

    for i in range(max_length):
        row = ""
        for word in words:    #Loop  the words in the list and if the word is less than the max kength then print the letter else a space
            if i < len(word):
                row += word[i] + " "
            else:
                row += " "
        print(row)

columns(words)