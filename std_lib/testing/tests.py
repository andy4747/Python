import unittest
from functions import instance_counter,transpose_matrix,intersection
from bank import Bank, LowBalanceError

class TestFunctions(unittest.TestCase):

    def test_instance_counter(self):
        self.assertEqual(instance_counter([1,1,1,2,2,2,3,3,4,4,5]),{1:3,2:3,3:2,4:2,5:1})
        self.assertEqual(transpose_matrix([[1,2,3],[4,5,6]]),[[1,4],[2,5],[3,6]])
        self.assertEqual(intersection([1,2,3,4,5],[4,5,6,7,8]),[4,5])

    def test_transactions(self):
        anjal=Bank("anjal",1000)
        depo=anjal.deposit(500)
        draw=anjal.withdraw(600)
        self.assertEqual(depo,1500)
        self.assertEqual(draw,900)
        with self.assertRaises(LowBalanceError):
            anjal.withdraw(1000)

if __name__=='__main__':
    unittest.main()