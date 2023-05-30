import pytest
from utils import arrs


@pytest.mark.parametrize('array, index, default, result', [
    ([1, 2, 3], 1, "test", 2),
    ([], 0, "test", "test")
                         ])
def test_get(array, index, default, result):
    assert arrs.get(array, index, default) == result


@pytest.mark.parametrize('array, index, default, result', [
    ([1, 2, 3, 4], 1, 3, [2, 3]),
    ([1, 2, 3], 1, None, [2, 3]),
    ([], 1, None, []),
    ([1, 2, 3], -5, None, [1, 2, 3]),
    ([1, 2, 3], -2, None, [2, 3])
])
def test_slice(array, index, default, result):
    assert arrs.my_slice(array, index, default) == result

