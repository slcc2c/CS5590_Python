def char_freq(word):
    temp = str(word)
    freqs = {}
    for l in temp:
        if l in freqs:
            freqs[l]+=1
        else:
            freqs[l]=1
    return freqs
word = str(input("What word would you like the frequency of?"))
freqs = char_freq(word)
print("In the word ",word,":")
for k,v in freqs.items():
    print("The letter ",k," has a frequency of ",v)