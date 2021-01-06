# -*- coding: utf-8 -*-

from time import process_time
import re

if __name__ == "__main__":
    with open("data01.txt") as f:
        data = tuple(int(line.strip()) for line in f)
    regex_to_parse_data = r"(\d+)-(\d+) (\w): (\w+)"
    re.compile(regex_to_parse_data)
    
    print(len())