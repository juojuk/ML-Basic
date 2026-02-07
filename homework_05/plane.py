"""
Создайте класс `Plane`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload

class Plane(Vehicle):
    cargo: int
    max_cargo: int

    def __init__(self, max_cargo, weight=0, fuel=0, fuel_consumption=0):
        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, cargo: int):
        if self.cargo + cargo <= self.max_cargo:
            self.cargo += cargo
        else:
            raise CargoOverload('Превышена максимальная грузоподъемность самолета')
        
    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        return cargo
