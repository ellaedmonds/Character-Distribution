"""
distribution.py
Author: Ella Edmonds
Credit: https://stackoverflow.com/questions/9764298/is-it-possible-to-sort-two-listswhich-reference-each-other-in-the-exact-same-w/9764364

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
a = input ('Please enter a string of text (the bigger the better):')
print('The distribution of characters in "'+a+'" is:')

letters = []
freq = []
letter = ""
for c in "abcdefghijklmnopqrstuvwxyz":
    if c in a:
        letters.append(c)
        freq.append(a.count(c))

print(letters)
print(freq)

#order = list(zip(*sorted(zip(freq,letters))))

freq1,letters1 = (list(t) for t in zip(*sorted(zip(freq, letters))))

print(letters1)
print(freq1)

order = list((zip(freq1,letters1)))

print(order)

for c in order[::-1]:
    print(c[0]*c[1])
    



