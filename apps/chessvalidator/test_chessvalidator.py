import unittest
import chessvalidator

class TestChessValidator(unittest.TestCase):

    def test_isValidChessBoard(self):
        self.assertTrue(chessvalidator.isValidChessBoard({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}))
        self.assertTrue(chessvalidator.isValidChessBoard({'1h': 'bking', '3e': 'wking'}))
        self.assertTrue(chessvalidator.isValidChessBoard({'2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '3d': 'wking'}))
        self.assertTrue(chessvalidator.isValidChessBoard({'1h': 'bking', '7c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}))
        self.assertTrue(chessvalidator.isValidChessBoard({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}))


if __name__ == '__main__':
    unittest.main()