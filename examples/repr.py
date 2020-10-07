
class FirstName:
    __slots__ = __fields__ = 'first',
    def __init__(self, name):
        self.first = name

    def __repr__(self,):
        fields = ', '.join([repr(getattr(self, f)) for f in self.__fields__])
        return f'{type(self).__name__}({fields})'

class FullName(FirstName):
    __slots__ = __fields__ = *FirstName.__fields__, 'last'
    def __init__(self, first, last):
        super().__init__(first)
        self.last = last



if __name__ == '__main__':
    first = FirstName('Israel')
    full = FullName('Israel', 'Campiotti')

    print(f'{first = }')
    print(f'{full = }')