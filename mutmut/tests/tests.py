import pytest
import sys
sys.path.append("C:\\Users\\aalves\\Downloads\\TesteSoftware\\mutmut\\src")
from tri3 import TipoTriangulo


@pytest.mark.parametrize('input, expected_result', [
    ([0,0,0], "invalido"),     #Year less than 1752 and multiple of 4
    ([0,0,2], "invalido"),      #Year less than 1752 and multiple of 4
    ([0,1,0], "invalido"),     #Year less than 1752 and multiple of 4
    ([1,0,0], "invalido"),      #Year less than 1752 and multiple of 4
    ([0,1,2], "invalido"), #Year less than 1752 and multiple of 4
    ([0,3,2], "invalido"),#Year less than 1752 and non-multiple of 4
    ([2,0,1], "invalido"), #Year greater than 1752 and multiple of 100
    ([2,1,0], "invalido"), #Year greater than 1752 and not a multiple of 4    
    ([-1,2,3], "invalido"),  #Year greater than 1752 and multiple of 4
    ([1,-2,3], "invalido"),  #Year greater than 1752 and multiple of 4
    ([1,2,-3], "invalido"),  #Year greater than 1752 and multiple of 4
    ([-2,-4,-9], "invalido"),  #Year greater than 1752 and multiple of 4
    ([3,4,7], "invalido"),  #Year greater than 1752 and multiple of 4
    ([7,4,3], "invalido"),   #Year greater than 1752 and multiple of 4
    ([3,7,4], "invalido"),  #Year greater than 1752 and multiple of 4
    ([3,4,10], "invalido"),  #Year greater than 1752 and multiple of 4
    ([10,4,3], "invalido"),  #Year greater than 1752 and multiple of 400
])
def test_invalid(input, expected_result):
    
    actual = TipoTriangulo(*input) 
    assert  actual == expected_result

@pytest.mark.parametrize('input, expected_result', [
    ([3,4,5], "escaleno"),     #Year less than 1752 and multiple of 4
    ([6,8,7], "escaleno"),      #Year greater than 1752 and multiple of 400
])
def test_scalene(input, expected_result):
    
    actual = TipoTriangulo(*input) 
    assert  actual == expected_result
   
@pytest.mark.parametrize('input, expected_result', [
    ([3,3,4], "isosceles"),     #Year less than 1752 and multiple of 4
    ([6,8,6], "isosceles"),     #Year less than 1752 and multiple of 4
    ([9,5,5], "isosceles"),       #Year greater than 1752 and multiple of 400
])
def test_isosceles(input, expected_result):
    
    actual = TipoTriangulo(*input) 
    assert  actual == expected_result
        
@pytest.mark.parametrize('input, expected_result', [
    ([3,3,3], "equilatero"),     #Year less than 1752 and multiple of 4
    ([1,1,1], "equilatero"),     #Year greater than 1752 and multiple of 400
])
def test_equilateral(input, expected_result):
    
    actual = TipoTriangulo(*input) 
    assert  actual == expected_result