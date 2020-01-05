"""
"""

import pytest
from random import randint, shuffle

from app.get_collinears import get_collinears


def test_raise_exception_if_missing_input():
    with pytest.raises(ValueError) as exception_info:
        get_collinears()
        assert 'Expected input argument is missing.' in str(exception_info.value)


def test_raise_exception_if_input_type_not_list():
    with pytest.raises(TypeError) as exception_info:
        xy_input = ((-1, -1), (3, 3), (6, 6), (0, 0))
        get_collinears(xy_input)
        assert 'Expected input type is list.' in str(exception_info.value)


def test_less_than_3_points_input():
    """Correct Type but Insufficient Data"""
    pnt_set0 = []
    pnt_set1 = [(0, 0)]
    pnt_set2 = [(0, 0), (1, 1)]
    assert get_collinears(pnt_set0) == []
    assert get_collinears(pnt_set0) == []
    assert get_collinears(pnt_set1) == []
    assert get_collinears(pnt_set2) == []

    pnt_set3 = [(0, 0), (1, 1), (2, 2)]  # collinear points
    assert get_collinears(pnt_set3) != []
    assert len(get_collinears(pnt_set3)) == 1


def test_raise_exception_if_xy_not_exactly_2_elements():

    # Too many values to unpack
    with pytest.raises(ValueError) as exception_info:
        get_collinears([(3, 2, 5), (4, -1, -1), (8, 1, 2), (-7, 0, 2)])
    assert 'too many values to unpack' in str(exception_info.value)

    # Not enough values to unpack
    with pytest.raises(ValueError) as exception_info:
        get_collinears([(3, ), (4, ), (8, ), (-7, )])
    assert 'not enough values to unpack' in str(exception_info.value)


def test_10_y_axis_parallel_lines():
    y_axis_parallel_lines = []
    for _ in range(10):
        x = randint(-100000, 100001)
        y_axis_parallel_lines += [(x, randint(-10000, 10001)) for _ in range(10)]

    shuffle(y_axis_parallel_lines)
    assert len(get_collinears(y_axis_parallel_lines)) == 10


def test_10_x_axis_parallel_lines():
    x_axis_parallel_lines = []
    for _ in range(10):
        y = randint(-100000, 100001)
        x_axis_parallel_lines += [(randint(-10000, 10001), y) for _ in range(10)]

    shuffle(x_axis_parallel_lines)
    assert len(get_collinears(x_axis_parallel_lines)) == 10


# Trivial Test Cases
def test_3_collinear_points_1_line():
    points = [(0, 0), (1, 1), (2, 2)]
    assert get_collinears(points) == [(1, 0)]
    assert len(get_collinears(points)) == 1

    pnt_set1 = [(0, 0), (-1, -1), (-2, -2)]
    assert get_collinears(pnt_set1) == [(1, 0)]
    assert len(get_collinears(pnt_set1)) == 1

    pnt_set2 = [(0, 0), (-1, -1), (-2, -2)]
    assert get_collinears(pnt_set2) == [(1, 0)]
    assert len(get_collinears(pnt_set2)) == 1

    pnt_set3 = [(4, -28), (9, -53), (0, -8)]
    x0, y0 = pnt_set3[0]
    x1, y1 = pnt_set3[2]
    x2, y2 = pnt_set3[1]
    slop = (y0 - y2) / (x0 - x2)
    assert slop == (y2 - y1) / (x2 - x1)
    intercept = y0 - slop * x0
    assert intercept == y2 - slop * x2
    assert intercept == y1 - slop * x1
    assert len(get_collinears(points)) == 1
    assert get_collinears(pnt_set3) == [(slop, intercept)]

    pnt_set4 = [(9, -42), (-2, 2), (3, -18)]
    x0, y0 = pnt_set4[0]
    x1, y1 = pnt_set4[2]
    x2, y2 = pnt_set4[1]
    slop = (y0 - y2) / (x0 - x2)
    assert slop == (y2 - y1) / (x2 - x1)
    intercept = y0 - slop * x0
    assert intercept == y2 - slop * x2
    assert intercept == y1 - slop * x1
    assert len(get_collinears(points)) == 1


