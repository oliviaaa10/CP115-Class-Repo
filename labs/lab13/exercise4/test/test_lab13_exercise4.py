import subprocess
import sys
import os

def run_exercise4(*inputs):
    """Run exercise4.py with given inputs and return output lines."""
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    script_path = os.path.join(script_dir, 'exercise4.py')

    input_data = '\n'.join(str(x) for x in inputs) + '\n'

    result = subprocess.run([sys.executable, script_path],
                          input=input_data, text=True, capture_output=True)

    if result.returncode != 0:
        raise Exception(f"Script failed: {result.stderr}")

    lines = result.stdout.strip().split('\n')
    return lines[0], lines[1]

def test_only_positive_numbers():
    """Test with only positive numbers"""
    inputs = [5, 10, 3.5, 0]
    count, total = run_exercise4(*inputs)
    assert count == '3', f"Input: {inputs} | Expected: 3 | Got: {count}"
    assert total == '18.50', f"Input: {inputs} | Expected: 18.50 | Got: {total}"

def test_skip_negative_numbers():
    """Test that negative numbers are skipped"""
    inputs = [5, -3, 10, -7, 2, 0]
    count, total = run_exercise4(*inputs)
    assert count == '3', f"Input: {inputs} | Expected: 3 | Got: {count}"
    assert total == '17.00', f"Input: {inputs} | Expected: 17.00 | Got: {total}"

def test_mixed_positive_negative():
    """Test with mixed positive and negative numbers"""
    inputs = [10, -5, 20, -10, 30, 0]
    count, total = run_exercise4(*inputs)
    assert count == '3', f"Input: {inputs} | Expected: 3 | Got: {count}"
    assert total == '60.00', f"Input: {inputs} | Expected: 60.00 | Got: {total}"

def test_zero_stops_immediately():
    """Test that 0 stops the loop immediately"""
    inputs = [0]
    count, total = run_exercise4(*inputs)
    assert count == '0', f"Input: {inputs} | Expected: 0 | Got: {count}"
    assert total == '0.00', f"Input: {inputs} | Expected: 0.00 | Got: {total}"

def test_only_negative_then_zero():
    """Test with only negative numbers before zero"""
    inputs = [-5, -10, -3, 0]
    count, total = run_exercise4(*inputs)
    assert count == '0', f"Input: {inputs} | Expected: 0 | Got: {count}"
    assert total == '0.00', f"Input: {inputs} | Expected: 0.00 | Got: {total}"

def test_decimal_positive_numbers():
    """Test with decimal positive numbers"""
    inputs = [1.5, 2.5, 3.5, 0]
    count, total = run_exercise4(*inputs)
    assert count == '3', f"Input: {inputs} | Expected: 3 | Got: {count}"
    assert total == '7.50', f"Input: {inputs} | Expected: 7.50 | Got: {total}"

def test_single_positive():
    """Test with single positive number"""
    inputs = [42, 0]
    count, total = run_exercise4(*inputs)
    assert count == '1', f"Input: {inputs} | Expected: 1 | Got: {count}"
    assert total == '42.00', f"Input: {inputs} | Expected: 42.00 | Got: {total}"

def test_large_numbers():
    """Test with large positive numbers"""
    inputs = [1000, 2000, 3000, 0]
    count, total = run_exercise4(*inputs)
    assert count == '3', f"Input: {inputs} | Expected: 3 | Got: {count}"
    assert total == '6000.00', f"Input: {inputs} | Expected: 6000.00 | Got: {total}"

def test_alternating_signs():
    """Test with alternating positive and negative"""
    inputs = [5, -2, 10, -3, 15, 0]
    count, total = run_exercise4(*inputs)
    assert count == '3', f"Input: {inputs} | Expected: 3 | Got: {count}"
    assert total == '30.00', f"Input: {inputs} | Expected: 30.00 | Got: {total}"

def test_small_decimals():
    """Test with small decimal numbers"""
    inputs = [0.1, 0.2, 0.3, 0]
    count, total = run_exercise4(*inputs)
    assert count == '3', f"Input: {inputs} | Expected: 3 | Got: {count}"
    assert total == '0.60', f"Input: {inputs} | Expected: 0.60 | Got: {total}"
