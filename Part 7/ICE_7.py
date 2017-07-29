from nltk.corpus import wordnet as wn

text ='Just as utilizing copies of the exponential or sine functions presents no problem to a spreadsheet or scientific calculator, substitution presents no real problem. You can create g(A10) in B10, and then f(B10) in C(10) and you have created the substituted value f(g(A10)) in C10. You can, by repeating this procedure, construct the most horrible looking combination of substitutions and arithmetical operations imaginable, and even worse than you could imagine, with very little difficulty, and you can find their numerical derivatives as well.\nBefore we go on to the last operation, we note that there is a great property associated with the operation of substitution. Just as we have found formulae above for finding the derivative of a sum or product or ratio of functions whose derivatives we know, we have a neat formula for the derivative of a substitution function in terms of the the derivatives of its constituents. Actually it is about as simple a formula for this as could be.\nThe result is often called the chain rule:'
words = text.split()

for synset in wn.synsets(words[0]):
    print(synset.definition())