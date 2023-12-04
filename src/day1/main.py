import sys

def get_first_number(line: str) -> int:
    for char in line:
        value: int = ord(char) - ord('0')

        if (value >= 0 and value <= 9):
            return value
        
    raise Exception("Input string contains no numbers")

def get_calibration_value(line: str) -> int:
    first_value = get_first_number(line)
    last_value = get_first_number(line[::-1])

    return (first_value * 10) + last_value

if __name__ == "__main__":
    filename = sys.argv[1]

    with open(filename, "r") as f:
        lines = f.readlines()
        result = sum([get_calibration_value(line) for line in lines])

        print(result)