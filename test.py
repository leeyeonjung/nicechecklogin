import pytest

class TestReports:
    @pytest.fixture
    def setup(self):
        pass

    def test_1(self):
        assert (3+4==7)

    def test_2(self):
        a = (8-8)
        assert 5 / a == 1

    def test_3(self):
        assert (1+3) == 5

    def test_4(self):
        assert 3*4 == 12
