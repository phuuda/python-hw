class Vehicle(object):
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year

class Bike(Vehicle):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        
class Bicycle(Bike):
    def __init__(self, manufacturer, model, year, b_type = 'mountain'):
        super().__init__(manufacturer, model, year)
        self.b_type = b_type
        
class Motorcycle(Bike):
    def __init__(self, manufacturer, model, year, m_type = 'sport'):
        super().__init__(manufacturer, model, year)
        self.m_type = m_type
        
    def sound(self):
        return 'Roar!'
        
class Car(Vehicle):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)

class Private_Car(Car):
    def __init__(self, manufacturer, model, year, c_type = 'sedan'):
        super().__init__(manufacturer, model, year)
        self.c_type = c_type
        
    def sound(self):
        return 'Vroooom!'

class Transporter(Car):
    def __init__(self, manufacturer, model, year, t_type = 'truck'):
        super().__init__(manufacturer, model, year)
        self.t_type = t_type
        
vehicles = [Motorcycle('BMW', 'F 700 GS', '2015'),
            Private_Car('Mazda', 'MX-5', '2008', 'roadster'),
            Motorcycle('Yamaha', 'V Star 250', '2008', 'cruiser')]

# Polymorphism -->
for vehicle in vehicles:
    print(vehicle.manufacturer + ' ' + 
          vehicle.model + ': ' + vehicle.sound())
