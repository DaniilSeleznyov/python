class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width * self.weight * self.roadbed*0.01


class MassCount(Road):
    def __init__(self, _length, _width, weight, roadbed):
        super().__init__(_length, _width)
        self.weight = weight
        self.roadbed = roadbed


r = MassCount(20, 5000, 25, 5)
print(r.mass())
