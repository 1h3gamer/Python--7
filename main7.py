class Class_reverse:
    def __init__(self,r):
        self.r=r
    def reversed(self):
        return self.r[::-1]

word = input("Enter the word to be reversed : ")

rev_ob = Class_reverse(word)

result = rev_ob.reversed()

print("Reversed String :", result)