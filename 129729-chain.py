# https://quera.org/problemset/129729

class Chain:
    TYPES = [int, str]

    def __init__(self, value):
        self.value = value
        self._type = Chain.get_type(self.value)

    def __call__(self, value):
        _type = Chain.get_type(value)

        if (_type != self._type) or (_type not in Chain.TYPES):
            raise Exception('invalid operation')

        elif _type == str:
            self.value += f' {value}'

        elif _type == int:
            self.value += value
            if self.value == int(self.value):
                self.value = int(self.value)

        return self

    def __eq__(self, value):
        if isinstance(value, Chain):
            return self.value == value.value
        return self.value == value

    @staticmethod
    def get_type(value):
        if Chain.is_number(value):
            return int
        elif Chain.is_string(value):
            return str

    @staticmethod
    def is_number(value):
        if isinstance(value, int) or isinstance(value, float):
            return True
        return False

    @staticmethod
    def is_string(value):
        if isinstance(value, str):
            return True
        return False

    def __repr__(self):
        if self._type == str:
            return f"'{self.value}'"
        return str(self.value)
