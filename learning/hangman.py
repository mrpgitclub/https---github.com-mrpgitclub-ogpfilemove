import random as r
l1 = open('items.txt',r)
l2 = l1.split()
l4,l5,l6,l7 = []

for w in l2:
    if len(w) < 4 or len(w) > 7 : pass
    elif len(w) == 4: l4.append(w)
    elif len(w) == 5: l5.append(w)
    elif len(w) == 6: l6.append(w)
    elif len(w) == 7: l7.append(w)



letter = ""
word = ""
