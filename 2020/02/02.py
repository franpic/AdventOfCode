# -*- coding: utf-8 -*-

import re

pattern_to_parse_password_policies = re.compile(
    r"(\d+)-(\d+) (\w): (\w+)")


def get_part_one_valid_password_count(input_data: list[str]):
    valid_passwords_count = 0
    for line in input_data:
        min_instancies_allowed, max_instancies_allowed, character, password = \
            pattern_to_parse_password_policies.match(line).groups()
        if \
                int(min_instancies_allowed) <= \
                password.count(character) <= \
                int(max_instancies_allowed):
            valid_passwords_count = valid_passwords_count + 1
    return valid_passwords_count


def get_part_two_valid_password_count(input_data: list[str]):
    valid_passwords_count = 0
    for line in input_data:
        first_index, second_index, character, password = \
            pattern_to_parse_password_policies.match(line).groups()
        indexes_to_check = (int(first_index) - 1, int(second_index) - 1)
        characters_to_check = tuple(password[i] for i in indexes_to_check)
        if characters_to_check.count(character) == 1:
            valid_passwords_count = valid_passwords_count + 1
    return valid_passwords_count


if __name__ == "__main__":
    with open("data02.txt") as f:
        data = f.readlines()
    print(get_part_one_valid_password_count(input_data=data))
    print(get_part_two_valid_password_count(input_data=data))
