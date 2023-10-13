"""
Word Occurrences
Estimate: 30 minutes
Actual: 18 minutes
"""

max_word_length = 0
word_to_count = {}
text = input("Text: ")
for word in text.split():
    word_to_count[word] = word_to_count.get(word, 0) + 1
    if len(word) > max_word_length:
        max_word_length = len(word)

for word in sorted(list(word_to_count)):
    print(f"{word:{max_word_length}} : {word_to_count[word]}")
