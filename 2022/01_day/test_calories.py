#!/usr/bin/env python3
"""tests for calories.py"""

from subprocess import getstatusoutput

prg = "./calories.py"
ex = "aoc_input.txt"
test1 = "test1.txt"
test2 = "test2.txt"

# --------------------------------------------------
def test_ex():
    """Test on more than one file"""
    rv, out = getstatusoutput(f"{prg} --file {ex}")
    assert rv == 0
    assert out.rstrip() == "Elf113 has most calories.\nHe has 71506 calories."


# --------------------------------------------------
def test_1():
    """Test on more than one file"""
    rv, out = getstatusoutput(f"{prg} --file {test1}")
    assert rv == 0
    assert out.rstrip() == "Elf3 has most calories.\nHe has 6 calories."
