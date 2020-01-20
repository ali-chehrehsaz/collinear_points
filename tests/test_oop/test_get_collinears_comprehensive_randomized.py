"""
"""

from random import choice, randint, shuffle
from typing import List

from collinear.get_collinears_oop import get_lines


def random_non_collinear_points(num_non_collinears=10) -> List[tuple]:
    """Helper func to generate random (x, y) in 2D with possibility of duplicates.
    """
    boundary = 10000000000
    nums = range(-boundary, boundary)
    return [(choice(nums), choice(nums)) for _ in range(num_non_collinears)]


def random_collinear_points(
    num_lines=3, min_collinear_points_per_line=3, max_collinear_points_per_line=3
) -> List[tuple]:
    """Helper func to generate 3 to 5 (x, y) points from 3 random lines in 2D
    A line represented as y=mx+b where m is the slop and b is line crossing y
    """
    boundary = 10000000000
    nums = range(-boundary, boundary)
    lines = [(choice(nums), choice(nums)) for _ in range(num_lines)]

    points = []
    seen = set()  # To prevent duplicate collinear points
    for m, b in lines:
        for _ in range(
            randint(min_collinear_points_per_line, max_collinear_points_per_line)
        ):

            # Prevent duplicate collinear points
            while True:
                x = choice(nums)
                if x not in seen:
                    seen.add(x)
                    break

            points.append((x, x * m + b))

    return list(points)


def test_200_non_collinear_points():
    non_collinear_point = random_non_collinear_points(num_non_collinears=200)
    # non_collinear_point = [(23, 6342), (42, 7777), (54, 1), (24111, 0), (6, 77)]
    assert get_lines(non_collinear_point) == []  # Expecting no line to be found


def test_300_collinear_points_forming_100_lines():
    collinear_points = random_collinear_points(
        num_lines=100, min_collinear_points_per_line=3, max_collinear_points_per_line=3
    )
    assert len(get_lines(collinear_points)) == 100


def test_300_to_900_collinear_points_forming_100_lines():
    collinear_points = random_collinear_points(
        num_lines=100,
        min_collinear_points_per_line=3,
        max_collinear_points_per_line=9,  # each line can have `randomly` between 3 to 9 collinear points
    )
    assert len(get_lines(collinear_points)) == 100


# This is the most important comprehensive test
def test_about_400_collinears_and_400_non_collinears_mixed():
    mixed_points = random_collinear_points(
        num_lines=100, min_collinear_points_per_line=3, max_collinear_points_per_line=5
    ) + random_non_collinear_points(num_non_collinears=400)

    shuffle(mixed_points)  # Randomly rearrange all points in-place
    assert len(get_lines(mixed_points)) == 100
