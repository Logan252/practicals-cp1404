"""estimated time 20 minutes
actual time: 14 minutes"""
word_to_count = {}
text = input("Text: ")

words = text.split()
for word in words:

    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

    words = list(word_to_count.keys())
    words.sort()
print(word_to_count)

#thing, width, other_thing = words, 13, 2
#print(f"{thing:{width}}  {other_thing}")