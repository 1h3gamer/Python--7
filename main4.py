class flashcards:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word + '('+self.meaning+')'
    
flash = []
print("welcome to flashcard application")

while(True):
    word = input("Enter the word you want to add to your flashcard.")
    meaning = input("Enter the meaning of your card.")

    flash.append(flashcards(word,meaning))
    option = int(input("Enter 0, if you want to add another flashcard otherwise type 1."))

    if(option==1):
        break

print("\n Your flashcards")
for i in flash:
    print(">",i)