#!/usr/bin/python3

import sys
from os.path import exists
from zipfile import ZipFile
from subprocess import run

if len(sys.argv) == 1:
    print("Enter level number")
    exit(-1)

level, test_cases = sys.argv[1], [sys.argv[2]] if len(sys.argv) >= 3 else [1, 2, 3, 4, 5]

run("make")

if not exists(f"level{level}_1.in"):
    with ZipFile(f"level{level}.zip", "r") as archive:
        archive.extractall()

for test_case in test_cases:
    with open(f"level{level}_{test_case}.in", "r") as in_file:
        with open(f"level{level}_{test_case}.out", "w") as out_file:
            run("./main", stdin=in_file, stdout=out_file)