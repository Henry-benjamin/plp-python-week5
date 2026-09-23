word = input("Enter a word: ")

for words in word:
    print(words)


for i in  word:
    print(f"{word.index(i)}.{i},")
    
print(len(word))