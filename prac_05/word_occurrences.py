"""
Word Occurrences
Estimate: 30 minutes
Actual:
"""

word_to_count = {}
text = input("Text: ")
for word in text.split():
    word_to_count[word] = word_to_count.get(word, 0) + 1

for word in sorted(list(word_to_count)):
    print(f"{word} : {word_to_count[word]}")
