from typing import List, Tuple
import pytest
from assertpy import assert_that


def is_increasing(v1: int, v2: int) -> bool:
    return v2 > v1


def get_cons_pairs(values: List[int]) -> List[Tuple[int, int]]:
    return [
        (i, j)
        for i, j in zip(values[:-1], values[1:])
    ]


def count_increasing_values(values: List[Tuple[int, int]]) -> int:
    return sum([
        is_increasing(*v)
        for v in values
    ])


def get_windows_of(window_size: int, values: List[int]) -> List[List[int]]:
    return [
        values[i:i+window_size]
        for i in range(len(values)-window_size+1)
    ]


def get_sums_of(values: List[List[int]]) -> List[int]:
    return [
        sum(v)
        for v in values
    ]


# ----


@pytest.fixture
def input():
    with open('input.txt') as f:
        return [int(i) for i in f.readlines()]


def test_input_size(input):
    assert_that(input).is_length(2000)


def test_bigger_value_increasing():
    assert_that(is_increasing(0, 1)).is_true()


def test_get_all_consequite_pair_of_list():
    pairs = get_cons_pairs([0, 1, 2, 3])
    assert_that(pairs).is_equal_to([
        (0, 1),
        (1, 2),
        (2, 3)
    ])


def test_count_increasing_values():
    assert_that(count_increasing_values([
        (0, 1),
        (2, 3),
        (10, 3)
    ])).is_equal_to(2)


def test_input(input):
    pairs = get_cons_pairs(input)
    assert_that(
        count_increasing_values(pairs)
    ).is_equal_to(1557)


def test_get_sliding_windows():
    windows = get_windows_of(3, [1, 2, 3, 4])
    assert_that(windows).is_equal_to([
        [1, 2, 3],
        [2, 3, 4]
    ])


def test_get_sum_of_elements():
    sums = get_sums_of([[1, 2], [4, 5, 6]])
    assert_that(sums).is_equal_to([3, 15])


def test_input_with_window(input):
    windows = get_windows_of(3, input)
    values = get_sums_of(windows)
    pairs = get_cons_pairs(values)
    assert_that(
        count_increasing_values(pairs)
    ).is_equal_to(1608)
