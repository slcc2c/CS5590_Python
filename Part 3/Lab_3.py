#1)
def toList():
    word = input('Please input a word')
    print(word.split(''),'\n',tuple(word))

#2)
def listOfTuples():
    user_input = ''
    l=[]
    while(user_input != q):
        user_input = input('enter first number')
        temp = user_input
        user_input = input('enter second number or type q to stop')
        l.append((temp,user_input))
    return sorted(l, key=lambda x:x[1])
