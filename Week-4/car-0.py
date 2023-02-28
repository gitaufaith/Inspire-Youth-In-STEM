#init method or constructor
class car ():
    def __init__(self,model,colour):
        self.model = model
        self.colour = colour
        def  show(self):
         print("model is",self.model)
        print("colour is",self.colour)

            #both objects have different self which contain their attributes
        audi=car("audi a4","blue")
        ferrari=car("ferrari 488","green")

        audi.show()  #same output as car.get(audi)
        ferrari.show()  #same output as car.get(ferrari)
             
        print("model for audi is ",audi.model)
        print("colour for ferrari is",ferrari.colour)
