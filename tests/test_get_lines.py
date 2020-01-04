"""
"""

import pytest
from random import randint, shuffle

from app import get_lines


def test_raise_exception_if_input_missing():
    with pytest.raises(TypeError):
        get_lines()


def test_less_than_3_points_input():
    """Correct Type but Insufficient Data"""
    pnt_set0 = []
    pnt_set1 = [(0, 0)]
    pnt_set2 = [(0, 0), (1, 1)]
    assert get_lines(pnt_set0) == []
    assert get_lines(pnt_set0) == []
    assert get_lines(pnt_set1) == []
    assert get_lines(pnt_set2) == []

    pnt_set3 = [(0, 0), (1, 1), (2, 2)]  # collinear points
    assert get_lines(pnt_set3) != []
    assert len(get_lines(pnt_set3)) == 1


def test_exception_raised_if_input_isnot_list():
    with pytest.raises(TypeError):
        points = tuple([(0, 0), (1, 1), (2, 2)])
        get_lines(points)


def test_raise_exception_if_xy_points_not_tuple_of_2_numeric():
    # Cartesian points not in planned immutable data structure i.e. tuple
    with pytest.raises(TypeError):
        get_lines([[0, 0], [1, 1], [2, 2]])

    # Too many values to unpack (expected 2, got 3)
    with pytest.raises(ValueError):
        get_lines([(0, 0), (1, 1), (2, 2, 9999)])

    # Not enough values to unpack (expected 2, got 1)
    with pytest.raises(ValueError):
        get_lines([(0,), (1,), (2,)])


# Core Algorithm Tests                          ----------------------------------------------------------
# Trivial Test Cases
def test_3_collinear_points_1_line():
    points = [(0, 0), (1, 1), (2, 2)]
    assert get_lines(points) == [(1, 0)]
    assert len(get_lines(points)) == 1

    pnt_set1 = [(0, 0), (-1, -1), (-2, -2)]
    assert get_lines(pnt_set1) == [(1, 0)]
    assert len(get_lines(pnt_set1)) == 1

    pnt_set2 = [(0, 0), (-1, -1), (-2, -2)]
    assert get_lines(pnt_set2) == [(1, 0)]
    assert len(get_lines(pnt_set2)) == 1

    pnt_set3 = [(4, -28), (9, -53), (0, -8)]
    x0, y0 = pnt_set3[0]
    x1, y1 = pnt_set3[2]
    x2, y2 = pnt_set3[1]
    slop = (y0 - y2) / (x0 - x2)
    assert slop == (y2 - y1) / (x2 - x1)
    intercept = y0 - slop * x0
    assert intercept == y2 - slop * x2
    assert intercept == y1 - slop * x1
    assert len(get_lines(points)) == 1
    assert get_lines(pnt_set3) == [(slop, intercept)]

    pnt_set4 = [(9, -42), (-2, 2), (3, -18)]
    x0, y0 = pnt_set4[0]
    x1, y1 = pnt_set4[2]
    x2, y2 = pnt_set4[1]
    slop = (y0 - y2) / (x0 - x2)
    assert slop == (y2 - y1) / (x2 - x1)
    intercept = y0 - slop * x0
    assert intercept == y2 - slop * x2
    assert intercept == y1 - slop * x1
    assert len(get_lines(points)) == 1
    assert get_lines(pnt_set4) == [(slop, intercept)]


def test_10_y_axis_parallel_lines():
    y_axis_parallel_lines = []
    for _ in range(10):
        x = randint(-100000, 100001)
        y_axis_parallel_lines += [(x, randint(-10000, 10001)) for _ in range(10)]

    shuffle(y_axis_parallel_lines)
    assert len(get_lines(y_axis_parallel_lines)) == 10


def test_10_x_axis_parallel_lines():
    x_axis_parallel_lines = []
    for _ in range(10):
        y = randint(-100000, 100001)
        x_axis_parallel_lines += [(randint(-10000, 10001), y) for _ in range(10)]

    shuffle(x_axis_parallel_lines)
    assert len(get_lines(x_axis_parallel_lines)) == 10
