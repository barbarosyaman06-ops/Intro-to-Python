#Object oriented programming

class Myclass:
  x=7 #property



obj=Myclass()
print(obj.x)





class Vehicle():
  brand="Chevrolet" #property(variable)
  model="Corvette" #property(variable)
  series="C5" #property(variable)
  make="1994" #property(variable)
  color="Devil Red" #property(variable)
  def __init__(self): #constructor method (a method created simoultensly with a class)
    pass

car_obj=Vehicle()
print("Brand: ", car_obj.brand)
print("Model: ", car_obj.model)
print("Series: ", car_obj.series)
print("Make: ", car_obj.make)
print("Color: ", car_obj.color)






class Series():
  def __init__(self, name,year,cast):
    self.name=name #instance variable
    self.year=year #instance variable
    self.cast=cast #instance variable

series_obj1=Series("Supernatural", 2005, "Jensen Ackles")
series_obj2=Series("Dexter",2005,"Micheal C. Hall")

print(series_obj1.name, "-", series_obj1.year, "-", series_obj1.cast)
print(series_obj2.name, "-", series_obj2.year, "-", series_obj2.cast)

