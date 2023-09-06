offensive_words = []

with open("offensive_words.txt","r") as file:
    for line in file:
        offensive_words.append(line.strip())


message = str(input("Enter the string\n"))


for words in offensive_words:
    message = message.replace(words,'*' * len(words))
print("\n"+message)