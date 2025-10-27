import subprocess
import sys
import os

def run_exercise3(*inputs):
    """Run exercise3.py with given inputs and return output lines."""
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    script_path = os.path.join(script_dir, 'exercise3.py')

    input_data = '\n'.join(str(x) for x in inputs) + '\n'

    result = subprocess.run([sys.executable, script_path],
                          input=input_data, text=True, capture_output=True)

    if result.returncode != 0:
        raise Exception(f"Script failed: {result.stderr}")

    lines = result.stdout.strip().split('\n')
    return lines[0], lines[1]

def test_all_valid_grades():
    """Test with all valid grades"""
    inputs = [85, 90, 78, -1]
    count, average = run_exercise3(*inputs)
    assert count == '3', f"Input: {inputs} | Expected: 3 | Got: {count}"
    assert average == '84.33', f"Input: {inputs} | Expected: 84.33 | Got: {average}"

def test_skip_invalid_high():
    """Test skipping grades over 100"""
    inputs = [85, 150, 90, -1]
    count, average = run_exercise3(*inputs)
    assert count == '2', f"Input: {inputs} | Expected: 2 | Got: {count}"
    assert average == '87.50', f"Input: {inputs} | Expected: 87.50 | Got: {average}"

def test_skip_invalid_low():
    """Test skipping grades less than 0 (but not stopping on -1)"""
    inputs = [85, -50, 90, -1]
    count, average = run_exercise3(*inputs)
    assert count == '2', f"Input: {inputs} | Expected: 2 | Got: {count}"
    assert average == '87.50', f"Input: {inputs} | Expected: 87.50 | Got: {average}"

def test_skip_both_invalid():
    """Test skipping both high and low invalid grades"""
    inputs = [85, 150, -50, 90, 101, 78, -1]
    count, average = run_exercise3(*inputs)
    assert count == '3', f"Input: {inputs} | Expected: 3 | Got: {count}"
    assert average == '84.33', f"Input: {inputs} | Expected: 84.33 | Got: {average}"

def test_boundary_values():
    """Test boundary values 0 and 100"""
    inputs = [0, 100, 50, -1]
    count, average = run_exercise3(*inputs)
    assert count == '3', f"Input: {inputs} | Expected: 3 | Got: {count}"
    assert average == '50.00', f"Input: {inputs} | Expected: 50.00 | Got: {average}"

def test_only_invalid_grades():
    """Test with only invalid grades before -1"""
    inputs = [150, 200, -50, -1]
    count, average = run_exercise3(*inputs)
    assert count == '0', f"Input: {inputs} | Expected: 0 | Got: {count}"
    assert average == '0.00', f"Input: {inputs} | Expected: 0.00 | Got: {average}"

def test_single_valid_grade():
    """Test with single valid grade"""
    inputs = [75, -1]
    count, average = run_exercise3(*inputs)
    assert count == '1', f"Input: {inputs} | Expected: 1 | Got: {count}"
    assert average == '75.00', f"Input: {inputs} | Expected: 75.00 | Got: {average}"

def test_all_100s():
    """Test with all perfect scores"""
    inputs = [100, 100, 100, -1]
    count, average = run_exercise3(*inputs)
    assert count == '3', f"Input: {inputs} | Expected: 3 | Got: {count}"
    assert average == '100.00', f"Input: {inputs} | Expected: 100.00 | Got: {average}"

def test_all_zeros():
    """Test with all zero grades"""
    inputs = [0, 0, 0, -1]
    count, average = run_exercise3(*inputs)
    assert count == '3', f"Input: {inputs} | Expected: 3 | Got: {count}"
    assert average == '0.00', f"Input: {inputs} | Expected: 0.00 | Got: {average}"

def test_mixed_boundary():
    """Test with mixed boundary values"""
    inputs = [0, 50, 100, -1]
    count, average = run_exercise3(*inputs)
    assert count == '3', f"Input: {inputs} | Expected: 3 | Got: {count}"
    assert average == '50.00', f"Input: {inputs} | Expected: 50.00 | Got: {average}"
