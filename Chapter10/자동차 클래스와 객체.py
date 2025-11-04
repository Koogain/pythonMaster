class Car:
    def __init__(self, model, fuelefficiency):
        self.__model = model
        self.__fuelefficiency = fuelefficiency

    def get_model(self):
        return self.__model

    def get_fuelefficiency(self):
        return self.__fuelefficiency

    def set_fuelefficiency(self, fuelefficiency):
        self.__fuelefficiency = fuelefficiency

    def get_fuelamount(self, distance):
        return distance / self.__fuelefficiency

car1 = Car('GV80', 12)
print('모델명: ', car1.get_model())
print('연비: ', car1.get_fuelefficiency())
distance = float(input('주행거리(km): '))
print('연료량: ', car1.get_fuelamount(distance))
