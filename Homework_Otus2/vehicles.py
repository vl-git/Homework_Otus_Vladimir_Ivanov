from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

class BaseVehicleABC(metaclass=ABCMeta):
    @abstractmethod
    def drive(self, distance):
        raise NotImplementedError

    @abstractmethod
    def add_fuel(self, fuel_to_add):
        raise NotImplementedError

    @abstractmethod
    def repair(self):
        raise NotImplementedError

    @abstractmethod
    def make_sound(self):
        raise NotImplementedError


class BaseVehicle(BaseVehicleABC):
    _SOUND = ''
    _CONSUMPTION = 0
    _MAX_FUEL = 0
    _broken = False
    _max_amortization = 0
    _speed = 0
    _WEIGHT = 0

    def __init__(self,
                 name,
                 color,
                 ):
        self.name = name
        self.color = color
        self._fuel = self._MAX_FUEL
        self._amortization = self._max_amortization

    def make_sound(self):
        print(self._SOUND)

    def drive(self, distance):
        fuel_to_go = distance * self._CONSUMPTION
        if fuel_to_go <= self._fuel:
            self._fuel -= fuel_to_go
            if self._amortization > 0:
                self._amortization -= 1
            elif self._amortization == 0:
                self._broken = True
                raise Exception(f'{self.name} needs to be repaired')
            print(f'Going {distance} ahead. Time to drive: {distance / self._speed}\n'
                  f'Fuel spent: {fuel_to_go}.\nFuel left: {self._fuel}\n'
                  f'Drives to next repair: {self._amortization}')
        else:
            print(f'Not enough fuel! You have to add {fuel_to_go - self._fuel}')

    def add_fuel(self, fuel_to_add: int):
        print(f'Adding {fuel_to_add} fuel to {self.name}')
        self._fuel += fuel_to_add
        if self._fuel >= self._MAX_FUEL:
            print(f'Lost {self._fuel - self._MAX_FUEL}!')
            self._fuel = self._MAX_FUEL

    def repair(self, only_full_repair=True):
        if self._broken:
            self._broken = False
            self._amortization = self._max_amortization
            print(f'{self.name} was successfully repaired')
        elif only_full_repair:
            print('It\'s not time yet!')
        else:
            self._amortization = self._max_amortization
            print(f'{self.name} was successfully repaired')


class Car(BaseVehicle):
    _SOUND = 'BEEP'
    _CONSUMPTION = 10
    _MAX_FUEL = 200
    _max_amortization = 25
    _speed = 10
    _WEIGHT = 1000
    _WHEELS = 4
    _DOORS = 5

    def __init__(self, name, color):
        super().__init__(name, color)
        self._amortization = self._max_amortization
        self._fuel = self._MAX_FUEL

    def __str__(self):
        return f'{self.name}:\n' \
               f'Characteristics: doors: {self._DOORS}, color = {self.color},' \
               f' {self._WHEELS} wheels, weight = {self._WEIGHT}\n' \ 
               f'Max fuel in tank: {self._MAX_FUEL}\n' \
               f'Fuel left: {self._fuel}\n' \
               f'Drives to repair: {self._amortization}'


if __name__ == '__main__':
    car = Car('Ford', 'Cyan')
    print(car)
    car.drive(15)
    car.add_fuel(100)
    car.repair(only_full_repair=False)

