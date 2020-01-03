"""
"""

from random import choice, randint, shuffle
from typing import List

import pytest

from app import collinear_pnts_lines


def random_non_collinear_points(num_points=10) -> List[tuple]:
    """Helper func to generate random (x, y) in 2D with possibility of duplicates.
    for simplicity -10 <= x <= 10 so is -10 <= y <= +10
    """
    nums = range(-10, 11)
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

def test_incomplete_input():
    pnt_set0 = []
    pnt_set1 = [(0, 0)]
    pnt_set2 = [(0, 0), (1, 1)]
    pnt_set3 = [(0, 0), (1, 1), (2, 2)]

    assert collinear_pnts_lines(pnt_set0) == []
    assert collinear_pnts_lines(pnt_set1) == []
    assert collinear_pnts_lines(pnt_set2) == []
    assert collinear_pnts_lines(pnt_set3) != []


def test_raise_exception_when_input_data_is_not_expected_list():
    with pytest.raises(TypeError):
        assert collinear_pnts_lines('some_string')
        assert collinear_pnts_lines('{0: 0, 1: 1, 2: 2}')
        assert collinear_pnts_lines('tuple((0, 0), (1, 1), (2, 2))')
        assert collinear_pnts_lines('set((0, 0), (1, 1), (2, 2)))')


def test_raise_exception_when_input_data_xy_points_is_not_expected_tuple_of_2():
    with pytest.raises(ValueError):
        assert collinear_pnts_lines(['1, 2', '4, 4'])
        assert collinear_pnts_lines([[1, 2], [4, 4]])
        assert collinear_pnts_lines([(1, 2, 3), (4, 4, 4)])



def test_3_collinear_points_1_line():
    points = [(0, 0), (1, 1), (2, 2)]
    assert collinear_pnts_lines(points) == [(1, 0)]
    assert len(collinear_pnts_lines(points)) == 1

    pnt_set1 = [(0, 0), (-1, -1), (-2, -2)]
    assert collinear_pnts_lines(pnt_set1) == [(1, 0)]
    assert len(collinear_pnts_lines(pnt_set1)) == 1

    pnt_set2 = [(0, 0), (-1, -1), (-2, -2)]
    assert collinear_pnts_lines(pnt_set2) == [(1, 0)]
    assert len(collinear_pnts_lines(pnt_set2)) == 1

    pnt_set3 = [(4, -28), (9, -53), (0, -8)]
    x0, y0 = pnt_set3[0]
    x1, y1 = pnt_set3[2]
    x2, y2 = pnt_set3[1]
    slop = (y0 - y2) / (x0 - x2)
    assert slop == (y2 - y1) / (x2 - x1)
    intercept = y0 - slop * x0
    assert intercept == y2 - slop * x2
    assert intercept == y1 - slop * x1
    assert len(collinear_pnts_lines(points)) == 1
    assert collinear_pnts_lines(pnt_set3) == [(slop, intercept)]

    pnt_set4 = [(9, -42), (-2, 2), (3, -18)]
    x0, y0 = pnt_set4[0]
    x1, y1 = pnt_set4[2]
    x2, y2 = pnt_set4[1]
    slop = (y0 - y2) / (x0 - x2)
    assert slop == (y2 - y1) / (x2 - x1)
    intercept = y0 - slop * x0
    assert intercept == y2 - slop * x2
    assert intercept == y1 - slop * x1
    assert len(collinear_pnts_lines(points)) == 1
    assert collinear_pnts_lines(pnt_set4) == [(slop, intercept)]


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



