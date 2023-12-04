#! /bin/bash

echo "Day 1: Trebuchet?!"
echo

basePath="../../input/day1/"
testInputFilePath="${basePath}input_test.txt"

if test -f $testInputFilePath; then
    echo "Results for test input data:"
    python3 main.py $testInputFilePath
else
    echo "The test input file count not be found."
fi

echo

inputFilePath="${basePath}input.txt"

if test -f $inputFilePath; then
    echo "Results for input data:"
    python3 main.py $inputFilePath
else
    echo "The input file could not be found."
fi