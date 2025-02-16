import pytest
import ast
import importlib

# Test to check for file docstring
def test_file_docstring():
    with open('assignment.py', 'r') as file:
        tree = ast.parse(file.read())
    docstring = ast.get_docstring(tree)
    assert docstring is not None, "DMACC Student, there does not appear to be a docstring at the top of your file. Please add a docstring explaining what your code does."

# Test to check the output of 'measurements' function with a rectangle
def test_measurements_rectangle():
    from assignment import measurements
    rectangle = [2.1, 3.4]
    result = measurements(rectangle)
    expected = "Perimeter = 11.00 Area = 7.14"
    assert result == expected, f"DMACC Student, the function 'measurements' did not return the expected value for input {rectangle}. Expected '{expected}', but got '{result}'."

# Test to check the output of 'measurements' function with a square
def test_measurements_square():
    from assignment import measurements
    square = [3.5]
    result = measurements(square)
    expected = "Perimeter = 14.00 Area = 12.25"
    assert result == expected, f"DMACC Student, the function 'measurements' did not return the expected value for input {square}. Expected '{expected}', but got '{result}'."

if __name__ == "__main__":
    pytest.main()