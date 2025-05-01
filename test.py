import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_large_maze(self):
        num_cols = 100
        num_rows = 100
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_unbalanced_maze(self):
        num_cols = 30
        num_rows = 2
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m2._cells),
            num_cols,
        )
        self.assertEqual(
            len(m2._cells[0]),
            num_rows,
        )

    def test_maze_minimal_dimensions(self):
        m = Maze(0, 0, 1, 1, 10, 10)  # 1×1 maze
        self.assertEqual(len(m._cells), 1)
        self.assertEqual(len(m._cells[0]), 1)

    def test_negative_dimensions(self):
        num_cols = -10
        num_rows = -8
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), 0)

    def test_zero_cell_size(self):
        m1 = Maze(0, 0, 5, 5, 0, 0)
        self.assertEqual(len(m1._cells), 5)
        self.assertEqual(len(m1._cells[0]), 5)

    def test_zero_dimensions(self):
        m1 = Maze(0, 0, 0, 0, 10, 10)
        self.assertEqual(len(m1._cells), 0)


if __name__ == "__main__":
    unittest.main()