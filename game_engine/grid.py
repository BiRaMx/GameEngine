class Grid:
    default_width: int = 10
    default_height: int = 10

    def __init__(self, *args, **kwargs):
        """
        Объект для работы с сеткой.
        Использование:
            Grid() -> width=default; height=default
            Grid(a) -> width=height=a
            Grid(a, b) -> width=a; height=b
            Grid(width=a) -> width=a; height=default
            Grid(height=b) -> width=default; height=b;
            Grid(width=a, height=b) -> width=a; height=b

        :param args: Список позиционных аргументов
        :param kwargs: Словарь именованных аргументов
        """

        self.width = Grid.default_width
        self.height = Grid.default_height

        if len(args) == 1:
            self.width = args[0]
            self.height = args[0]
        elif len(args) == 2:
            self.width = args[0]
            self.height = args[1]
        elif len(args) >= 3:
            raise TypeError("No more than 2 positional parameters"
                            f"were expected. Received {len(args)}")
        elif not args and kwargs:
            for key, val in kwargs.items():
                if key == "width":
                    self.width = val
                elif key == "height":
                    self.height = val
                else:
                    raise TypeError(f"Unknown parameter: {key}")
        elif kwargs:
            raise TypeError("Positional and keyword arguments cannot be used together")

    @classmethod
    def __verify_size(cls, size):
        if not isinstance(size, int):
            raise ValueError(f"Sizes must be integers. Got {type(size).__name__} instead")
        if size <= 0:
            raise ValueError(f"Size must be positive. Got {size} instead")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        try:
            Grid.__verify_size(value)
        except ValueError as err:
            raise ValueError("Wrong width parameter: " + str(err)) from None
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        try:
            Grid.__verify_size(value)
        except ValueError as err:
            raise ValueError("Wrong height parameter: " + str(err)) from None
        else:
            self.__height = value

    def snap(self, *args):
        """
        Возвращает ближайшее значение, прикрепленное к объекту Grid, к исходному
        :param args: Исходная точка
        :return:
        """
        if len(args) == 1:
            rx, ry = args[0]
        else:
            rx = args[0]
            ry = args[1]

        x = rx - rx % self.width
        y = ry - ry % self.height
        return x, y


def _test_grid_class():
    w_def = Grid.default_width
    Grid.default_width = 10
    h_def = Grid.default_height
    Grid.default_height = 10

    g = Grid()
    assert g.width == 10
    assert g.height == 10 

    g = Grid(30)
    assert g.width == 30
    assert g.height == 30

    g = Grid(20, 30)
    assert g.width == 20
    assert g.height == 30

    g = Grid(width=30)
    assert g.width == 30
    assert g.height == 10

    g = Grid(height=20)
    assert g.width == 10
    assert g.height == 20

    g = Grid(width=10, height=20)
    assert g.width == 10
    assert g.height == 20

    assert g.snap(0, 0) == g.snap((0, 0)) == (0, 0)
    assert g.snap(10, 20) == g.snap((10, 20)) == (10, 20)
    assert g.snap(20, 20) == g.snap((20, 20)) == (20, 20)
    assert g.snap(10, 40) == g.snap((10, 40)) == (10, 40)
    assert g.snap(20, 40) == g.snap((20, 40)) == (20, 40)

    assert g.snap(10, 15) == g.snap((10, 15)) == (10, 0)
    assert g.snap(15, 20) == g.snap((15, 20)) == (10, 20)
    assert g.snap(15, 15) == g.snap((15, 15)) == (10, 0)

    assert g.snap(-10, -20) == g.snap((-10, -20)) == (-10, -20)
    assert g.snap(-20, -20) == g.snap((-20, -20)) == (-20, -20)


    print("Grid class: all tests PASSED.")
    Grid.default_width = w_def
    Grid.default_height = h_def


if __name__ == '__main__':
    _test_grid_class()
