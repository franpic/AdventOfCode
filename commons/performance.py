# -*- coding: utf-8 -*-

from time import perf_counter


class ChronometerDecorator:
    def __init__(self, f):
        self._f = f

    def __call__(self, *args, **kwargs):
        start_time = perf_counter()
        ret = self._f(*args, **kwargs)
        print(
            f"function {self._f.__name__} elapsed time:"
            f" {(perf_counter() - start_time):.2f} seconds")
        return ret
