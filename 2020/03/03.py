# -*- coding: utf-8 -*-
from math import prod


def get_tree_encountered_counter(
        input_data: list[str],
        x_increment: int,
        y_increment: int,
        start_x: int = 0,
        start_y: int = 0):
    x = start_x
    input_data = input_data[start_y:]
    tree_encountered_counter = 0
    while True:
        try:
            if input_data[0][x % len(input_data[0])] == "#":
                tree_encountered_counter = tree_encountered_counter + 1
            x = x + x_increment
            input_data = input_data[y_increment:]
        except IndexError:
            break
        
    return tree_encountered_counter


if __name__ == "__main__":
    with open("data03.txt") as f:
        data = f.readlines()
    data = [line.strip() for line in data]
    slopes = (
        get_tree_encountered_counter(
            input_data=data,
            x_increment=1,
            y_increment=1,
            start_x=0,
            start_y=0),
        get_tree_encountered_counter(
            input_data=data,
            x_increment=3,
            y_increment=1,
            start_x=0,
            start_y=0),
        get_tree_encountered_counter(
            input_data=data,
            x_increment=5,
            y_increment=1,
            start_x=0,
            start_y=0),
        get_tree_encountered_counter(
            input_data=data,
            x_increment=7,
            y_increment=1,
            start_x=0,
            start_y=0),
        get_tree_encountered_counter(
            input_data=data,
            x_increment=1,
            y_increment=2,
            start_x=0,
            start_y=0),
    )
    print(prod(slopes))
