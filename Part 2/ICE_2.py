def char_freq(word):
    temp = str(word)
    freqs = {}
    for l in temp:
        if l in freqs:
            freqs[l]+=1
        else:
            freqs[l]=1
    return freqs
word = str(input("What word would you like the frequency of? "))
freqs = char_freq(word)
print("In the word ",word,":")
for k,v in freqs.items():
    print("The letter ",k," has a frequency of ",v)

def longest_word(words):
    max_length = 0
    for word in words:
        if len(word)>max_length:
            max_length = len(word)
    return max_length
def get_words():
    words = []
    word = input("Please enter your first word or hit enter on a blank line to exit: ")
    while(word != ''):
        words.append(word)
        word = input("Please enter your another word or hit enter on a blank line to exit: ")
    return words
print(longest_word(get_words()))
