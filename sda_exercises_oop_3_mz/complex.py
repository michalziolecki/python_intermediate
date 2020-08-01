class MyComplex:

    def __init__(self, real: int, unreal=0):
        self._real = real
        self._unreal = unreal

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, value):
        self._real = value

    @property
    def unreal(self):
        return self._unreal

    @unreal.setter
    def unreal(self, value):
        self._unreal = value

    def show(self):
        print(f'{self._real} + {self._unreal}i')

    def __str__(self) -> str:
        return f'{self._real} + {self._unreal}i'

    def __eq__(self, value) -> bool:
        if isinstance(value, MyComplex):
            if self._real == value.real \
                    and self._unreal == value.unreal:
                return True
        return False

    def is_equal_to(self, real: int, unreal: int) -> bool:
        if self._real == real \
                and self._unreal == unreal:
            return True
        return False

    @classmethod
    def add_two_complex(cls, one: 'MyComplex', two: 'MyComplex') -> 'MyComplex':
        return cls(one.real + two.real, one.unreal + two.unreal)

    @classmethod
    def add_three_complex(cls, one: 'MyComplex', two: 'MyComplex', three: 'MyComplex') -> 'MyComplex':
        return cls(one.real + two.real + three.real, one.unreal + two.unreal + three.unreal)

    @classmethod
    def add_many_complex(cls, complex_list: list):
        real_value = 0
        unreal_value = 0

        for complex_val in complex_list:
            real_value = real_value + complex_val.real
            unreal_value = unreal_value + complex_val.unreal
        return cls(real_value, unreal_value)

    def add_by_values(self, real=0, unreal=0):
        self.real = self.real + real
        self.unreal = self.unreal + unreal
        return self

    def add(self, complex_value: 'MyComplex'):
        self.real = self.real + complex_value.real
        self.unreal = self.unreal + complex_value.unreal
        return self
