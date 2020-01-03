"""
"""

from random import choice, randint, shuffle
from typing import List

from app import three_collinears_lines


def random_non_collinear_points(num_points=10) -> List[tuple]:
    """Helper func to generate random (x, y) in 2D with possibility of duplicates.
    for simplicity -10 <= x <= 10 so is -10 <= y <= +10
    """
    nums = range(-10, 11)
    return [(choice(nums), choice(nums)) for _ in range(num_points)]


def random_collinear_points(num_lines=3,
                            min_collinear_points_per_line=3,
                            max_collinear_points_per_line=5) -> List[tuple]:
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


def test_3_collinear_points_1_line():
    points = [(0, 0), (1, 1), (2, 2)]
    assert three_collinears_lines(points) == [(1, 0)]
    assert len(three_collinears_lines(points)) == 1

    points = [(0, 0), (-1, -1), (-2, -2)]
    assert three_collinears_lines(points) == [(-1, 0)]
    assert len(three_collinears_lines(points)) == 1





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



