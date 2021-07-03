import unittest

from ui import calc

class Test(unittest.TestCase):

    def setUp(self):
        self.calc = calc()

    def test_add(self):
            assert self.calc.calculate('0', '+', '1') == 1
            assert self.calc.calculate('2', '+', '3') == 5
            assert self.calc.calculate('4', '+', '5') == 9
    def test_add2(self):
            assert self.calc.calculate('-8', '+', '9') == 1
            assert self.calc.calculate('3', '+', '-4') == -1
            assert self.calc.calculate('4.0', '+', '2.5') == 6.5
            
    def test_subtraction(self):
            assert self.calc.calculate('2', '-', '9') == -7
            assert self.calc.calculate('-10', '-', '-4') == -6
            assert self.calc.calculate('7.2', '-', '5.3') == 1.9
            
    def test_division(self):
            assert self.calc.calculate('15', '/', '3') == 5
            assert self.calc.calculate('16', '/', '-4') == -4
            assert self.calc.calculate('0', '/', '2') == 0

    def test_multiplication(self):
            assert self.calc.calculate('1', '*', '2') == 2
            assert self.calc.calculate('-2', '*', '-4') == 8
            assert self.calc.calculate('-6', '*', '8') == -48
            assert self.calc.calculate('1', '*', '0') == 0
            assert self.calc.calculate('1.5', '*', '2.5') == 3.75
        
    def test_CalErrors(self):
            pass
      
if __name__ == "_main_":
    unittest.main()
