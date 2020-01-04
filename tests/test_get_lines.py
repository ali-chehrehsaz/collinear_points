"""
"""

from random import choice, randint, shuffle
from typing import List

import pytest

from app import get_lines


def random_non_collinear_points(num_points=10) -> List[tuple]:
    """Helper func to generate random (x, y) in 2D with possibility of duplicates.
    """
    nums = range(-10000, 10000)
    return [(choice(nums), choice(nums)) for _ in range(num_points)]


def random_collinear_points(num_lines=3,
                            min_collinear_points_per_line=3,
                            max_collinear_points_per_line=3) -> List[tuple]:
    """Helper func to generate 3 to 5 (x, y) points from 3 random lines in 2D
    A line represented as y=mx+b where m is the slop and b is line crossing y
    """
    nums = range(-10, 11)
    lines = [(choice(nums), choice(nums)) for _ in range(num_lines)]

    points = []
    seen = set()  # To prevent duplicate collinear points
    for m, b in lines:
        for _ in range(randint(min_collinear_points_per_line, max_collinear_points_per_line)):

            # Prevent duplicate collinear points
            while True:
                x = choice(nums)
                if x not in seen:
                    seen.add(x)
                    break

            points.append((x, x * m + b))

    return list(points)


# def test_3_collinear_points():
#     points = random_collinear_points(
#         num_lines=1,
#         min_collinear_points_per_line=3,
#         max_collinear_points_per_line=3
#     )
#     r = (list(three_collinears_lines(points)))
#     assert len(r) == 1
#
#
#     points = random_collinear_points(
#         num_lines=1,
#         min_collinear_points_per_line=4,
#         max_collinear_points_per_line=4
#     )
#     r = (list(three_collinears_lines(points)))
#     assert len(r) == 4
#
#     points = random_collinear_points(
#         num_lines=1,
#         min_collinear_points_per_line=5,
#         max_collinear_points_per_line=5
#     )
#     r = (list(three_collinears_lines(points)))
#     assert len(r) == factorial(5)/(factorial(3)*factorial(5-3))


# def test_one():
#     points = random_non_collinear_points(num_points=10) + \
#              random_collinear_points(
#                  num_lines=3,
#                  min_collinear_points_per_line=3,
#                  max_collinear_points_per_line=5
#              )
#     shuffle(points)
#
#     assert len(three_collinears_lines(points)) == 3

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
        get_lines([(0, ), (1, ), (2, )])


# Core Algorithm Tests                          ----------------------------------------------------------
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


def test_noncollinears():
    points = random_non_collinear_points(num_points=100)
    assert get_lines(points) == []


if __name__ == '__main__':
    points = random_non_collinear_points(num_points=0) + \
             random_collinear_points(
                    num_lines=1,
                    min_collinear_points_per_line=3,
                    max_collinear_points_per_line=3
    )
    shuffle(points)
    print(points)


    # print(random_collinear_points(num_lines=1, max_collinear_points_per_line=3))



