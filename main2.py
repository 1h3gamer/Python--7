class India:
    def capital(self):
        print("New Dheli is the capital of India")
    def language(self):
        print("Hindi is mostly used")
    def type(self):
        print("It is a developing country")

class USA:
    def capital(self):
        print("Washington DC is the capital of USA")
    def language(self):
        print("English is mostly used")
    def type(self):
        print("It is a developed country")

obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()