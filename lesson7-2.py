class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_s(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Площадь общая ткани: {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round((self.width / 6.5 + 0.5), 2)

    def __str__(self):
        return f'Площадь на пальто: {self.square_c}'


class Suit(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_s = round((self.height * 2 + 0.3), 2)

    def __str__(self):
        return f'Площадь на костюм: {self.square_s}'

coat = Coat(18, 1.8)
suit = Suit(18, 1.8)
print(coat)
print(suit)
print(coat.get_sq_full)

