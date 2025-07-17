# https://quera.org/problemset/129729


class Chain:
    TYPES = (float, str)

    def __init__(self, value):
        if isinstance(value, int):
            value = float(value)

        if not isinstance(value, self.TYPES):
            raise Exception('invalid operation')

        self.value = value

    @property
    def datatype(self):
        return type(self.value)

    def __call__(self, value):
        other = type(self)(value)
        return self + other

    def __add__(self, other):
        cls = type(self)
        if not isinstance(other, cls):
            other = cls(other)

        if self.datatype != other.datatype:
            raise Exception('invalid operation')

        if self.datatype == str:
            return cls(self.value + ' ' + other.value)
        elif self.datatype == float:
            return cls(self.value + other.value)

    def __eq__(self, value):
        if isinstance(value, type(self)):
            value = value.value
        return self.value == value

    def __repr__(self):
        if self.datatype == str:
            return f"'{self.value}'"
        elif (self.datatype == float) and self.value.is_integer():
            return str(int(self.value))
        return str(self.value)
