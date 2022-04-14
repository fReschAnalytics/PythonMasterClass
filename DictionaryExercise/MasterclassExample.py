# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}
 
# Text string
text = "Later in the course, you'll see how to use the collections Counter class."
 
# Your code goes here ...
text = text.casefold()

punctuation = ".,/?' "
for c in text:
    if c not in punctuation:
        word_count[c] = word_count.setdefault(c, 0) + 1
 
 
# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
