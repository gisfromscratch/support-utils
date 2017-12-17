"""
Finds data errors in the specified file.
"""

import csv
import sys
from attribute_rule import AttributeRule, NonVisibleCodepointsRule


def main(file_path, delimiter):
    """
    Reads the specified file.
    file_path -- the input file path
    """
    rule = AttributeRule(r"\s*")
    controlRule = NonVisibleCodepointsRule()
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=delimiter)
        for line in reader:
            for value in line:
                if rule.matches(value):
                    print(value)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        main(sys.argv[1], '\t')
