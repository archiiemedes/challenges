# https://codility.com/programmers/task/binary_gap/


def solution(N):
    bin_n = format(N, 'b')
    gap_count = 0
    max_gap_len = 0
    for char in bin_n:
        if int(char) == 0:
            gap_count += 1
        elif int(char) == 1:
            if gap_count > max_gap_len:
                max_gap_len = gap_count
            gap_count = 0
    return max_gap_len


def test_1041():
    #1041 = 10000010001
    assert solution(1041) == 5


def test_328():
    # 328 = 101001000
    assert solution(328) == 2


def test_6():
    # 6 = 110
    assert solution(6) == 0


def test_805306373():
    assert solution(805306373) == 25