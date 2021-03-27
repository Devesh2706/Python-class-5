class Laptop(object):


    def __init__(self,ram,processor,graphics_card):
        self.ram = ram
        self.processor = processor
        self.graphics_card = graphics_card


    def printram(self):
        print ("Your laptop's ram is " + self.ram)


    def printprocessor(self):
        print ("Your laptop's processor is " + self.processor)

    def printgraphics_card(self):
        print ("Your latop has " + self.graphics_card)





Asus = Laptop("16 gigs","Amd ryzhen 7","RTX 3080 ti")

Asus.printgraphics_card()
        
