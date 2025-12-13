class Reverse:
    def __init__(self,r):
        self.r=r
    def reversed(self,w,reverse):
        self.w=w
        self.reverse=reverse
        reverse = w-1

w = str(input("Give a word "))
print(w.reversed())