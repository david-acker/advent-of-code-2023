#! /bin/bash

echo "Day 1: Trebuchet?!"
echo

basePath="../../input/day1/"

# Test Input
testInput1FilePath="${basePath}test_input_1.txt"
testInput2FilePath="${basePath}test_input_2.txt"

if test -f $testInputFilePath; then
    echo "Results for test input data:"
    python3 main.py $testInput1FilePath $testInput2FilePath
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