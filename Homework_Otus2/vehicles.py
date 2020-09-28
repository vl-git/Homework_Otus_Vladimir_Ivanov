from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
import errors
from random import choice


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


@dataclass
class Engine:
    engine_speed: int
    capacity: (int, float)
    started = False


@dataclass
class MusicSystem:
    song: str


class Car(BaseVehicle):
    _SOUND = 'BEEP'
    _CONSUMPTION = 10
    _MAX_FUEL = 200
    _max_amortization = 25
    _speed = 10
    _WEIGHT = 1000
    _WHEELS = 4
    _DOORS = 5
    engine = Engine(6000, 2)
    music_system = MusicSystem('ABBA - \"Waterloo\"')

    def __init__(self, name, color):
        super().__init__(name, color)
        self._amortization = self._max_amortization
        self._fuel = self._MAX_FUEL

    def play_music(self):
        print(f'playing: {self.music_system.song}')

    def start_engine(self):
        if not self._broken:
            self.engine.started = True
            print('Ready to drive')
        else:
            print('Repair your car!')

    def stop_engine(self):
        if not self.engine.started:
            print('The engine already stopped')
        else:
            self.engine.started = False

    def drive(self, distance):
        if self.engine.started:
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
        else:
            raise errors.StartError

    def __str__(self):
        return f'{self.name}:\n' \
               f'Characteristics: doors: {self._DOORS}, color = {self.color},' \
               f' {self._WHEELS} wheels, weight = {self._WEIGHT}\n' \
               f'Engine characteristics: {self.engine}\n' \
               f'Max fuel in tank: {self._MAX_FUEL}\n' \
               f'Fuel left: {self._fuel}\n' \
               f'Drives to repair: {self._amortization}'


class Sportcar(Car):
    _SOUND = 'Beep-beep'
    _CONSUMPTION = 15
    _MAX_FUEL = 150
    _max_amortization = 15
    _speed = 20
    _WEIGHT = 1250
    _WHEELS = 4
    _DOORS = 3
    engine = Engine(10000, 2.5)
    music_system = MusicSystem('Survivor - \"Eye of the tiger\"')
    _UPGRADED = False

    def __init__(self, name, color):
        super().__init__(name, color)

    def pit_stop(self):
        self.repair(only_full_repair=False)
        self.add_fuel(self._MAX_FUEL)

    def upgrade(self):
        if not self._UPGRADED:
            self._MAX_FUEL = 200
            self._CONSUMPTION = 20
            self._max_amortization = 20
            self._speed = 25
            self._UPGRADED = True
            print(f'{self.name} was successfully upgraded')
        else:
            print(f'{self.name} characteristics already upgraded')


class Boat(BaseVehicle):
    _COMPASS = ['North', 'South', 'West', 'East', 'Southwest', 'Northwest', 'Southeast', 'Northeast']
    _SOUND = 'WEE-WEE'
    _speed = 5
    _WEIGHT = 1000
    _started = False
    _SAIL = 1

    def __init__(self, name, color):
        super().__init__(name, color)

    def get_wind(self):
        wind = choice(self._COMPASS)
        return wind

    def drive(self, distance):
        raise errors.VehicleTypeError

    def set_sail(self):
        if self._started:
            print('Already set, ready for sail')
        else:
            self._started = True
            print('Ready for sail!')

    def sail(self, distance):
        if self._started:
            wind = self.get_wind()
            print(f'Sailing in the {wind} wind for {distance}. Arriving in {distance / self._speed}')
        else:
            raise errors.BoatStartError

    def __str__(self):
        return f'Boat \"{self.name}\":\n' \
               f'Characteristics: sail: {self._SAIL}, speed: {self._speed}, weight: {self._WEIGHT}' \
               f'color: {self.color}'


class SteamBoat(Boat, Car):
    _SOUND = 'WOO-WOO'
    _speed = 10
    _speed_engine = 20
    _WEIGHT = 2000
    _started = False
    _SAIL = 3
    _started_engine = False
    _engine = Engine(1000, 3)
    _MAX_FUEL = 500
    _CONSUMPTION = 10
    _WHEELS = 0
    _DOORS = 0

    def __init__(self, name, color):
        super().__init__(name, color)

    def drive(self, distance):
        if self.engine.started:
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
        else:
            raise errors.StartError

    def __str__(self):
        return f'Steamboat \"{self.name}\":\n' \
               f'Characteristics: sail: {self._SAIL}, speed on sail: {self._speed}, weight: {self._WEIGHT}\n' \
               f'color: {self.color}\n' \
               f'Engine characteristics: {self.engine}\n' \
               f'Speed on engine: {self._speed_engine}\n' \
               f'Max fuel in tank: {self._MAX_FUEL}\n' \
               f'Fuel left: {self._fuel}\n' \
               f'Drives to repair: {self._amortization}'


if __name__ == '__main__':
    '''car = Car('Ford', 'Cyan')
    print(car)
    car.start_engine()
    car.drive(15)
    car.add_fuel(100)
    car.repair(only_full_repair=False)
    car.play_music()

    sportcar = Sportcar('Porsche', 'Red')
    print(sportcar)
    sportcar.start_engine()
    sportcar.drive(5)
    sportcar.upgrade()
    sportcar.pit_stop()
    sportcar.drive(10)
    sportcar.play_music()
    sportcar.stop_engine()'''

    '''boat = Boat('Ann-Marie', 'White')
    boat.set_sail()
    boat.sail(50)
    boat.make_sound()'''

    steamboat = SteamBoat('Supreme', 'Black')
    print(steamboat)
    print()
    steamboat.set_sail()
    steamboat.sail(15)
    print()
    steamboat.start_engine()
    steamboat.drive(50)
    steamboat.add_fuel(200)
    steamboat.play_music()
