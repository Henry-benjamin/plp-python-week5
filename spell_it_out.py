word = input("Enter a word: ")

for words in word:
    print(words)


for count, i in  enumerate(word, start=1):
    print(f"{i}.{count},")
    
print(len(word))