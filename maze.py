from graphics import Line, Point
from cell import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells(self)

    def _create_cells(self):
        self._cells = []
        for column in range(self._num_cols):
            column_cells = []
            for row in range(self._num_rows):
                column_cells.append(Cell(self._win))
            self._cells.append(column_cells)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):