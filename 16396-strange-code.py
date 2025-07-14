# https://quera.org/problemset/16396

class Foo:
        def __init__(self):
                self._x = 0

        @property
        def x(self):
                return self._x

        @x.setter
        def x(self, value):
                if value < 0:
                        self._x = -1
                else:
                        self._x = value % 100
