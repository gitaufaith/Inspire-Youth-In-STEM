class car:
    def _init_(self,model,make,y_o_m, engine_capacity):
     self.model = model  
     self.make = make
     self.year = y_o_m
     self.engine_capacity =engine_capacity

#getters
    def get_model(self):
        return self.model
    def get_make(self):
        return self.make
    def get_year(self):
        return self.y_o_m
    def get_y_o_m(self):
       return self.engine_capacity
    
    #setters:set the attributes 
    def set_model(self,model):
       self.model=model
    def set_make(self,make):
       self.make=make
    def set_y_o_m(self,y_o_m):
       self.y_o_m=y_o_m

    def set_engine_capacity(self,engine_capacity):
       self.engine_capacity=engine_capacity

#obj:instance of the class

car1=("demio","nissan",2018,1300)
car2=("hilux","toyota",2019,2500)
car3=("passat","vw",2016,3300)

print(car1)
print(car2)
print(car3)

print(car1.self.model())
print(car1.get_y_o_m())

print(car2.get_make())
print(car2.get_y_o_m())

print(car3.get_model())
print(car3.get_y_o_m())



print(car3.get_y_o_m())
print(car1.get_y_o_m())







