# import pytest

# class TestReports:
#     @pytest.fixture
#     def setup(self):
#         pass
#     def test_1(self):
#         assert True
#     def test_2(self):
#         assert 3 == 4
#     def test_3(self):
#         assert 3!=5

import pytest
from configuration import webDriver
import Logic.common as cm

class TestReports:
    @pytest.fixture
    def setup(self):
        pass
    def test_1(self):
        assert webDriver.cal()
    def test_2(self):
        assert cm.phoneNumberLoginclick()