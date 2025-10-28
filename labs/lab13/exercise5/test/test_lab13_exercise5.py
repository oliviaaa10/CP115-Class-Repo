import subprocess
import sys
import os

def run_exercise5(*inputs):
    """Run exercise5.py with given inputs and return output lines."""
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    script_path = os.path.join(script_dir, 'exercise5.py')

    input_data = '\n'.join(str(x) for x in inputs) + '\n'

    result = subprocess.run([sys.executable, script_path],
                          input=input_data, text=True, capture_output=True)

    if result.returncode != 0:
        raise Exception(f"Script failed: {result.stderr}")

    lines = result.stdout.strip().split('\n')
    return lines[0], lines[1]

def test_all_valid_withdrawals():
    """Test with all valid withdrawals"""
    inputs = [20, 40, 100, 0]
    count, total = run_exercise5(*inputs)
    assert count == '3', f"Input: {inputs} | Expected: 3 | Got: {count}"
    assert total == '160', f"Input: {inputs} | Expected: 160 | Got: {total}"

def test_skip_below_minimum():
    """Test skipping amounts below $20"""
    inputs = [10, 20, 40, 0]
    count, total = run_exercise5(*inputs)
    assert count == '2', f"Input: {inputs} | Expected: 2 | Got: {count}"
    assert total == '60', f"Input: {inputs} | Expected: 60 | Got: {total}"

def test_skip_above_maximum():
    """Test skipping amounts above $500"""
    inputs = [600, 100, 200, 0]
    count, total = run_exercise5(*inputs)
    assert count == '2', f"Input: {inputs} | Expected: 2 | Got: {count}"
    assert total == '300', f"Input: {inputs} | Expected: 300 | Got: {total}"

def test_skip_not_multiples_of_20():
    """Test skipping amounts not multiples of 20"""
    inputs = [25, 20, 35, 40, 60, 0]
    count, total = run_exercise5(*inputs)
    assert count == '3', f"Input: {inputs} | Expected: 3 | Got: {count}"
    assert total == '120', f"Input: {inputs} | Expected: 120 | Got: {total}"

def test_maximum_valid_withdrawal():
    """Test maximum valid withdrawal of $500"""
    inputs = [500, 100, 0]
    count, total = run_exercise5(*inputs)
    assert count == '2', f"Input: {inputs} | Expected: 2 | Got: {count}"
    assert total == '600', f"Input: {inputs} | Expected: 600 | Got: {total}"

def test_only_invalid_withdrawals():
    """Test with only invalid withdrawals"""
    inputs = [15, 505, 35, 0]
    count, total = run_exercise5(*inputs)
    assert count == '0', f"Input: {inputs} | Expected: 0 | Got: {count}"
    assert total == '0', f"Input: {inputs} | Expected: 0 | Got: {total}"

def test_mixed_valid_invalid():
    """Test with mixed valid and invalid amounts"""
    inputs = [15, 20, 600, 40, 25, 60, 0]
    count, total = run_exercise5(*inputs)
    assert count == '3', f"Input: {inputs} | Expected: 3 | Got: {count}"
    assert total == '120', f"Input: {inputs} | Expected: 120 | Got: {total}"

def test_minimum_withdrawal():
    """Test minimum valid withdrawal of $20"""
    inputs = [20, 0]
    count, total = run_exercise5(*inputs)
    assert count == '1', f"Input: {inputs} | Expected: 1 | Got: {count}"
    assert total == '20', f"Input: {inputs} | Expected: 20 | Got: {total}"

def test_boundary_values():
    """Test boundary values 20 and 500"""
    inputs = [20, 500, 0]
    count, total = run_exercise5(*inputs)
    assert count == '2', f"Input: {inputs} | Expected: 2 | Got: {count}"
    assert total == '520', f"Input: {inputs} | Expected: 520 | Got: {total}"

def test_all_multiples_of_20():
    """Test all multiples of 20 in range"""
    inputs = [60, 80, 100, 120, 0]
    count, total = run_exercise5(*inputs)
    assert count == '4', f"Input: {inputs} | Expected: 4 | Got: {count}"
    assert total == '360', f"Input: {inputs} | Expected: 360 | Got: {total}"
