#Task 6

words = ["the","quick","brown","fox","ate","my","chickens"]


def longest(words):
    longest_word = ""
    long = 0

    for word in words:
        if len(word) > long:
            long = len(word)
            longest_word = word
    
    return longest_word

print(longest(words))