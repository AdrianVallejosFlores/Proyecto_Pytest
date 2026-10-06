import pytest

def test_conversion_grados_a_radianes():
    import math
    assert 180 * math.pi / 180 == pytest.approx(math.pi)