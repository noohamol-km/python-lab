s = input("Enter a sentence:")
print(s)
wordList = s.split()
print(wordList)
#Use set to get unique words
uniqueWords = set(wordList)
for word in uniqueWords:
    print(f"{word}occurs{wordList.count(word)}times")
