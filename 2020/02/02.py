# -*- coding: utf-8 -*-

from time import process_time
import re

if __name__ == "__main__":
    with open("data02.txt") as f:
        pattern_to_parse_password_policies = re.compile(
            r"(\d+)-(\d+) (\w): (\w+)")
        valid_passwords_count = 0
        for line in f:
            min_instancies_allowed, max_instancies_allowed, character, password\
                = pattern_to_parse_password_policies.match(line).groups()
            # print(pattern_to_parse_password_policies.match(line).groups())
            if \
                    int(min_instancies_allowed) <= \
                    password.count(character) <= \
                    int(max_instancies_allowed):
                valid_passwords_count = valid_passwords_count + 1
        print(valid_passwords_count)
