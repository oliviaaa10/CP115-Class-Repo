import subprocess
import sys
import os

def run_exercise6(*inputs):
    """Run exercise6.py with given inputs and return output lines."""
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    script_path = os.path.join(script_dir, 'exercise6.py')

    input_data = '\n'.join(str(x) for x in inputs) + '\n'

    result = subprocess.run([sys.executable, script_path],
                          input=input_data, text=True, capture_output=True)

    if result.returncode != 0:
        raise Exception(f"Script failed: {result.stderr}")

    lines = result.stdout.strip().split('\n')
    return lines[0], lines[1]

def test_all_age_groups():
    """Test with all different age groups"""
    inputs = [10, 15, 25, 70, -1]
    tickets, revenue = run_exercise6(*inputs)
    assert tickets == '4', f"Input: {inputs} | Expected: 4 | Got: {tickets}"
    assert revenue == '43', f"Input: {inputs} | Expected: 43 | Got: {revenue}"

def test_only_children():
    """Test with only children tickets"""
    inputs = [5, 8, 12, -1]
    tickets, revenue = run_exercise6(*inputs)
    assert tickets == '3', f"Input: {inputs} | Expected: 3 | Got: {tickets}"
    assert revenue == '24', f"Input: {inputs} | Expected: 24 | Got: {revenue}"

def test_only_teens():
    """Test with only teen tickets"""
    inputs = [13, 15, 17, -1]
    tickets, revenue = run_exercise6(*inputs)
    assert tickets == '3', f"Input: {inputs} | Expected: 3 | Got: {tickets}"
    assert revenue == '30', f"Input: {inputs} | Expected: 30 | Got: {revenue}"

def test_only_adults():
    """Test with only adult tickets"""
    inputs = [18, 30, 64, -1]
    tickets, revenue = run_exercise6(*inputs)
    assert tickets == '3', f"Input: {inputs} | Expected: 3 | Got: {tickets}"
    assert revenue == '45', f"Input: {inputs} | Expected: 45 | Got: {revenue}"

def test_only_seniors():
    """Test with only senior tickets"""
    inputs = [65, 75, 80, -1]
    tickets, revenue = run_exercise6(*inputs)
    assert tickets == '3', f"Input: {inputs} | Expected: 3 | Got: {tickets}"
    assert revenue == '30', f"Input: {inputs} | Expected: 30 | Got: {revenue}"

def test_boundary_ages():
    """Test boundary ages for each category"""
    inputs = [0, 12, 13, 17, 18, 64, 65, -1]
    tickets, revenue = run_exercise6(*inputs)
    assert tickets == '7', f"Input: {inputs} | Expected: 7 | Got: {tickets}"
    assert revenue == '76', f"Input: {inputs} | Expected: 76 | Got: {revenue}"

def test_no_tickets():
    """Test with no tickets sold"""
    inputs = [-1]
    tickets, revenue = run_exercise6(*inputs)
    assert tickets == '0', f"Input: {inputs} | Expected: 0 | Got: {tickets}"
    assert revenue == '0', f"Input: {inputs} | Expected: 0 | Got: {revenue}"

def test_single_ticket():
    """Test with single ticket"""
    inputs = [25, -1]
    tickets, revenue = run_exercise6(*inputs)
    assert tickets == '1', f"Input: {inputs} | Expected: 1 | Got: {tickets}"
    assert revenue == '15', f"Input: {inputs} | Expected: 15 | Got: {revenue}"

def test_child_boundary():
    """Test child age boundary at 12"""
    inputs = [12, -1]
    tickets, revenue = run_exercise6(*inputs)
    assert tickets == '1', f"Input: {inputs} | Expected: 1 | Got: {tickets}"
    assert revenue == '8', f"Input: {inputs} | Expected: 8 | Got: {revenue}"

def test_teen_boundary():
    """Test teen age boundaries at 13 and 17"""
    inputs = [13, 17, -1]
    tickets, revenue = run_exercise6(*inputs)
    assert tickets == '2', f"Input: {inputs} | Expected: 2 | Got: {tickets}"
    assert revenue == '20', f"Input: {inputs} | Expected: 20 | Got: {revenue}"
