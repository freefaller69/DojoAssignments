# input
l = ['hello','world','my','name','is','Anna']
char = 'o'

n = []
for word in l:
    if char in word:
        print word
        n.append(word)
print n
