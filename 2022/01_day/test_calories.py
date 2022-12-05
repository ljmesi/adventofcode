#!/usr/bin/env python3
"""tests for calories.py"""

from subprocess import getstatusoutput

prg = "./calories.py"
ex = "elfs_and_calories.json"
test1 = "test1.json"
test2 = "test2.json"

# --------------------------------------------------
def test_ex():
    """Test on more than one file"""
    rv, out = getstatusoutput(f"{prg} --file {ex}")
    assert rv == 0
    assert out.rstrip() == "Elf4 has most calories.\nHe has 24000 calories."


# --------------------------------------------------
def test_1():
    """Test on more than one file"""
    rv, out = getstatusoutput(f"{prg} --file {test1}")
    assert rv == 0
    assert out.rstrip() == "Elf1 has most calories.\nHe has 6000 calories."


# --------------------------------------------------
def test_2():
    """Test on more than one file"""
    rv, out = getstatusoutput(f"{prg} --file {test2}")
    assert rv == 0
    assert out.rstrip() == "Elf3 has most calories.\nHe has 6000 calories."
