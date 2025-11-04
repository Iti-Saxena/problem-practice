import os
import typing
import pytest

def load_solution_class():
    src_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'src', 'merge_sort_problem.py'))
    with open(src_path, 'r', encoding='utf-8') as fh:
        src = fh.read()
    globs = {'__file__': src_path, '__name__': 'merge_sort_problem1', 'List': typing.List}
    exec(compile(src, src_path, 'exec'), globs)
    return globs['Solution']

Solution = load_solution_class()

@pytest.mark.parametrize(
    "nums1,m,nums2,n,expected",
    [
        ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),           # example 1
        ([1], 1, [], 0, [1]),                                   # example 2
        ([0], 0, [1], 1, [1]),                                  # example 3 (m=0)
        ([5,6,7,0,0,0], 3, [1,2,3], 3, [1,2,3,5,6,7]),          # all nums2 smaller
        ([-2,0,0,0,3,0], 3, [-3,0,1], 3, [-3,-2,0,0,0,1]),      # negatives & duplicates
        ([1,2,2,3,0,0,0], 4, [2,2,3], 3, [1,2,2,2,2,3,3]),      # duplicates overlap
        ([2,0], 1, [2], 1, [2,2]),                              # same single values
    ]
)
def test_merge_parametrized(nums1, m, nums2, n, expected):
    a = list(nums1)
    b = list(nums2)
    Solution().merge(a, m, b, n)
    assert a == expected