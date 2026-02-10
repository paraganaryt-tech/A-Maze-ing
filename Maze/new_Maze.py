from enum import IntFlag
from dataclasses import dataclass


class Wall(IntFlag):  # rah walo ghir 3la wd l7youta
    NONE = 0
    NORTH = 1
    EAST = 2
    SOUTH = 4
    WEST = 8
    ALL = 15


@dataclass   # decoration bach nsahlo lkhdma
class Cell:
    x: int   # type hints rah walo
    y: int
    walls: Wall = Wall.ALL  # hadi type hint o fnfs lw9t default value
    is_visited: bool = False  # tahadu li kibanu lk huka may5al3ukch
    is_42: bool = False


class MazeGenerator:  # mhm hadchi rah bayen o wade7
    """
    Mouhim haya lmandatory mal9it fin nkteb comment drt docstr hhhhh
    """
    def __init__(self, height, width, entry, exit):
        self.height = height
        self.width = width
        self.entry = entry
        self.exit = exit
        self._cells: list[list[Cell]] = []  # type hint maday39kch
        self._init_cells()

    def _init_cells(self):  # nasser hado protected akhouya
        """
        Hadi fiha dik lcomrehension akhouya at5rb9ek shwya aswel AI
        aynaddik fiha ana anmout bn3as
        """
        self._cells = [[Cell(x=x, y=y) for x in range(self.width)]
                       for y in range(self.height)]  # comprehension ez

    def _get_cell(self, x: int, y: int):  # tahadi protected
        if 0 <= x < self.width and 0 <= y < self.height:
            return self._cells[y][x]
        return None

    def _get_the_ways(self, current_cell: Cell):  # 9ra smit lmethod atfhm
        """
        Hadi ba9i na9esha checki l bool ze3ma wach l7ayt deja visited ola la
        o checki tadik 42 walkin machi daba tansaliw had l7ama9
        """
        ways_around = []  # ba9i khassa chi l3ibat had lmethod
        north_way = self._get_cell(current_cell.x, current_cell.y - 1)
        if north_way is not None:
            ways_around.append(north_way)
        east_way = self._get_cell(current_cell.x + 1, current_cell.y)
        if east_way is not None:
            ways_around.append(east_way)
        south_way = self._get_cell(current_cell.x, current_cell.y + 1)
        if south_way is not None:
            ways_around.append(south_way)
        west_way = self._get_cell(current_cell.x - 1, current_cell.y)
        if west_way is not None:
            ways_around.append(west_way)
        return ways_around

# kmel chwya abinma mchit n3ast o fa9t anode ankmel lamafhtich chi haja 
#  9sed l ai o goulih ichre7 lk wla chi l3iba