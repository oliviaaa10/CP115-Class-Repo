import subprocess
import sys
import os

def run_exercise2():
    """Run exercise2.py and return output."""
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    script_path = os.path.join(script_dir, 'exercise2.py')

    result = subprocess.run([sys.executable, script_path],
                          text=True, capture_output=True)

    if result.returncode != 0:
        raise Exception(f"Script failed: {result.stderr}")

    return result.stdout.strip()

def test_finds_correct_number():
    """Test that it finds 91 (the first number divisible by both 7 and 13)"""
    result = run_exercise2()
    assert result == '91', f"Input: None | Expected: 91 | Got: {result}"

def test_number_divisible_by_7():
    """Test that found number is divisible by 7"""
    result = int(run_exercise2())
    assert result % 7 == 0, f"Input: None | Expected: divisible by 7 | Got: {result}"

def test_number_divisible_by_13():
    """Test that found number is divisible by 13"""
    result = int(run_exercise2())
    assert result % 13 == 0, f"Input: None | Expected: divisible by 13 | Got: {result}"

def test_number_in_range():
    """Test that found number is between 1 and 100"""
    result = int(run_exercise2())
    assert 1 <= result <= 100, f"Input: None | Expected: between 1 and 100 | Got: {result}"

def test_is_91():
    """Test output is exactly 91"""
    result = run_exercise2()
    assert result == '91', f"Input: None | Expected: 91 | Got: {result}"

def test_divisible_by_both():
    """Test number divisible by both 7 and 13"""
    result = int(run_exercise2())
    assert result % 7 == 0 and result % 13 == 0, f"Input: None | Expected: divisible by 7 and 13 | Got: {result}"

def test_is_integer():
    """Test output is a valid integer"""
    result = run_exercise2()
    try:
        int(result)
        assert True
    except ValueError:
        assert False, f"Input: None | Expected: integer | Got: {result}"

def test_not_zero():
    """Test number is not zero"""
    result = int(run_exercise2())
    assert result != 0, f"Input: None | Expected: non-zero | Got: {result}"

def test_positive():
    """Test number is positive"""
    result = int(run_exercise2())
    assert result > 0, f"Input: None | Expected: positive | Got: {result}"

def test_is_lcm():
    """Test number is LCM of 7 and 13"""
    result = int(run_exercise2())
    assert result == 91, f"Input: None | Expected: 91 (LCM of 7 and 13) | Got: {result}"
