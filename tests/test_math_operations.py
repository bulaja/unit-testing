import pytest

from src.math_operations import add, subtract


# Define test cases for addition as a list of input parameters and expected results
add_test_cases = [
    # Test case 1: Add two positive numbers
    ((2, 3), 5),

    # Test case 2: Add a positive and a negative number
    ((5, -2), 3),

    # Test case 3: Add two negative numbers
    ((-5, -2), -7),

    # Additional test cases can be added here
]


# Use the @pytest.mark.parametrize decorator to run the test function with different inputs
@pytest.mark.parametrize("input_args, expected_result", add_test_cases)
def test_add(input_args, expected_result):
    """
    Test the add function.

    Args:
        input_args (tuple): A tuple containing two numbers as input arguments.
        expected_result (float or int): The expected result of the addition.

    """
    # Unpack the input arguments
    a, b = input_args

    # Test addition
    assert add(a, b) == expected_result


subtract_test_cases = [
    # Test case 1: Subtract two positive numbers
    ((10, 3), 7),

    # Test case 2: Subtract a positive and a negative number
    ((5, -2), 7),

    # Test case 3: Subtract two negative numbers
    ((-5, -2), -3),

    # Additional test cases can be added here
]


# Use the @pytest.mark.parametrize decorator to run the test function with different inputs
@pytest.mark.parametrize("input_args, expected_result", subtract_test_cases)
def test_subtract(input_args, expected_result):
    """
    Test the subtract function.

    Args:
        input_args (tuple): A tuple containing two numbers as input arguments.
        expected_result (float or int): The expected result of the subtraction.

    """
    # Unpack the input arguments
    a, b = input_args

    # Test subtraction
    assert subtract(a, b) == expected_result
