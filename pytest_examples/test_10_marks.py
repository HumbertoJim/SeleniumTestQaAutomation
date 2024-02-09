"""
pytest .\pytest_examples\test_10_marks.py -v -s -k "function_name"
pytest .\pytest_examples\test_10_marks.py -v -s -k "not function_name"
pytest .\pytest_examples\test_10_marks.py -v -s -m "mark_name"
pytest .\pytest_examples\test_10_marks.py -v -s -m "not mark_name"
Example:
pytest .\pytest_examples\test_10_marks.py -v -s -m "mark_name"
"""
import pytest

@pytest.mark.sales_module
def test_one():
    print("test one")
    
@pytest.mark.sales_module
def test_two():
    print("test two")
    
@pytest.mark.sales_module
def test_three():
    print("test three")
    
@pytest.mark.report_module
def test_four():
    print("test four")

@pytest.mark.report_module
def test_five():
    print("test five")
    
@pytest.mark.report_module
def test_six():
    print("test six")

@pytest.mark.skip
def test_seven():
    print("test seven")