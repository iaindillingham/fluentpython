import pytest

from fluentpython import vector


class TestVector:
    def test_abs(self):
        assert abs(vector.Vector(3, 4)) == 5

    def test_bool(self):
        assert bool(vector.Vector(3, 4)) is True

    def test_add(self):
        v1 = vector.Vector(3, 4)
        v2 = vector.Vector(3, 4)
        vr = v1 + v2
        # Vector does not implement "__eq__"
        assert vr.x == 6
        assert vr.y == 8
        # "__add__" returns a new vector
        assert v1 is not vr
        assert v2 is not vr

    def test_mul(self):
        v1 = vector.Vector(3, 4)
        vr = v1 * 2
        # Vector does not implement "__eq__"
        assert vr.x == 6
        assert vr.y == 8
        # "__mul__" returns a new vector
        assert v1 is not vr

    def test_rmul(self):
        # Vector does not implement "__rmul__"
        with pytest.raises(TypeError):
            2 * vector.Vector(3, 4)
