import subprocess
import sys
import os

def run_exercise1(*inputs):
    """Run exercise1.py with given inputs and return output lines."""
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    script_path = os.path.join(script_dir, 'exercise1.py')

    input_data = '\n'.join(str(x) for x in inputs) + '\n'

    result = subprocess.run([sys.executable, script_path],
                          input=input_data, text=True, capture_output=True)

    if result.returncode != 0:
        raise Exception(f"Script failed: {result.stderr}")

    lines = result.stdout.strip().split('\n')
    return lines[0], lines[1]

def test_correct_first_attempt():
    """Test correct password on first attempt"""
    inputs = ['python123']
    logged_in, attempts = run_exercise1(*inputs)
    assert logged_in == 'True', f"Input: {inputs} | Expected: True | Got: {logged_in}"
    assert attempts == '1', f"Input: {inputs} | Expected: 1 | Got: {attempts}"

def test_correct_second_attempt():
    """Test correct password on second attempt"""
    inputs = ['wrong1', 'python123']
    logged_in, attempts = run_exercise1(*inputs)
    assert logged_in == 'True', f"Input: {inputs} | Expected: True | Got: {logged_in}"
    assert attempts == '2', f"Input: {inputs} | Expected: 2 | Got: {attempts}"

def test_correct_third_attempt():
    """Test correct password on third attempt"""
    inputs = ['wrong1', 'wrong2', 'python123']
    logged_in, attempts = run_exercise1(*inputs)
    assert logged_in == 'True', f"Input: {inputs} | Expected: True | Got: {logged_in}"
    assert attempts == '3', f"Input: {inputs} | Expected: 3 | Got: {attempts}"

def test_all_wrong_attempts():
    """Test all wrong attempts"""
    inputs = ['wrong1', 'wrong2', 'wrong3']
    logged_in, attempts = run_exercise1(*inputs)
    assert logged_in == 'False', f"Input: {inputs} | Expected: False | Got: {logged_in}"
    assert attempts == '3', f"Input: {inputs} | Expected: 3 | Got: {attempts}"

def test_stops_after_correct():
    """Test that it stops immediately after correct password"""
    inputs = ['python123']
    logged_in, attempts = run_exercise1(*inputs)
    assert logged_in == 'True', f"Input: {inputs} | Expected: True | Got: {logged_in}"
    assert attempts == '1', f"Input: {inputs} | Expected: 1 | Got: {attempts}"

def test_wrong_then_correct():
    """Test wrong password then correct"""
    inputs = ['wrongpass', 'python123']
    logged_in, attempts = run_exercise1(*inputs)
    assert logged_in == 'True', f"Input: {inputs} | Expected: True | Got: {logged_in}"
    assert attempts == '2', f"Input: {inputs} | Expected: 2 | Got: {attempts}"

def test_two_wrong_then_correct():
    """Test two wrong passwords then correct"""
    inputs = ['abc', 'def', 'python123']
    logged_in, attempts = run_exercise1(*inputs)
    assert logged_in == 'True', f"Input: {inputs} | Expected: True | Got: {logged_in}"
    assert attempts == '3', f"Input: {inputs} | Expected: 3 | Got: {attempts}"

def test_three_different_wrong():
    """Test three different wrong passwords"""
    inputs = ['password', 'admin', '12345']
    logged_in, attempts = run_exercise1(*inputs)
    assert logged_in == 'False', f"Input: {inputs} | Expected: False | Got: {logged_in}"
    assert attempts == '3', f"Input: {inputs} | Expected: 3 | Got: {attempts}"

def test_empty_passwords():
    """Test with empty password attempts"""
    inputs = ['', '', '']
    logged_in, attempts = run_exercise1(*inputs)
    assert logged_in == 'False', f"Input: {inputs} | Expected: False | Got: {logged_in}"
    assert attempts == '3', f"Input: {inputs} | Expected: 3 | Got: {attempts}"

def test_case_sensitive():
    """Test that password is case sensitive"""
    inputs = ['Python123', 'PYTHON123', 'python123']
    logged_in, attempts = run_exercise1(*inputs)
    assert logged_in == 'True', f"Input: {inputs} | Expected: True | Got: {logged_in}"
    assert attempts == '3', f"Input: {inputs} | Expected: 3 | Got: {attempts}"
