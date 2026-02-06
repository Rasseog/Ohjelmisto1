import random


class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"{'License':<10} {'Max':>5} {'Speed':>6} {'Distance':>10}")
        for car in self.cars:
            print(
                f"{car.license_plate:<10} "
                f"{car.maximum_speed:>5} "
                f"{car.current_speed:>6} "
                f"{car.travelled_distance:>10.1f}"
            )

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)
