import pytest
import sys
sys.path.append("C:\\Users\\aalves\\Downloads\\TesteSoftware\\banco\\src")
from main import banco


@pytest.mark.parametrize('input, expected_result', [
    # ([3, [
    #     (0 ,10),
    #     (0 ,10),
    #     (0 ,10),
    #     (3 ,10),
    #     (5 ,10),
    #     (7 ,10),
    #     (11, 10),
    #     (13, 10),
    #     (14, 10),
    #     (15, 10),
    #     (16, 10),
    #     (17, 10),
    #     (18, 3),
    #     (19, 10),
    #     (20, 10),
    #     (23, 3)
    #     ]], 2),
    ([1, [(0, 10),
        (0, 10),
        (1, 10),
        (2, 10),
        (30, 10)]], 1)
    ])
def test_invalid(input, expected_result):
    
    actual = banco(*input) 
    assert  actual == expected_result