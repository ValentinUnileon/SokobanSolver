import unittest
import main

class TestSokoban(unittest.TestCase):

    puzzle_lines = [
    ['X', 'X', 'X', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '\n'],
    ['X', 'X', 'X', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '\n'],
    ['#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '\n'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '!', '#', '#', '#', '#', '\n'],
    ['#', ' ', ' ', '@', '$', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '\n'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.', ' ', ' ', ' ', ' ', '#', '\n'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]


    puzzle_lines2 = [
    ['X', 'X', 'X', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '\n'],
    ['X', 'X', 'X', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '\n'],
    ['#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '\n'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '\n'],
    ['#', ' ', ' ', ' ', '$', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '@', ' ', '#', '\n'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.', ' ', ' ', ' ', ' ', '#', '\n'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]

    puzzle_lines3 = [
    ['X', 'X', 'X', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '\n'],
    ['X', 'X', 'X', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '\n'],
    ['#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '\n'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '\n'],
    ['#', ' ', ' ', ' ', '$', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '@', '$', ' ', '#', '\n'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', '#', '\n'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]


    def test_getCharPositionXY(self):
        self.assertEqual(main.getCharPositionXY(self.puzzle_lines), (3, 4))
        self.assertEqual(main.getCharPositionXY(self.puzzle_lines2), (15, 4))

    def test_isMovementValid(self):
        self.assertEqual(main.isMovementValid(15, 3, self.puzzle_lines2), False)
        self.assertEqual(main.isMovementValid(15, 5, self.puzzle_lines2), True)
        self.assertEqual(main.isMovementValid(15, 4, self.puzzle_lines3), False) #aunque tenga un punto en la horizontal a la que se va a mover el mov no es valido




if __name__ == '__main__':
    unittest.main()