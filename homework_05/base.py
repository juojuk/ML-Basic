"""
Доработайте класс `Vehicle`
"""

from abc import ABC
import math

from homework_05.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight: int = 0
    started: bool = False
    fuel: int = 0
    fuel_consumption: float = 10.000

    def __init__(self, weight: int, fuel: int, fuel_consumption: float):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                 raise LowFuelError('Недостаточно топлива для запуска двигателя')

    def move(self, distance: int):
        fuel_needed = math.ceil(distance * self.fuel_consumption)
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
        else:
            raise NotEnoughFuel('Недостаточно топлива для движения')