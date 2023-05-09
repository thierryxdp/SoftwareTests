import unittest
import sys
sys.path.append("C:\\Users\\aalves\\Downloads\\TesteSoftware\\mutmut\\src")
from tri3 import TipoTriangulo

class InvalidTriangleTestCase(unittest.TestCase):

    def testAllSidesEqualZero(self):
        assert TipoTriangulo(0,0,0) == "invalido"
    
    def testFirstSideEqualZero(self):
        assert TipoTriangulo(0,1,2) == "invalido"
        
    def testSecondSideEqualZero(self):
        assert TipoTriangulo(2,0,1) == "invalido"
    
    def testSecondSideEqualZero(self):
        assert TipoTriangulo(2,1,0) == "invalido"

    def testFirstSideIsLessThanZero(self):
        assert TipoTriangulo(-1,2,3) == "invalido"
        
    def testSecondSideIsLessThanZero(self):
        assert TipoTriangulo(1,-2,3) == "invalido"
        
    def testThirdSideIsLessThanZero(self):
        assert TipoTriangulo(1,2,-3) == "invalido"
    
    def testAllSidesAreLessThanZero(self):
        assert TipoTriangulo(-2,-4,-9) == "invalido"
    
    def testSumOfTwoFirstSidesIsEqualTheThirdOne(self):
        assert TipoTriangulo(3,4,7) == "invalido"
        
    def testSumOfTwoLastSidesIsEqualThanFirstOne(self):
        assert TipoTriangulo(7,4,3) == "invalido"

    def testSumOfTwoFirstSidesIsBiggerThanThirdOne(self):
        assert TipoTriangulo(3,4,10) == "invalido"
    
    def testSumOfTwoLastSidesIsBiggerThanFirstOne(self):
        assert TipoTriangulo(10,4,3) == "invalido"

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
        
    def testAllSidesEqualOneAndTriangleIsValid(self):
        assert TipoTriangulo(1,1,1) == "equilatero"

if __name__ == "__main__":
    unittest.main() # run all tests