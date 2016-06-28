from collections import deque


def solution(a, k):
    if k == 0:
        return a

    if not a:
        return []

    deq_a = deque(a)
    if k >= len(deq_a):
        new_k = k % len(deq_a)
        deq_a.rotate(new_k)
    else:
        deq_a.rotate(k)
    return list(deq_a)


def test_38976_3_times():
    assert solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]


def test_87236_rotated_7_times():
    assert solution([8, 7, 2, 3, 6], 7) == [3, 6, 8, 7, 2]


def test_k_lower_than_n():
    assert solution([5, -1000], 1) == [-1000, 5]