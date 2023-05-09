import unittest
import sys
sys.path.append('../')
from TriangleTypeBusiness.TipoTrianguloDefeituoso1 import TipoTriangulo
class InvalidTriangleTestCase(unittest.TestCase):

    def testAllSidesEqualZero(self):
        assert TipoTriangulo(0,0,0) == "invalido"

    def testFirstSideIsLessThanZero(self):
        assert TipoTriangulo(-1,2,3) == "invalido"
    
    def testAllSidesAreLessThanZero(self):
        assert TipoTriangulo(-2,-4,-9) == "invalido"
    
    def testSumOfTwoFirstSidesIsEqualTheThirdOne(self):
        assert TipoTriangulo(3,4,7) == "invalido"

    def testSumOfTwoFirstSidesIsBiggerThanThirdOne(self):
        assert TipoTriangulo(3,4,10) == "invalido"

class ScaleneTriangleTestCase(unittest.TestCase):

    def testAllSidesDifferentWithLastSideBiggerAndTriangleIsValid(self):
        assert TipoTriangulo(3,4,5) == "escaleno"

    def testAllSidesDifferentWithSecondSideBiggerAndTriangleIsValid(self):
        assert TipoTriangulo(6,8,7) == "escaleno"

class IsoscelesTriangleTestCase(unittest.TestCase):

    def testFirstTwoSidesEqualAndTriangleIsValid(self):
        assert TipoTriangulo(3,3,4) == "isosceles"

    def testFirstAndLastSidesEqualAndTriangleIsValid(self):
        assert TipoTriangulo(6,8,6) == "isosceles"
    
    def testSecondAndLastSidesEqualAndTriangleIsValid(self):
        assert TipoTriangulo(9,5,5) == "isosceles"

class EquilateralTriangleTestCase(unittest.TestCase):

    def testAllSidesEqualAndTriangleIsValid(self):
        assert TipoTriangulo(3,3,3) == "equilatero"

if __name__ == "__main__":
    unittest.main() # run all tests