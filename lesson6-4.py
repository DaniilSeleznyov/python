class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for work car'
        else:
            return f'Speed of {self.name} is normal for work car'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


maserati = SportCar(180, 'Red', 'Maserati', False)
toyota = TownCar(69, 'Grey', 'Toyota', False)
tata = WorkCar(39, 'Orange', 'Tata', False)
ford = PoliceCar(110, 'White',  'Ford', True)

print(tata.turn_left())
print(f'When {toyota.turn_right()}, then {maserati.stop()}')
print(f'{tata.go()} with speed exactly {tata.show_speed()}')
print(f'{tata.name} is {tata.color}')
print(f'Is {maserati.name} a police car? {maserati.is_police}')
print(f'Is {tata.name}  a police car? {tata.is_police}')
print(maserati.show_speed())
print(toyota.show_speed())
print(ford.police())
print(ford.show_speed())
