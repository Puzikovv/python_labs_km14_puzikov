a = input("Enter the first phrase ")
first_phrase = set()  
for i in a:
    if i.isalpha():
        first_phrase.add(i.lower())
b = input("Enter the second phrase ")
second_phrase = set()
for i in b:
    if i.isalpha():
        second_phrase.add(i.lower())
print("Letters of first phrase: "+str(first_phrase))
print("Letters of second phrase: "+str(second_phrase))
if len(second_phrase - first_phrase) == 0:
    print("You can make second phrase")
else:
    print("You can`t make second phrase")