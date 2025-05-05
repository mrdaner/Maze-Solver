import time
import random
from cell import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        if self._cells and len(self._cells) > 0 and len(self._cells[0]) > 0:
                self._break_walls_r(0, 0)
                self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        x2 = self._x1 + (i + 1) * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        y2 = self._y1 + (j + 1) * self._cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        if not self._cells or not self._cells[0]:
            return

        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False

        exit_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        exit_cell.has_bottom_wall = False

        self._draw_cell(0, 0)
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        if not self._cells or i >= len(self._cells) or j >= len(self._cells[0]) if self._cells else 0:
            return
        self._cells[i][j].visited = True
        while True:
            not_visited = []
            if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                not_visited.append((i+1, j, "right"))
            if j > 0 and not self._cells[i][j-1].visited:
                not_visited.append((i, j-1, "up"))
            if i > 0 and not self._cells[i-1][j].visited:
                not_visited.append((i-1, j, "left"))
            if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
                not_visited.append((i, j+1, "down"))

            if len(not_visited) == 0:
                self._draw_cell(i, j)
                return
            
            idx = random.randrange(len(not_visited))
            next_i, next_j, direction = not_visited[idx]
            
            if direction == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
            elif direction == "up":
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            elif direction == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            elif direction == "down":
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False

            self._draw_cell(i, j)
            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
            self._animate()
            self._cells[i][j].visited = True
            if i == self._num_cols - 1 and j == self._num_rows - 1:
                return True
            
            if (
                i > 0
                and not self._cells[i][j].has_left_wall
                and not self._cells[i - 1][j].visited
            ):
                self._cells[i][j].draw_move(self._cells[i - 1][j])
                if self._solve_r(i - 1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i - 1][j], True)

            if (
                i < self._num_cols - 1
                and not self._cells[i][j].has_right_wall
                and not self._cells[i + 1][j].visited
            ):
                self._cells[i][j].draw_move(self._cells[i + 1][j])
                if self._solve_r(i + 1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i + 1][j], True)

            if (
                j > 0
                and not self._cells[i][j].has_top_wall
                and not self._cells[i][j - 1].visited
            ):
                self._cells[i][j].draw_move(self._cells[i][j - 1])
                if self._solve_r(i, j - 1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j - 1], True)

            if (
                j < self._num_rows - 1
                and not self._cells[i][j].has_bottom_wall
                and not self._cells[i][j + 1].visited
            ):
                self._cells[i][j].draw_move(self._cells[i][j + 1])
                if self._solve_r(i, j + 1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j + 1], True)
            return False