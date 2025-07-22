#!/usr/bin/env python3
import subprocess
import sys
import re
import argparse

TOL = 1e-6

def extract_numbers(text):
    """Extract ints/floats (including scientific notation) from text."""
    nums = re.findall(r"-?\d+\.?\d*(?:[eE][+-]?\d+)?", text)
    return [float(n) for n in nums]

def run_test(script, input_data, expected):
    proc = subprocess.run(
        [sys.executable, script],
        input=input_data,
        text=True,
        capture_output=True
    )
    actual = extract_numbers(proc.stdout)
    ok = (
        len(actual) == len(expected) and
        all(abs(a - e) < TOL for a, e in zip(actual, expected))
    )
    if ok:
        print(f"PASS {script} | in={input_data.strip()} → out={actual}")
    else:
        print(f"\nFAIL {script}")
        print(f"  Input:    {input_data.strip()}")
        print(f"  Expected: {expected}")
        print(f"  Actual:   {actual}")
    return ok

def parse_args():
    parser = argparse.ArgumentParser(
        description="Run Lab 03 tests (optionally for a single student script)"
    )
    parser.add_argument(
        "--script",
        help="Only run tests for this student script (e.g. lab_03_2.py)"
    )
    return parser.parse_args()

def main():
    args = parse_args()

    tests = [
        # Scenario 1: TOTAL_PAYMENT
        ("lab_03_2.py", "0\n", [0.0]),
        ("lab_03_2.py", "1\n", [287.50]),
        ("lab_03_2.py", "5\n", [1437.50]),

        # Scenario 2: KB → MB, GB, TB, PB
        ("lab_03_3.py", "0\n",    [0.0, 0.0, 0.0, 0.0]),
        ("lab_03_3.py", "1024\n", [1.0, 0.0009765625, 9.5367431640625e-07, 9.313225746154785e-10]),
        ("lab_03_3.py", "1536\n", [1.5, 0.00146484375, 1.430511474609375e-06, 1.4015116691589355e-09]),

        # Scenario 3: TOTAL_COST
        ("lab_03_4.py", "0\n",  [3.00]),
        ("lab_03_4.py", "5\n",  [4.00]),
        ("lab_03_4.py", "10\n", [5.00]),

        # Scenario 4: TOTAL_CALORIES
        ("lab_03_5.py", "0\n", [0.0]),
        ("lab_03_5.py", "1\n", [3000.0]),
        ("lab_03_5.py", "4\n", [12000.0]),

        # Scenario 5: WAGE
        ("lab_03_6.py", "10 10 4 4\n", [168.00]),
        ("lab_03_6.py", "5 5 2 2\n",   [42.00]),
        ("lab_03_6.py", "20 15 5 5\n", [550.00]),

        # Scenario 6: Temperature Conversion
        ("lab_03_7.py", "0\n",        [32.0, 273.15]),
        ("lab_03_7.py", "100\n",      [212.0, 373.15]),
        ("lab_03_7.py", "-273.15\n",  [-459.67, 0.0]),

        # Scenario 7: Simple Interest + Monthly
        ("lab_03_8.py", "1000\n5\n2\n", [100.0, 1100.0, 100.0 / 24]),
        ("lab_03_8.py", "500\n3\n1\n",   [15.0, 515.0, 15.0 / 12]),
        ("lab_03_8.py", "200\n0\n5\n",   [0.0, 200.0, 0.0]),
    ]

    if args.script:
        tests = [t for t in tests if t[0] == args.script]

    failures = False
    for script, inp, exp in tests:
        if not run_test(script, inp, exp):
            failures = True

    if failures:
        sys.exit(1)
    print("\n✅ All tests passed.")

if __name__ == "__main__":
    main()
