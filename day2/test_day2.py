from enum import Enum
from typing import Dict, List, Tuple
import pytest
from assertpy import assert_that


class Direction(Enum):
    FORWARD = 0
    UP = 1
    DOWN = 2


def get_path(path_text: List[str]) -> List[Tuple[Direction, int]]:
    lut = {
        'forward': Direction.FORWARD,
        'down': Direction.DOWN,
        'up': Direction.UP
    }

    def _convert_to_dir(d: str):
        direction, amount = d.split(' ')
        return lut[direction], int(amount)

    return [
        _convert_to_dir(d)
        for d in path_text
    ]


def get_sum_of_dir(direction: Direction, path: List[Tuple[Direction, int]]) -> int:
    return sum([
        a
        for d, a in path
        if d == direction
    ])


def get_sum_with_aim(path: List[Tuple[Direction, int]]) -> Tuple[int, int]:
    aim = 0
    forward = 0
    depth = 0
    for d, a in path:
        if d == Direction.DOWN:
            aim += a
        elif d == Direction.UP:
            aim -= a
        elif d == Direction.FORWARD:
            forward += a
            depth += a * aim

    return forward, depth

# ----


@pytest.fixture
def input():
    with open('input.txt') as f:
        return [i for i in f.readlines()]


def test_convert_text_to_dict():
    path_text = [
        'forward 5',
        'down 5',
        'forward 8',
        'up 3',
        'down 8',
        'forward 2'
    ]
    path = get_path(path_text)

    assert_that(path).is_equal_to([
        (Direction.FORWARD, 5),
        (Direction.DOWN, 5),
        (Direction.FORWARD, 8),
        (Direction.UP, 3),
        (Direction.DOWN, 8),
        (Direction.FORWARD, 2),
    ])


def test_calculate_one_dir():
    assert_that(
        get_sum_of_dir(Direction.FORWARD, [
            (Direction.FORWARD, 5),
            (Direction.DOWN, 5),
            (Direction.FORWARD, 8),
        ])
    ).is_equal_to(13)


def test_input(input):
    path = get_path(input)
    forward = get_sum_of_dir(Direction.FORWARD, path)
    up = get_sum_of_dir(Direction.UP, path)
    down = get_sum_of_dir(Direction.DOWN, path)

    depth = down - up

    assert_that(forward * depth).is_equal_to(1692075)


def test_sample_with_aim():
    path = [
        (Direction.FORWARD, 5),
        (Direction.DOWN, 5),
        (Direction.FORWARD, 8),
        (Direction.UP, 3),
        (Direction.DOWN, 8),
        (Direction.FORWARD, 2),
    ]
    forward, depth = get_sum_with_aim(path)
    assert_that(forward * depth).is_equal_to(900)


def test_input_with_aim(input):
    path = get_path(input)
    forward, depth = get_sum_with_aim(path)
    assert_that(forward * depth).is_equal_to(1749524700)
