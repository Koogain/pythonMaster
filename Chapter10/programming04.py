class Car:
    def __init__(self, model, fuel):
        self.model = model
        self.fuelefficiency = fuel

    def get_model(self):
        return self.model

    def get_fuel_efficiency(self):
        return self.fuelefficiency

class Gasolinecar(Car):
    def __init__(self, model, fuel, displacement, co2):
        super().__init__(model,fuel)
        self.displacement = displacement
        self.co2emission = co2

    def get_dispacement(self):
        return self.displacement

    def get_co2emission(self):
        return self.co2emission

class Electriccar(Car):
    def __init__(self, model, fuel, battery):
        super().__init__(model, fuel)
        self.battery_capacity = battery

    def get_battery_capcity(self):
        return self.battery_capacity

car1 = Gasolinecar('GV80', 13, 2150, 160)
print(car1.get_model(), ':', car1.get_co2emission())

car2 = Electriccar('GV99', 4.5, 77)
print(car2.get_model(), ':', car2.get_battery_capcity())