# -*- coding: utf-8 -*-

from itertools import product
from math import prod
from time import process_time
from commons.performance import ChronometerDecorator


@ChronometerDecorator
def get_addends_products(
        input_data: tuple[int],
        number_of_addends: int,
        sum_to_achieve: int) -> set[int]:
    p = product(input_data, repeat=number_of_addends)
    return set(prod(t) for t in p if sum(t) == sum_to_achieve)


if __name__ == "__main__":
    start_time = process_time()
    with open("data01.txt") as f:
        data = tuple(int(line.strip()) for line in f)

    for i in range(2, 5):
        print()
        addend_products = get_addends_products(
            input_data=data,
            number_of_addends=i,
            sum_to_achieve=2020)
        print(f"Part {i - 1}:\n{addend_products}")
        print()
    print(f"Total Elapsed time: {(process_time() - start_time):.2f} seconds")

