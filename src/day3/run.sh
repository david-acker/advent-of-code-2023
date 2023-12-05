#! /bin/bash

echo "Day 3: Gear Ratios"
echo

basePath="../../input/day3/"

# Test Input
testInputFilePath="${basePath}test_input.txt"

if test -f $testInputFilePath; then
    echo "Results for test input data:"
    python3 main.py $testInputFilePath
else
    echo "The test input file could not be found."
fi

echo

# Puzzle Input
inputFilePath="${basePath}input.txt"

if test -f $inputFilePath; then
    echo "Results for puzzle input data:"
    python3 main.py $inputFilePath
else
    echo "The input file could not be found."
fi