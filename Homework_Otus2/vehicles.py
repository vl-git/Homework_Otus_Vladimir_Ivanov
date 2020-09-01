from abc import ABCMeta, abstractmethod


class BaseVehicleABC(metaclass=ABCMeta):
    @abstractmethod
    def go(self, distance) -> str:
        raise NotImplementedError

    @abstractmethod
    def add_fuel(self, fuel_to_add):
        raise NotImplementedError

    @abstractmethod
    def repair(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def make_sound(self):
        raise NotImplementedError

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError


class BaseVehicle(BaseVehicleABC):
    _SOUND = ''
    _CONSUMPTION = 0
    _MAX_FUEL = 0
    _broken = False
    _NAME = ''

    def __init__(self,
                 speed: int,
                 weight: int,
                 fuel_type: str,
                 fuel: int,
                 color: str,
                 ):
        self.COLOR = color
        self.speed = speed
        self.weight = weight
        self.fuel_type = fuel_type
        self.fuel = fuel

    def make_sound(self):
        print(self._SOUND)

    def go(self, distance):
        fuel_to_go = distance * self._CONSUMPTION
        if fuel_to_go <= self.fuel:
            self.fuel -= fuel_to_go
            print(f' Going for {distance}. Fuel spent: {fuel_to_go}.\nFuel left: {self.fuel} ')
        else:
            print(f'Not enough fuel! You have to add {fuel_to_go - self.fuel}')
        # TODO: Add speed correlation, breaking conditions

    def add_fuel(self, fuel_to_add: int):
        print(f'Adding {fuel_to_add} fuel to {self._NAME}')
        self.fuel += fuel_to_add
        if self.fuel >= self._MAX_FUEL:
            print(f'Lost {self.fuel - self._MAX_FUEL}!')
            self.fuel = self._MAX_FUEL
        # TODO: Add exceptions
