# ALL about country

class USA():
    def capital(self):
        print("Washington, D.C. is capital of USA")

    def type(self):
        print("USA is a developed country")

class Japan():
    def capital(self):
        print("Tokyo is the capital of Japan")
 
    def type(self):
        print("Japan is highly developed country")

objUSA = USA()
objJap = Japan()

for c in (objJap, objUSA):
    c.capital()
    c.type()